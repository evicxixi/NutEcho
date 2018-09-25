<template>
  <div class="weui-tab__content">
      <div class="item">
          3
          <Search/>
      </div>
  </div>
</template>

<script>

import Search from '@/components/search'

export default {
  name: "lhead",
  components:{
    Search,
  },
  methods: {
    logout() {
      this.$store.commit('clearToken')
      this.$router.push({path: '/index'})
    }
  }
}
</script>
</style>

