import Vue from 'vue'
import Router from 'vue-router'
import aTodo from '@/components/aTodo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'aTodo',
      component: aTodo
    }
  ]
})
