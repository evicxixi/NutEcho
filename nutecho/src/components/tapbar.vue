<template>
<div class="weui-tab">
    <div class="weui-tab__panel">
      <nut_head/>
      <router-view></router-view>
      <!-- <Echo/> -->
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

      <router-link to="/content_current" class="weui-tabbar__item">
        <img src="../svg/resource.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Content</p>
      </router-link>

<!--       <router-link to="/person" class="weui-tabbar__item">
        <img src="../svg/person.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Person</p>
      </router-link>

      <router-link to="/setting" class="weui-tabbar__item">
        <img src="../svg/setting.svg" alt="" class="weui-tabbar__icon">
        <p class="weui-tabbar__label">Setting</p>
      </router-link> -->
    </div>
</div>
</template>

<script>
import nut_head from '@/components/head'
// import Echo from '@/components/echo'
import content_list from '@/components/content_list'
import content_current from '@/components/content'

export default {
  name: "tapbar",
  components:{
    nut_head,
    content_list,
    content_current,
    // Echo,
  },
  methods: {
  }
}
</script>

</style>

