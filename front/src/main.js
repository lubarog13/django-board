import Vue from 'vue'
import App from './App.vue'
import VueFormulate from '@braid/vue-formulate'
import VueToast from 'vue-toast-notification';
// Import one of the available themes
//import 'vue-toast-notification/dist/theme-default.css';
import 'vue-toast-notification/dist/theme-sugar.css';

Vue.use(VueToast);
Vue.use(VueFormulate)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
