<template>
  <div id="app">
    <lhead/>
    <!-- <Search/> -->
    <!-- <router-view/> -->
    <Tapbar/>
    <!-- <foot/> -->
  </div>
</template>

<script>
// import 'vue-awesome/dist/css/bootstrap.min.css'
// import '/node_moudules/vue-awesome/dist/vue-awesome.js'
import lhead from '@/components/head'
import foot from './components/foot'
import Tapbar from './components/tapbar'
// import content_current from '@/components/content'
// import Search from './components/search'
// import Footer from './components/Foot'
export default {
  name: 'App',
  components:{
      lhead,
      Tapbar,
      foot,
      // content_current,
      // Echo,
      // Search,
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
icon {
  width:20px;
}
</style>
