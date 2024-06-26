<template>
  <main>
    <div class="container">
      <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
        <h2 class="mb-0">Estoque Regional de Fármacos</h2>
        <button class="btn btn-primary">
          <router-link class="dropdown-item" to="/regional/adicionar">Adicionar ao Estoque Regional</router-link>
        </button>
      </div>
      <p>Aqui você pode conferir os fármacos que compõem o estoque regional e registrar abastecimentos ou distribuições desse estoque.</p>
      <RegionalStockTable />
    </div>
  </main>
</template>

<script>
import RegionalStockTable from '../components/RegionalStockTable.vue';

export default {
  components: {
    RegionalStockTable
  }
};
</script>
