<template>
  <main>
    <div class="container">
      <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
        <h2 class="mb-0">Estoque Regional de Fármacos</h2>
        <button class="btn btn-primary">
          <router-link class="dropdown-item" to="/regional/adicionar">Adicionar ao Estoque Regional</router-link>
        </button>
      </div>
      <p>Aqui você pode conferir os fármacos que compõem o estoque regional e registrar abastecimentos ou distribuições desse estoque.
        Quaisquer alertas de estoque baixo nos postos de distribuição nessa região serão mostrados aqui.</p>

      <div v-if="alerts.length" class="row">
        <div v-for="alert in alerts" :key="alert.id" class="col-12 col-md-4 mb-4">
          <LowStockAlert :alert="alert" />
        </div>
      </div>

      <RegionalStockTable />
    </div>
  </main>
</template>

<script>
import axios from 'axios';
import RegionalStockTable from '../components/RegionalStockTable.vue';
import LowStockAlert from '../components/LowStockAlert.vue';

export default {
  components: {
    RegionalStockTable,
    LowStockAlert
  },
  data() {
    return {
      alerts: []
    };
  },
  created() {
    this.fetchAlerts();
  },
  methods: {
    fetchAlerts() {
      axios.get('http://localhost:8000/estoque-regional/alerts/')
        .then(response => {
          this.alerts = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar alertas:', error);
        });
    }
  }
};
</script>