// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import weui from 'weui'
import axios from 'axios'

// 引入并注册 vue-svg-icon
import Icon from 'vue-svg-icon/Icon.vue';
Vue.component('icon', Icon);  


// 引入Vuex
import Vuex from 'vuex'  // 引入Vuex 第1步
Vue.use(Vuex)  // 引入Vuex 第2步

const store = new Vuex.Store({
    state:{
        http : 'http://0.0.0.0:5000/API/',
        content_list:{},
        content_current:{},
        msg_toast:'',
        user:{},
    },
    mutations:{    // 全部操作交由store自身mutations内的方法来执行
        init:function (state,content_list) {
            // 初始化所有content_list到store中
            // 并转换为key为content_id value为content的字典列表
            for (var i = content_list.length - 1; i >= 0; i--) {
                state.content_list[content_list[i].content_id] = content_list[i];
            }
            // console.log('state.content_list',state.content_list)
        },
        content:function (state,content_id) {
            // body...
            // state.content_current = content_id;
            var data = state.content_list[content_id];
            state.content_current = data;
            // state.content_current = JSON.stringify(data);
            // console.log('state.content_current',typeof(state.content_current),state.content_current);
        },
        login (state,data) {
            // body...
            state.user = data;
            console.log('state.user',typeof(state.user),state.user);
        },
        logout (state,data) {
            // body...
            state.user = '';
            window.localStorage.removeItem("user");
            console.log('logout > state.user',typeof(state.user),state.user);
        },
        msg_toast(state,msg){
            setTimeout(()=>{
                state.msg_toast = msg;
            },300)
            setTimeout(()=>{
                state.msg_toast = "";
            },2000)
        },
        echo_list(state,data){
            state.echo_list = data;
        },
    }
})



Vue.config.productionTip = false



/* eslint-disable no-new */
new Vue({
el: '#app',
    router,
    store,
    data(){
        return {
            msg: 'Welcome to Your Vue.js App',
            // http : 'http://0.0.0.0:5000/',
        }
    },
    // props:{
    //     http : 'http://0.0.0.0:5000/',
    // },
    components: { 
        App,
    },
    template: '<App/>'
})



