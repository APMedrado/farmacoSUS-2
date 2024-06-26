<template>
  <main>
    <div class="container">
      <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
        <h2 class="mb-0">Fármacos Cadastrados no Sistema</h2>
        <button class="btn btn-primary">
          <router-link class="dropdown-item" to="/farmacos/novo">Novo Fármaco</router-link>
        </button>
      </div>
      <p>Aqui você pode conferir e editar os fármacos cadastrados no sistema, ou deletar um fármaco.</p>
      <FarmacoTableComponent />
    </div>
  </main>
</template>

<script>
import FarmacoTableComponent from '../components/FarmacoTableComponent.vue';

export default {
  components: {
    FarmacoTableComponent
  }
};
</script>
