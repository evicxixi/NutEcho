<template>
<div class="weui-panel weui-panel_access">
    <div class="weui-panel__hd">content_current {{content_current}}</div>
    <div class="weui-panel__bd">
        
        <!-- router循环开始 -->
        <router-link v-for="content in content_list" to="/content_current" v-on:click="current(content.content_id)" class="weui-media-box weui-media-box_appmsg">
            <div class="weui-media-box__hd">

                <!-- 标签内模板语法需用v-bind（支持字符串拼接） -->
                <img class="weui-media-box__thumb" v-bind:src="http + 'get_file/' + content.content_id + '.jpg' " >
            </div>
            <div class="weui-media-box__bd">
                <h4 class="weui-media-box__title">{{ content.title }}</h4>
                <p class="weui-media-box__desc">{{ content.author }}</p>
            </div>
        </router-link>
    </div>
    <div class="weui-panel__ft">
        <a href="javascript:void(0);" class="weui-cell weui-cell_access weui-cell_link">
            <div class="weui-cell__bd">查看更多</div>
            <span class="weui-cell__ft"></span>
        </a>    
    </div>
</div>
</template>

<script>
// import content_current from '@/components/content'
import axios from 'axios'



export default {
    name: "content_list",
    data:function () {
        return {
            http : 'http://0.0.0.0:5000/',
            content_list:[2,3,4],
        }
    },
    computed: {
        content_current:function () {
            // body...
            var data = this.$store.state.content_current;
            console.log(data,typeof(data),data);
            return data
        },
    },
    components:{
      // content_current,
    },
    mounted: function () {
        // 1. 从server端取值content_list
        // 2. 提交到store字段content_list
        // 为什么用到箭头函数（未完成）
        axios.post(this.http+'get_content_list', {})
        .then((data) => {
            // console.log('data.data',typeof(data.data),data.data);
            this.content_list = data.data;
            // 提交到store
            this.$store.commit('init',data.data);
        })
        .catch(function (error) {
            console.log('error',typeof(error),error);
        });
    },
    methods: {
        current(content_id){
            // console.log('content_id',content_id);
            // 提交到store
            this.$store.commit('content',content_id);
        },
    }
}


</script>

<style>
</style>

