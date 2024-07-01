<template>
  <main>
    <div class="container mt-5">
      <h2>Cadastro de Novo Paciente</h2>
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <label for="cpf" class="form-label">CPF</label>
          <input type="text" class="form-control" id="cpf" v-model="cpf" @input="formatCpf" required>
        </div>
        <div class="mb-3">
          <label for="nome" class="form-label">Nome</label>
          <input type="text" class="form-control" id="nome" v-model="nome" required>
        </div>
        <div class="mb-3">
          <label for="dataNascimento" class="form-label">Data de Nascimento</label>
          <input type="date" class="form-control" id="dataNascimento" v-model="dataNascimento" required>
        </div>
        <div class="mb-3">
          <label for="bolsaFamilia" class="form-label">Bolsa Família</label>
          <input type="text" class="form-control" id="bolsaFamilia" v-model="bolsaFamilia" required>
        </div>
        <div class="mb-3">
          <label for="cadastroUnico" class="form-label">Cadastro Único</label>
          <input type="text" class="form-control" id="cadastroUnico" v-model="cadastroUnico" required>
        </div>
        <button type="submit" class="btn btn-primary" :disabled="!isFormValid">Salvar</button>
      </form>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cpf: '',
      nome: '',
      dataNascimento: '',
      bolsaFamilia: '',
      cadastroUnico: ''
    };
  },
  computed: {
    isFormValid() {
      return this.isValidCpf(this.cpf) && this.nome && this.dataNascimento && this.bolsaFamilia && this.cadastroUnico;
    }
  },
  methods: {
    formatCpf() {
      let cpf = this.cpf.replace(/\D/g, '');
      cpf = cpf.slice(0, 11);
      const formattedCpf = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
      this.cpf = formattedCpf;
    },
    isValidCpf(cpf) {
      const regex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
      return regex.test(cpf);
    },
    async submitForm() {
      if (!this.isValidCpf(this.cpf)) {
        alert('CPF inválido. Por favor, insira um CPF no formato XXX.XXX.XXX-XX.');
        return;
      }

      const novoPaciente = {
        cpf: this.cpf.replace(/\D/g, ''), // Remove formatação antes de enviar
        nome: this.nome,
        data_nascimento: this.dataNascimento,
        bolsa_familia: this.bolsaFamilia,
        cadastro_unico: this.cadastroUnico
      };

      try {
        const response = await axios.post('http://andromeda.lasdpc.icmc.usp.br:5025/api/pacientes/', novoPaciente);
        console.log(response.data);
        alert('Paciente adicionado com sucesso!');
      } catch (error) {
        console.error(error);
        alert('Erro ao adicionar paciente.');
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>