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
        <div v-for="alert in sortedAlerts" :key="alert.id" class="col-12 col-md-4 mb-4">
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
    this.startPolling();
  },
  beforeDestroy() {
    this.stopPolling();
  },
  computed: {
    sortedAlerts() {
      return this.alerts.sort((a, b) => {
        const statusOrder = {
          'out of stock': 1,
          'critical': 2,
          'low': 3,
          'attention': 4
        };

        const statusComparison = statusOrder[a.status] - statusOrder[b.status];
        if (statusComparison !== 0) {
          return statusComparison;
        }

        const timestampA = new Date(a.timestamp);
        const timestampB = new Date(b.timestamp);
        return timestampB - timestampA;
      });
    }
  },
  methods: {
    fetchAlerts() {
      axios.get('http://andromeda.lasdpc.icmc.usp.br:5025/api/estoque-regional/alerts/')
        .then(response => {
          this.alerts = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar alertas:', error);
        });
    },
    startPolling() {
      this.polling = setInterval(this.fetchAlerts, 10000); // Checa a cada 10 segundos
    },
    stopPolling() {
      clearInterval(this.polling);
    }
  }
};
</script>