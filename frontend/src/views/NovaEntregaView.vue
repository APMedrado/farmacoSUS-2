<template>
    <div class="container mt-5">
      <h2>Registrar Nova Entrega</h2>
      <form @submit.prevent="handleSubmit">
        <!-- Posto de Distribuição com Pesquisa de CNES -->
        <div class="mb-3 position-relative">
          <label for="postoDistribuicao" class="form-label">Posto de Distribuição (CNES)</label>
          <div class="input-group">
            <input type="text" class="form-control" id="postoDistribuicao" v-model="postoDistribuicaoSearch" placeholder="Digite o CNES">
            <button type="button" class="btn btn-primary" @click="searchPostoDistribuicao">Pesquisar</button>
          </div>
          <p v-if="postoDistribuicaoSearchResult" class="mt-2">{{ postoDistribuicaoSearchResult }}</p>
          <div v-if="form.postoDistribuicao" class="mt-2">
            <strong>Posto Selecionado:</strong><br>
            CNES: {{ form.postoDistribuicao.cnes }}<br>
            Nome: {{ form.postoDistribuicao.nome }}<br>
            Endereço: {{ form.postoDistribuicao.endereco }}<br>
            Bairro: {{ form.postoDistribuicao.bairro }}<br>
            Município: {{ form.postoDistribuicao.municipio }}
          </div>
        </div>

  
        <!-- Beneficiário com Pesquisa de CPF -->
        <div class="mb-3 position-relative">
          <label for="beneficiario" class="form-label">Beneficiário (CPF)</label>
          <div class="input-group">
            <input type="text" class="form-control" id="beneficiario" v-model="beneficiarioSearch" @input="formatCpf" placeholder="Digite o CPF">
            <button type="button" class="btn btn-primary" @click="searchBeneficiario">Pesquisar</button>
          </div>
          <p v-if="beneficiarioSearchResult" class="mt-2">{{ beneficiarioSearchResult }}</p>
          <p v-if="beneficiarioInfo" class="mt-2">
            Nome: {{ beneficiarioInfo.nome }}<br>
            Data de Nascimento: {{ beneficiarioInfo.dataNascimento }}<br>
            Bolsa Família: {{ beneficiarioInfo.bolsaFamilia || 'N/A' }}<br>
            Cadastro Único: {{ beneficiarioInfo.cadastroUnico || 'N/A' }}
          </p>
        </div>
  
        <!-- Médico com Pesquisa de CRM -->
        <div class="mb-3 position-relative">
          <label for="medico" class="form-label">Médico (CRM)</label>
          <div class="input-group">
            <input type="text" class="form-control" id="medico" v-model="medicoSearch" placeholder="Digite o CRM">
            <button type="button" class="btn btn-primary" @click="searchMedico">Pesquisar</button>
          </div>
          <p v-if="medicoSearchResult" class="mt-2">{{ medicoSearchResult }}</p>
          <p v-if="medicoInfo" class="mt-2">
            Nome: {{ medicoInfo.nome }}<br>
            Especialidade: {{ medicoInfo.especialidade }}<br>
            Situação: {{ medicoInfo.situacao }}
          </p>
        </div>
  
        <!-- Medicamento(s) com Pesquisa de Código de Barras -->
        <div class="mb-3 position-relative">
        <label for="medicamento" class="form-label">Medicamento (Código de Barras)</label>
        <div class="input-group">
            <input type="text" class="form-control" id="medicamento" v-model="medicamentoSearch" placeholder="Digite o Código de Barras">
            <button type="button" class="btn btn-primary" @click="searchMedicamento">Pesquisar</button>
        </div>
        <p v-if="medicamentoSearchResult" class="mt-2">{{ medicamentoSearchResult }}</p>
        </div>
  
        <!-- Lista de Medicamentos Selecionados -->
        <div class="mb-3" v-if="form.medicamentos.length">
            <label class="form-label">Medicamentos Selecionados</label>
            <ul class="list-group">
                <li v-for="(medicamento, index) in form.medicamentos" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
                {{ medicamento.nome }} ({{ medicamento.quantidade }})
                <div>
                    <input type="number" class="form-control d-inline-block me-2" v-model.number="medicamento.quantidade" min="1" style="width: 80px;">
                    <button type="button" class="btn btn-danger btn-sm" @click="removeMedicamento(index)">Remover</button>
                </div>
                </li>
            </ul>
        </div>
  
        <!-- Data da Receita -->
        <div class="mb-3">
          <label for="dataReceita" class="form-label">Data da Receita</label>
          <input type="date" class="form-control" id="dataReceita" v-model="form.dataReceita">
        </div>
  
        <!-- Data da Entrega -->
        <div class="mb-3">
          <label for="dataEntrega" class="form-label">Data da Entrega</label>
          <input type="date" class="form-control" id="dataEntrega" v-model="form.dataEntrega">
        </div>
  
        <button type="submit" class="btn btn-primary">Registrar Entrega</button>
      </form>
    </div>
  </template>
  
