import Vue from 'vue'
import App from './App.vue'
import VueFormulate from '@braid/vue-formulate'
import VueToast from 'vue-toast-notification';
// Import one of the available themes
//import 'vue-toast-notification/dist/theme-default.css';
import 'vue-toast-notification/dist/theme-sugar.css';
import { library } from '@fortawesome/fontawesome-svg-core'
/* import specific icons */
import { faPencilSquare, faTrash } from '@fortawesome/free-solid-svg-icons'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* add icons to the library */
library.add(faPencilSquare)
library.add(faTrash)

/* add font awesome icon component */
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueToast);
Vue.use(VueFormulate)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
