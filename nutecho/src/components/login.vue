<template>
<div class="weui-cells weui-cells_radio">
    <label class="weui-cell weui-check__label" for="x11">
        <div class="weui-cell__bd">
            <p>cell standard</p>
        </div>
        <div class="weui-cell__ft">
            <input type="radio" class="weui-check" name="radio1" id="x11">
            <span class="weui-icon-checked"></span>
        </div>
    </label>
    <label class="weui-cell weui-check__label" for="x12">

        <div class="weui-cell__bd">
            <p>cell standard</p>
        </div>
        <div class="weui-cell__ft">
            <input type="radio" name="radio1" class="weui-check" id="x12" checked="checked">
            <span class="weui-icon-checked"></span>
        </div>
    </label>
    <a href="javascript:void(0);" class="weui-cell weui-cell_link">
        <div class="weui-cell__bd">添加更多</div>
    </a>
</div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>
</style>
