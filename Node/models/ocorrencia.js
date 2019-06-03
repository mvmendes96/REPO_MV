const mongoose = require('mongoose');

const OcorrenciaSchema = new mongoose.Schema({
  tipo: {
    type: String,
    required: false
  },
  data: {
    type: String,
    required: false
  },
  local: {
    type: String,
    required: false
  },
  nome_policial: {
    type: String,
    required: false
  }
});

const Ocorrencia = mongoose.model('Ocorrencia', OcorrenciaSchema);

module.exports = Ocorrencia;
