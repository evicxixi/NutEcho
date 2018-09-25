<template>
<div>
    <div class="weui-flex">
        <div class="weui-flex__item"><div class="placeholder">weui</div></div>
        <div class="weui-flex__item"><div class="placeholder">{{ content_current }}</div></div>
        <div class="weui-flex__item"><div class="placeholder">weui</div></div>
    </div>
    <div class="button-sp-area">
       <!--  <a href="javascript:;" class="weui-btn weui-btn_plain-default">按钮</a>
        <a href="javascript:;" class="weui-btn weui-btn_plain-default weui-btn_plain-disabled">按钮</a> -->
        <a href="javascript:;" class="weui-btn weui-btn_plain-primary">按钮</a>
        <!-- <a href="javascript:;" class="weui-btn weui-btn_plain-primary weui-btn_plain-disabled">按钮</a> -->
        <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_primary">按钮</a>
        <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_default">按钮</a>
        <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_warn">按钮</a>
    </div>
</div>

</template>

<script>



export default {
    name: "content_current",
    data:function () {
        return {
            http : 'http://0.0.0.0:5000/',
            // content_current:{},
        }
    },
    // props:[],
    // watched: {
    // beforeCreated:{
    // created:{
    computed: {
        content_current:function () {
            var data = this.$store.state.content_current;
            // var data = JSON.parse(JSON.stringify(data));    
            console.log('data',typeof(data),data);
            return data
        },
    },
    components:{
    },
    // created: function () {
    mounted: function () {
        // this.$store.commit('init',data.data);
        // console.log('this.$store.state.content_current',this.$store.state);
        // this.content = this.$store.state.content_current;
        // console.log('this.content',this.content);
    },
    methods: {
    }
}


</script>

<style>
</style>

