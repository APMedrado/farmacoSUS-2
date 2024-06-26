<template>
  <main>
    <div class="container mt-5">
      <h2>Cadastro de Fármacos em Massa</h2>
      <p>Envie um arquivo JSON corretamente formatado para cadastrar múltiplos fármacos de uma vez.</p>
      <form @submit.prevent="handleSubmit">
        <div class="mb-3">
          <label for="farmacos-json" class="form-label">JSON com Fármacos</label>
          <input type="file" class="form-control" id="farmacos-json" @change="handleFileUpload" required>
        </div>
        <button type="submit" class="btn btn-primary">Salvar</button>
      </form>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      farmacosJson: null
    };
  },
  methods: {
    handleFileUpload(event) {
      const fileReader = new FileReader();
      fileReader.readAsText(event.target.files[0]);
      fileReader.onload = () => {
        try {
          this.farmacosJson = JSON.parse(fileReader.result);
        } catch (error) {
          alert('Erro na leitura do arquivo JSON: ' + error.message);
          this.farmacosJson = null;
        }
      };
    },
    handleSubmit() {
      if (!this.farmacosJson) {
        alert('Por favor, carregue um arquivo JSON válido.');
        return;
      }
      axios.post('http://localhost:8000/api/farmacos/batch/', this.farmacosJson)
        .then(response => {
          alert('Fármacos cadastrados com sucesso!');
        })
        .catch(error => {
          alert('Erro ao cadastrar fármacos: ' + error.message);
        });
    }
  }
};
</script>
  
<style scoped>
.container {
  max-width: 600px;
}
</style>
