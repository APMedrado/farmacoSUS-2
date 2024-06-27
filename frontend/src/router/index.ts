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
import ListarPacientesView from '@/views/ListarPacientesView.vue'
import NovoPacienteView from '@/views/NovoPacienteView.vue'
import ListarMedicosView from '@/views/ListarMedicosView.vue'
import NovoMedicoView from '@/views/NovoMedicoView.vue'
import ListarEntregasView from '@/views/ListarEntregasView.vue'

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
      path: '/pacientes',
      name: 'listar-pacientes',
      component: ListarPacientesView
    },
    {
      path: '/pacientes/novo',
      name: 'novo-paciente',
      component: NovoPacienteView
    },
    {
      path: '/medicos',
      name: 'listar-medicos',
      component: ListarMedicosView
    },
    {
      path: '/medicos/novo',
      name: 'novo-medico',
      component: NovoMedicoView
    },
    {
      path: '/registros-entrega',
      name: 'listar-registros-entrega',
      component: ListarEntregasView
    },
    {
      path: '/registros-entrega/novo',
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