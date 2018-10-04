// import * from

// const Index = { 
//     template: `
//         <div yd-flexbox direction="vertical" align="center">
//             <br>
//             <record-play></record-play>
//             <br>
//             <record-button></record-button>
//             <br>
//             <grids></grids>
//             <br>
//         </div>`
//  }
// const Login = { template: '<div>Login</div>' }
// const Foo = { template: '<div>foo</div>' }
// const Bar = { template: '<div>bar</div>' }

// const routes = [
//   { path: '/', component: Index },
//   { path: '/login', component: Login },
//   { path: '/foo', component: Foo },
//   { path: '/bar', component: Bar },
// ]





















// 定义一个名为 button-counter 的新组件

// Vue.component('', {
//   template: ``
// })
// Vue.component('navbar', {
//   template: `
//     <yd-navbar slot="center" title="Nut Echo">
//         <router-link to="/" slot="left">
//             <yd-icon name="qrscan" size="25px" color="#777"></yd-icon>
//         </router-link>
//         <router-link to="/login" slot="right">
//             <yd-icon name="ucenter-outline" size="25px" color="#777"></yd-icon>
//         </router-link>
//         <router-link to="/foo" slot="right">
//             <yd-icon name="ucenter-outline" size="25px" color="#777"></yd-icon>
//         </router-link>
//         <router-link to="/bar" slot="right">
//             <yd-icon name="ucenter-outline" size="25px" color="#777"></yd-icon>
//         </router-link>
//     </yd-navbar>
//     `
// })
// Vue.component('record-play', {
//   template: `
//     <yd-flexbox>
//         <yd-flexbox-item direction="vertical">
//             <audio src="" controls autoplay id="player">
//             </audio>
//         </yd-flexbox-item>
//     </yd-flexbox>
//     `
// })
// Vue.component('record-button', {
//   template: `
//     <yd-flexbox>
//         <yd-flexbox-item>
//             <yd-button onclick="audio_start()" type="primary">Start Recard</yd-button>
//             <yd-button onclick="audio_stop()" type="danger">Send Record</yd-button>
//         </yd-flexbox-item>
//     </yd-flexbox>
//     </div>
//     `,
// })
// Vue.component('tabbar', {
//   template: `
//   <yd-tabbar slot="tabbar" fixed="true">
//     <yd-tabbar-item title="Discover" link="#" active>
//         <yd-icon name="discover" slot="icon"></yd-icon>
//     </yd-tabbar-item>
//     <yd-tabbar-item title="购物车" link="#">
//         <yd-icon name="shopcart-outline" slot="icon"></yd-icon>
//     </yd-tabbar-item>
//     <yd-tabbar-item v-on:click="say('hi')" title="个人中心" link="#">
//         <yd-icon name="ucenter-outline" slot="icon"></yd-icon>
//     </yd-tabbar-item>
// </yd-tabbar>
// `
// })



// Vue.component('grids', {
//   template: `
//     <yd-grids-group :rows="3">
//         <yd-grids-item v-for="n in 1">
//             <span slot="text">
//             </span>
//         </yd-grids-item>
//         <yd-grids-item v-for="n in 1">
//             <span slot="text">
//             开机
//                 <yd-button size="large" type="primary">
//                     <yd-icon name="checkoff"></yd-icon>
//                     Start
//                 </yd-button>
//             </span>
//         </yd-grids-item>
//     </yd-grids-group>
//     `
// })



import Vue from '/static/js/vue.main.js'
import Router from '/static/js/vue-router.js'

import Login from '/static/router/login.js'
// import Navbar from '/static/router/navbar.js'


Vue.use(Router)


export default new VueRouter({
export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'index',
    //   component: Index
    // },
    { path: '/login', component: Login },
    // { path: '/foo', component: Foo },
    // { path: '/bar', component: Bar },
    // {
    //   path: '/course',
    //   name: 'course',
    //   component: Course
    // },
  ],
  mode: "history"
})