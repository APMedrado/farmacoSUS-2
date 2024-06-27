<template>
  <main>
    <div class="container">
      <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
        <h2 class="mb-0">Histórico de Registros de Entrega</h2>
        <button class="btn btn-primary me-md-3">
          <router-link class="dropdown-item" to="/registros-entrega/novo">Nova Entrega</router-link>
        </button>
      </div>
      <p>Aqui você pode conferir o histórico de registros de entrega no sistema.</p>
      <DeliveryRecordsTable />
    </div>
  </main>
</template>

<script>
import DeliveryRecordsTable from '../components/DeliveryRecordsTable.vue';

export default {
  components: {
    DeliveryRecordsTable
  }
};
</script>  