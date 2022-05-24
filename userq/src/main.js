// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false
import echarts from 'echarts'  //引入echarts

Vue.prototype.$echarts = echarts  //注册组件
import ElementUi from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'	
Vue.use(ElementUi)


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
