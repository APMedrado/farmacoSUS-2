import { createRouter, createWebHistory } from 'vue-router'
import PageNotFoundView from '@/views/PageNotFoundView.vue'
import ListarFarmacosView from '@/views/ListarFarmacosView.vue'
import EstoqueLocalView from '@/views/EstoqueLocalView.vue'
import AddFarmacoLocalView from '@/views/AddFarmacoLocalView.vue'
import EstoqueRegionalView from '@/views/EstoqueRegionalView.vue'
import AddFarmacoRegionalView from '@/views/AddFarmacoRegionalView.vue'
import NovoFarmacoView from '@/views/NovoFarmacoView.vue'
import NovaEntregaView from '@/views/NovaEntregaView.vue'
import FarmacoBatchInput from '@/views/FarmacoBatchInput.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/local',
      name: 'estoque-local',
      component: EstoqueLocalView
    },
    {
      path: '/local/adicionar',
      name: 'estoque-local-adicionar',
      component: AddFarmacoLocalView
    },
    {
      path: '/regional',
      name: 'estoque-regional',
      component: EstoqueRegionalView
    },
    {
      path: '/regional/adicionar',
      name: 'estoque-regional-adicionar',
      component: AddFarmacoRegionalView
    },
    {
      path: '/farmacos',
      name: 'listar-farmacos',
      component: ListarFarmacosView
    },
    {
      path: '/farmacos/novo',
      name: 'novo-farmaco',
      component: NovoFarmacoView
    },
    {
      path: '/farmacos/batch',
      name: 'farmaco-batch-input',
      component: FarmacoBatchInput
    },
    {
      path: '/entrega',
      name: 'nova-entrega',
      component: NovaEntregaView
    },
    { path: '/home', redirect: '/local' },
    { path: '/', redirect: '/local' },
    {
      path: '/:catchall(.*)*',
      name: 'PageNotFound',
      component: PageNotFoundView,
    },
  ]
})

export default router
