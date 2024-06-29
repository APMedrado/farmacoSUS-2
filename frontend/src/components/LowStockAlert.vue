<template>
  <div :class="['alert', alertClass]" role="alert">
    <h5 class="alert-heading">Alerta de Estoque Baixo</h5>
    <p><strong>Posto:</strong> {{ alert.posto_distribuicao.nome }}</p>
    <p><strong>Fármaco:</strong> {{ alert.medicamento.produto }}</p>
    <p><strong>Estoque:</strong> {{ translatedStatus }} ({{ alert.quantidade }})</p>
  </div>
</template>

<script>
export default {
  name: 'LowStockAlert',
  props: {
    alert: {
      type: Object,
      required: true
    }
  },
  computed: {
    alertClass() {
      if (['critical', 'out of stock'].includes(this.alert.status)) {
        return 'alert-danger';
      } else {
        return 'alert-warning';
      }
    },
    translatedStatus() {
      const statusMap = {
        'attention': 'Atenção',
        'low': 'Baixo',
        'critical': 'Crítico',
        'out of stock': 'Fora de Estoque'
      };
      return statusMap[this.alert.status];
    }
  }
};
</script>

<style scoped>
.alert {
  margin-bottom: 20px;
}
</style>