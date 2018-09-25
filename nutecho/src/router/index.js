import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Echo from '@/components/echo'
import content_list from '@/components/content_list'
import current_content from '@/components/content'


Vue.use(Router)

export default new Router({
    mode: 'history',    // 使用history模式 vue路径中去除#
    routes: [
        {
          path: '/',
          name: 'HelloWorld',
          component: HelloWorld
        },
        {
          path: '/echo',
          name: 'Echo',
          component: Echo
        },
        {
          path: '/login',
          name: 'Login',
          component: Login
        },
        {
          path: '/content_list',
          name: 'content_list',
          component: content_list
        },
        {
          path: '/content_current',
          name: 'content_current',
          component: current_content
        },

    ]
})
