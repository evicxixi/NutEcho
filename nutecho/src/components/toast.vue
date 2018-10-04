<template>
    <!-- <transition name="fade" > -->
        <div id="toast" v-if="msg">
            <div class="weui-mask_transparent"></div>
            <div class="weui-toast">
                <i class="weui-icon-success-no-circle weui-icon_toast"></i>
                <p class="weui-toast__content">{{msg}}</p>
            </div>
        </div>
    <!-- </transition> -->
</template>

<script>



export default {
    name: "toast",
    data:function () {
        return {}
    },
    computed: {
        msg(){
            return this.$store.state.msg_toast;
        },
    },
    components:{
    },
    methods: {
    },
}


</script>

<style>
/*.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to{
  opacity: 0;
}*/
</style>

