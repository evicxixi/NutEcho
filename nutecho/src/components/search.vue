<template>
        
<div class="weui-search-bar" id="search_bar" 
      @result-click="resultClick">
    <form class="weui-search-bar__form">
        <div class="weui-search-bar__box">
            <i class="weui-icon-search"></i>
            <input type="search" class="weui-search-bar__input" placeholder="搜索" required="">
            <a href="javascript:" class="weui-icon-clear"></a>
        </div>
        <label class="weui-search-bar__label">
            <i class="weui-icon-search"></i>
            <span>搜索</span>
        </label>
    </form>
    <a href="javascript:" class="weui-search-bar__cancel-btn">取消</a>
</div>
</template>

<script>

  export default {
    name: "search",
    methods: {
        resultClick (item) {
          window.alert('you click the result item: ' + JSON.stringify(item))
        },
    }
  }
</script>
var ui = weui.searchBar('#search_bar');

// ui.onclick(function () {
//     // body...
//     alert('223')
// })

</style>