<script>
export default {
  data() {
    return {
      beneficiarioSearch: '',
      beneficiarioSearchResult: '',
      beneficiarioInfo: null,
      postoDistribuicaoSearch: '',
      postoDistribuicaoSearchResult: '',
      medicoSearch: '',
      medicoSearchResult: '',
      medicoInfo: null,
      medicamentoSearch: '',
      medicamentoSearchResult: '',
      form: {
        medicamentos: [],
        beneficiario: '',
        medico: '',
        dataReceita: '',
        postoDistribuicao: null,
        dataEntrega: this.getCurrentDate() // Pré-preencher com a data atual
      },
      beneficiariosDisponiveis: [
        { cpf: '12345678900', nome: 'João da Silva', dataNascimento: '1980-01-01', bolsaFamilia: '123456', cadastroUnico: '654321' },
        { cpf: '98765432100', nome: 'Maria de Souza', dataNascimento: '1975-05-15' }
      ],
      postosDistribuicaoDisponiveis: [
        { cnes: '1234567', nome: 'Posto Central', endereco: 'Rua Central, 123', bairro: 'Centro', municipio: 'Cidade A' },
        { cnes: '2345678', nome: 'Posto Norte', endereco: 'Rua Norte, 456', bairro: 'Norte', municipio: 'Cidade B' },
        { cnes: '3456789', nome: 'Posto Sul', endereco: 'Rua Sul, 789', bairro: 'Sul', municipio: 'Cidade C' }
      ],
      medicosDisponiveis: [
        { crm: '12345', nome: 'Dr. Carlos', especialidade: 'Cardiologia', situacao: 'Ativo' },
        { crm: '67890', nome: 'Dra. Ana', especialidade: 'Pediatria', situacao: 'Inativo' }
      ],
      medicamentosPorPosto: {
        '1234567': [
          { codigoBarras: '7891234567890', nome: 'Paracetamol', quantidade: 100 },
          { codigoBarras: '7891234567891', nome: 'Ibuprofeno', quantidade: 50 },
          { codigoBarras: '7891234567892', nome: 'Dipirona', quantidade: 75 }
        ],
        '2345678': [
          { codigoBarras: '7891234567890', nome: 'Paracetamol', quantidade: 80 },
          { codigoBarras: '7891234567893', nome: 'Amoxicilina', quantidade: 60 },
          { codigoBarras: '7891234567894', nome: 'Omeprazol', quantidade: 90 }
        ],
        '3456789': [
          { codigoBarras: '7891234567891', nome: 'Ibuprofeno', quantidade: 40 },
          { codigoBarras: '7891234567892', nome: 'Dipirona', quantidade: 65 },
          { codigoBarras: '7891234567894', nome: 'Omeprazol', quantidade: 70 }
        ]
      }
    };
  },
  methods: {
    getCurrentDate() {
      const today = new Date();
      const day = String(today.getDate()).padStart(2, '0');
      const month = String(today.getMonth() + 1).padStart(2, '0');
      const year = today.getFullYear();
      return `${year}-${month}-${day}`;
    },
    formatCpf() {
      let cpf = this.beneficiarioSearch.replace(/\D/g, '');
      cpf = cpf.slice(0, 11);
      const formattedCpf = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
      this.beneficiarioSearch = formattedCpf;
    },
    searchBeneficiario() {
      const cpfUnformatted = this.beneficiarioSearch.replace(/\D/g, '');
      const found = this.beneficiariosDisponiveis.find(beneficiario => beneficiario.cpf === cpfUnformatted);
      if (found) {
        this.beneficiarioInfo = found;
        this.form.beneficiario = cpfUnformatted;
        this.beneficiarioSearchResult = '';
      } else {
        this.beneficiarioInfo = null;
        this.beneficiarioSearchResult = 'Beneficiário não encontrado';
      }
    },
    searchPostoDistribuicao() {
      const found = this.postosDistribuicaoDisponiveis.find(posto => posto.cnes === this.postoDistribuicaoSearch);
      if (found) {
        this.form.postoDistribuicao = found;
        this.postoDistribuicaoSearchResult = '';
        this.form.medicamentos = []; // Resetar lista de medicamentos ao selecionar novo posto
      } else {
        this.form.postoDistribuicao = null;
        this.postoDistribuicaoSearchResult = 'Posto de distribuição não encontrado';
      }
    },
    searchMedico() {
      // Fazendo a requisição GET para buscar o médico pelo CRM
      axios.get(`http://localhost:8000/api/medicos/?crm=${this.medicoSearch}`)
        .then(response => {
      if (response.data) {
        if (response.data.situacao === 'Ativo') {
          this.medicoInfo = response.data;
          this.form.medico = this.medicoSearch;
          this.medicoSearchResult = '';
        } else {
          this.medicoInfo = null;
          this.medicoSearchResult = 'Médico inativo';
        }
      } else {
        this.medicoInfo = null;
        this.medicoSearchResult = 'Médico não encontrado';
      }
      })
      .catch(error => {
        console.error('Erro ao buscar médico: ', error);
        this.medicoInfo = null;
        this.medicoSearchResult = 'Erro ao buscar médico';
      });
    },
    searchMedicamento() {
      if (!this.form.postoDistribuicao || !this.form.postoDistribuicao.cnes) {
        this.medicamentoSearchResult = 'Por favor, selecione um posto de distribuição válido primeiro';
        return;
      }
      const found = (this.medicamentosPorPosto[this.form.postoDistribuicao.cnes] || []).find(medicamento => medicamento.codigoBarras === this.medicamentoSearch);
      if (found) {
        this.addMedicamento(found);
        this.medicamentoSearchResult = '';
      } else {
        this.medicamentoSearchResult = 'Medicamento não encontrado ou fora de estoque';
      }
    },
    addMedicamento(medicamento) {
      if (medicamento && !this.form.medicamentos.some(m => m.codigoBarras === medicamento.codigoBarras)) {
        this.form.medicamentos.push({ nome: medicamento.nome, codigoBarras: medicamento.codigoBarras, quantidade: 1 });
        this.medicamentoSearch = '';
      }
    },
    removeMedicamento(index) {
      this.form.medicamentos.splice(index, 1);
    },
    handleSubmit() {
      // Cria um objeto FormData para enviar os dados
      const formData = new FormData();
      formData.append('medicamentos', JSON.stringify(this.form.medicamentos));
      formData.append('beneficiario', this.form.beneficiario);
      formData.append('medico', this.form.medico);
      if (this.form.dataReceita) formData.append('dataReceita', this.form.dataReceita);
      formData.append('postoDistribuicao', this.form.postoDistribuicao.nome);
      if (this.form.dataEntrega) formData.append('dataEntrega', this.form.dataEntrega);

      // Aqui você pode adicionar a lógica para enviar o FormData para um servidor via AJAX.
      console.log('Form data:', formData);
      // Limpar o formulário após o envio
      this.form = {
        medicamentos: [],
        beneficiario: '',
        medico: '',
        dataReceita: '',
        postoDistribuicao: null,
        dataEntrega: this.getCurrentDate()  // Redefine com a data atual
      };
      this.beneficiarioSearch = '';
      this.beneficiarioSearchResult = '';
      this.beneficiarioInfo = null;
      this.postoDistribuicaoSearch = '';
      this.postoDistribuicaoSearchResult = '';
      this.medicoSearch = '';
      this.medicoSearchResult = '';
      this.medicoInfo = null;
      this.medicamentoSearch = '';
      this.medicamentoSearchResult = '';
      alert('Entrega registrada com sucesso!');
    }
  }
};
</script>

  
  <style scoped>
  .container {
    max-width: 600px;
  }
  .dropdown-menu.show {
    display: block;
    max-height: 150px;
    overflow-y: auto;
  }
  </style>
  