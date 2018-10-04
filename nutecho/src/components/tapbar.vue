<template>
<div class="weui-tab">
    <!-- <nut_head/> -->
    <div class="weui-tab__panel">
      <router-view></router-view>
      <!-- <foot/> -->
    </div>
    <div class="weui-tabbar" style="position: fixed;">
      <router-link to="/echo" class="weui-tabbar__item">
        <img src="../svg/echo.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Echo</p>
      </router-link>

      <router-link to="/" class="weui-tabbar__item">
        <img src="../svg/echo.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Echo</p>
      </router-link>

      <router-link to="/content_list" class="weui-tabbar__item">
        <img src="../svg/resource.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Content</p>
      </router-link>

      <!-- <router-link to="/content_current" class="weui-tabbar__item">
        <img src="../svg/resource.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Content</p>
      </router-link>
 -->
      <router-link to="/person" class="weui-tabbar__item">
        <img src="../svg/person.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Person</p>
      </router-link>

<!--       <router-link to="/setting" class="weui-tabbar__item">
        <img src="../svg/setting.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Setting</p>
      </router-link> -->
    </div>
</div>
</template>

<script>
import nut_head from '@/components/head'
// import foot from '@/components/foot'
// import Echo from '@/components/echo'
import content_list from '@/components/content_list'
import content_current from '@/components/content'
import login from '@/components/login'
import person from '@/components/person'

export default {
  name: "tapbar",
  data () {
      return {
          msg: 'Welcome to Your Vue.js App',
          // http : 'http://0.0.0.0:5000/',
      }
  },
  components:{
    nut_head,
    // foot,
    content_list,
    content_current,
    person,
    // Echo,
  },
  methods: {
  }
}
</script>

</style>

