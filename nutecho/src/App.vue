<template>
  <div id="app">
    <nut_head/>
    <!-- <search/> -->
    <!-- <router-view/> -->
    <tapbar/>
    <foot/>
  </div>
</template>

<script>
import '@/css/main.css'
import record from '@/js/record.js'
import weui from '@/js/weui.js'
import nut_head from '@/components/head'
import foot from '@/components/foot'
import tapbar from '@/components/tapbar'
import login from '@/components/login'
import toast from '@/components/toast'
// import content_current from '@/components/content'
import search from './components/search'
// import Footer from './components/Foot'
export default {
  name: 'App',
  components:{
      nut_head,
      tapbar,
      foot,
      login,
      toast,
      // content_current,
      // Echo,
      search,
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
icon {
  width:20px;
}
</style>
