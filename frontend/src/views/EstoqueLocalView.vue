<template>
  <main>
    <div class="container">
      <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
        <h2 class="mb-0">Estoque Local de Fármacos</h2>
        <button class="btn btn-primary">
          <router-link class="dropdown-item" to="/local/adicionar">Adicionar ao Estoque Local</router-link>
        </button>
      </div>
      <p>Aqui você pode conferir os fármacos que compõem o estoque local, podendo visualizar todo o estoque ou filtrar por postos específicos.</p>
      <div class="mb-3">
        <input type="radio" id="todoEstoque" value="todo" v-model="estoqueType">
        <label class="px-2" for="todoEstoque">Todo o Estoque</label>
        <input type="radio" id="porPosto" value="posto" v-model="estoqueType">
        <label class="px-2" for="porPosto">Por Posto de Distribuição</label>
      </div>
      <div class="input-group mb-3 d-flex align-items-center" style="max-width: 600px;" v-if="estoqueType === 'posto'">
        <input class="form-control" type="text" v-model="cnes" placeholder="Digite o CNES do posto">
        <button type="button" class="btn btn-primary" @click="fetchPosto">Confirmar</button>
        <p class="ms-3 my-0" v-if="selectedPosto">Posto selecionado: {{ selectedPosto.nome }}</p>
      </div>
      <LocalStockTable :postoId="selectedPostoId" />
    </div>
  </main>
</template>

<script>
import LocalStockTable from '../components/LocalStockTable.vue';
import axios from 'axios';

export default {
  components: {
    LocalStockTable
  },
  data() {
    return {
      estoqueType: 'todo',
      cnes: '',
      selectedPosto: null,
      selectedPostoId: ''
    };
  },
  methods: {
    fetchPosto() {
      axios.get(`http://localhost:8000/api/postos-distribuicao/${this.cnes}/`)
        .then(response => {
          this.selectedPosto = response.data;
          this.selectedPostoId = response.data.cnes;
        })
        .catch(error => {
          console.error('Error fetching posto data: ', error);
          this.selectedPosto = null;
          this.selectedPostoId = '';
        });
    }
  },
  watch: {
    estoqueType(newVal) {
      if (newVal === 'todo') {
        this.selectedPosto = null;
        this.selectedPostoId = '';
      }
    }
  }
};
</script>