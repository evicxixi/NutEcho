import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Echo from '@/components/echo'
import content_list from '@/components/content_list'
import current_content from '@/components/content'
import person from '@/components/person'
import signin from '@/components/signin'
import login from '@/components/login'
import echo_add from '@/components/echo_add'



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
          path: '/content_list',
          name: 'content_list',
          component: content_list
        },
        {
          path: '/content_current',
          name: 'content_current',
          component: current_content
        },
        {
          path: '/person',
          name: 'person',
          component: person
        },
        {
          path: '/signin',
          name: 'signin',
          component: signin
        },
        {
          path: '/login',
          name: 'login',
          component: login
        },
        {
          path: '/echo_add',
          name: 'echo_add',
          component: echo_add
        },
    ]
})
