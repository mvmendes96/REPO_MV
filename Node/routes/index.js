const express = require('express');
const router = express.Router();
const { ensureAuthenticated, forwardAuthenticated } = require('../config/auth');
// Load Ocorrencia model
const Ocorrencia = require('../models/ocorrencia');

// Welcome Page
router.get('/', forwardAuthenticated, (req, res) => res.render('welcome'));

// Dashboard
router.get('/dashboard', ensureAuthenticated, (req, res) =>
  res.render('dashboard', {
    user: req.user
  })
);


router.get('/registrar_ocorrencia', ensureAuthenticated, (req, res) =>
  res.render('registrar_ocorrencia', {
    user: req.user
  })
);


router.post('/registrar_ocorrencia', (req, res) => {
  const { tipo, data, local, nome_policial } = req.body;
  let errors = [];

	  if (!tipo || !data || !local || !nome_policial) {
	    errors.push({ msg: 'Please enter all fields' });
	  }

	  
	  if (errors.length > 0) {
	    res.render('registrar_ocorrencia', {
	      errors,
	      tipo,
	      data,
	      local,
	      nome_policial
	    });
	  } 
  const newOcorrencia = new Ocorrencia({
  	tipo,
  	data,
  	local,
  	nome_policial
  });
  newOcorrencia
  .save()
  res.redirect('/dashboard');

});


// router.get('/consultar_ocorrencia', ensureAuthenticated, (req, res) =>
//   res.render('consultar_ocorrencia', {
//     Ocorrencia: req.Ocorrencia
//   })
// );


router.get('/consultar_ocorrencia', function(req, res) {
   Ocorrencia.find({}, function(error, ocorrs) {
	if(error) {
  	   res.json({error: 'Nao foi possivel retornar dados'});
  	} else {
	  
	   res.json({Registrados: ocorrs});
		
	}
   });
});

// // Registro de Ocoorencia
// router.post('/registrar_ocorrencia', (req, res) => {
//  passport.authenticate('local', {
//     successRedirect: '/dashboard',
//     failureRedirect: '/users/login',
//     failureFlash: true
//   })(req, res, next);
// });


module.exports = router;
