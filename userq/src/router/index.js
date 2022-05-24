import Vue from 'vue'
import Router from 'vue-router'
import main from '@/components/main/main'
import index from '@/components/main/index'
import echarts from '@/components/tu/echarts'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '主页面',
      component: main,
      children:[
                {
                  path: '/index',
                name: 'index',
                component: index,
              },
              {
                path: '/echarts',
              name: 'zhexiantu',
              component: echarts,
            }
           ]
    },
    
  ]
})
