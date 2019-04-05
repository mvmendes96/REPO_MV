

function Login()
{	
	var usuario = document.getElementById("user").value
	var senha = document.getElementById("senha").value
	if((usuario == "master@teste.com"&& senha == "abcd1234"))
	{
		Acesso()
		alert("Senha Correta")
		window.location="base"
	}
	else
		alert("Usuario ou Senha invalido")
	
}

function Acesso()
{try{
	var theUrl= "http://httpbin.org/ip"; 
	var xmlHttp= new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false ); 
	xmlHttp.send( null);alert(xmlHttp.responseText);
} catch (e) {
	alert(e);}}

function Cadastrar()
{
	var email = document.getElementById("mail").value
	if (email.indexOf("@") >= 0)
		alert("Email tem @")
	else
		alert("Email nao tem @")
	var senhaCad = document.getElementById("senha").value
	var regex = /^(?=(?:.*?[A-Z]){1})(?=(?:.*?[0-9]){1})/

	if(senhaCad.length < 8)
	{
	    alert("A senha deve conter no minímo 6 digitos!")
	   
	    return false;
	}
	else if(!regex.exec(senhaCad))
	{
	    alert("A senha deve conter no mínimo 1 letra e 1 número")
	}
}


