from flask import Flask,jsonify,request,send_file, render_template
import pandas as pd
from plotly.offline import iplot, init_notebook_mode, plot 
import plotly.graph_objs as go
import plotly.io as pio
import json
import plotly.figure_factory as ff
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
#-----------------------------------OFICIAL---------------------------------#

def id_4(data):
	aux = 0
	dado = []

	for i in data["data"]:
	       
	    df = pd.DataFrame.from_dict(i)
	    n = str(df.columns[0])
	    df = df.sort_values(n)


	    eixo_x = str(df.columns[0])
	    eixo_y = str(df.columns[1])

	    trace=go.Scatter(
	    x = df.loc[:,eixo_x],
	    y = df.loc[:,eixo_y],
	    mode='lines+markers',
	    xaxis='x2', yaxis='y2')
	    dado.append(trace)

	    if aux >= 1:
	        dfs_f = pd.merge(df, dfs, how='inner', on=eixo_x)
	           
	    dfs = df
	    aux = aux + 1
	    

	figure = ff.create_table(dfs_f)

	figure.add_traces(dado)

	# initialize xaxis2 and yaxis2
	figure['layout']['xaxis2'] = {}
	figure['layout']['yaxis2'] = {}

	# Edit layout for subplots
	figure.layout.xaxis.update({'domain': [0, .35]})
	figure.layout.xaxis2.update({'domain': [0.4, 1.]})

	figure.layout.margin.update({'t':50, 'b':70})
	figure.layout.update({'title': data["title"]})
	figure.layout.yaxis2.update({'anchor': 'x2'})
	figure.layout.xaxis2.update(dict(tickmode='linear'))
	figure.layout.update({'height':900})
	figure.layout.update({'width':1200})

	pio.write_image(figure, 'images/fig.png')



def id_3(data):
	aux = 0
	dado = []
	z = 0 

	for i in data["data"]:
	       
	    df = pd.DataFrame.from_dict(i)

	    eixo_x = str(df.columns[0])
	    eixo_y = str(df.columns[1])

	    trace=go.Scatter(
	    x = df.loc[:,eixo_x],
	    y = df.loc[:,eixo_y],
	    mode='lines+markers+text',
	    text=df.loc[:,eixo_y],
	    textposition='bottom center',
	    name = data['names'][z])
	    dado.append(trace)
	    z = z + 1

	layout = go.Layout(title=data['title'])

	figure = go.Figure(data=dado,layout=layout)
	pio.write_image(figure, 'images/fig.png')


def id_2(data):
	dado = []
	z = 0
	for i in data['data']:
	    df = pd.DataFrame.from_dict(i)
	    
	    eixo_x = str(df.columns[0])
	    eixo_y = str(df.columns[1])
	    
	    trace = go.Bar(
	        x=df.loc[:,eixo_x],
	        y=df.loc[:,eixo_y],
	        text=df.loc[:,eixo_y],
	        textposition = 'auto',
	        name = data['names'][z])
	    dado.append(trace)
	    z = z + 1
	    

	layout = go.Layout(
	    title=data['title']
	)

	figure = go.Figure(data=dado,layout=layout)
	pio.write_image(figure, 'images/fig.png')


def id_1(data):
	aux = 0
	dado = []

	for i in data['data']:
	    df = pd.DataFrame.from_dict(i)
	    
	    if aux > 1:
	        dfs_f = pd.merge(df, dfs, how='inner', on=eixo_x)
	           
	    dfs = df
	    aux = aux + 1
	    
	if aux == 2:
	        dfs_f = pd.merge(df, dfs, how='inner', on=eixo_x)
	        
	if aux == 1:
	        dfs_f = df   
    
	figure = ff.create_table(dfs_f,height_constant=10)
	figure.layout.width=350
	pio.write_image(figure, 'images/fig.png')


@app.route("/readme")
def main():
	return render_template('index.html')


@app.route("/img_post",methods=['POST'])
def MyDashApp():


	data = request.get_json()

	if data['id'] == 4:
		id_4(data)
		filename = 'images/fig.png'
		return send_file(filename, mimetype='image/png'),201

	if data['id'] == 3:
		id_3(data)
		filename = 'images/fig.png'
		return send_file(filename, mimetype='image/png'),201

	if data['id'] == 2:
		id_2(data)
		filename = 'images/fig.png'
		return send_file(filename, mimetype='image/png'),201	

	if data['id'] == 1:
		id_1(data)
		filename = 'images/fig.png'
		return send_file(filename, mimetype='image/png'),201


	else:
		return 'erro: not found ID', 404	



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=False)