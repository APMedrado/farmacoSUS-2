<template>
  <div :class="['alert', alertClass]" role="alert">
    <h5 class="alert-heading">Alerta de Estoque Baixo</h5>
    <p><strong>Posto:</strong> {{ alert.posto_distribuicao.nome }}</p>
    <p><strong>Fármaco:</strong> {{ alert.medicamento.produto }}</p>
    <p><strong>Estoque:</strong> {{ translatedStatus }} ({{ alert.quantidade }})</p>
    
    <div class="form-group">
      <label for="quantidade">Quantidade a enviar:</label>
      <input type="number" class="form-control" v-model="quantidade" min="1" />
    </div>
    <button class="btn btn-primary mt-2" @click="enviarAbastecimento">Enviar Abastecimento</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LowStockAlert',
  props: {
    alert: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      quantidade: 1
    };
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
  },
  methods: {
    enviarAbastecimento() {
      const data = {
        medicamento_codigo: this.alert.medicamento.codigo_barra,
        posto_cnes: this.alert.posto_distribuicao.cnes,
        quantidade: this.quantidade
      };
      axios.post('http://localhost:8000/estoque-local/enviar-abastecimento/', data)
        .then(response => {
          alert('Abastecimento enviado com sucesso!');
        })
        .catch(error => {
          console.error('Erro ao enviar abastecimento:', error);
          alert('Erro ao enviar abastecimento');
        });
    }
  }
};
</script>