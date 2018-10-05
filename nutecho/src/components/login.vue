<template>
<div>
    <article class="weui-article" style="text-align: center;">
    <h1>Login</h1>
    </toast>
    </article>
    <div class="weui-cells__title">单选列表项</div>
    <div class="weui-cells weui-cells_form">
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Username</label></div>
            <div class="weui-cell__bd">
                <input id="username" class="weui-input" type="text" placeholder="Username"/>
            </div>
        </div>
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Password</label></div>
            <div class="weui-cell__bd">
                <input id="password" class="weui-input" type="password" placeholder="Password"/>
            </div>
        </div>
    </div>
    <div class="weui-btn-area">
        <a v-on:click="signin" class="weui-btn weui-btn_primary">Login</a>
    </div>


</div>
</template>

<script>
import toast from '@/components/toast'
import hex_md5 from 'js-md5';
import axios from 'axios'
export default {
    name: 'login',
    data () {
        return {
            // http : this.$store.state.http,
            http : 'http://0.0.0.0:5000/',
        }
    },
    components: { 
        toast,
    },
    methods:{
        signin(){
            // console.log('signin');            
            // 取值4个signin字段 同时对密码做前端校验
            var password = document.getElementById("password").value;
            var password = hex_md5(password);
            var username = document.getElementById("username").value;

            var data = {
                    'username': username,
                    'password': password,
                };

            // 发送singnin注册请求
            axios.post(
                this.http + 'login',
                data
            ).then((data) => {
                console.log('login data.data',typeof(data.data),data.data);
                // data.data.data = {
                //     echo_list: (2) [{…}, {…}]
                //     gender: "0"
                //     nickname: "红果"
                //     username: "rednut"
                //     _id: "5bb7cab4cd817298c678676a"
                // }
                if (data.data['code'] == 1){
                    var ret = JSON.stringify(data.data.data);
                    // var ret = data.data;
                    // console.log('ret',typeof(ret),ret);
                    window.localStorage.setItem("user", ret);
                    this.$store.commit('login',ret);
                    return ret
                }
            }).then((data) => {
                // 初始化我的echo_list设备信息
                // console.log('初始化我的echo_list设备信息 data',typeof(data),data);
                var data = JSON.parse(data);
                axios.post(this.http + 'API/' + 'echo_list', data).then((data) => {
                        console.log('login echo_list',typeof(data.data.data),data.data.data);
                        if (data.data['code'] == 1){
                            this.$store.commit('echo_list',data.data.data);
                        }
                    }).catch(function (error) {
                        console.log('error',typeof(error),error);
                    }
                );
            }).then((data) => {
                setTimeout(() => {
                    // 首次初始化echo_list数据，等待一段时间再跳转。
                    this.$router.push('/person');
                },50)
            }).catch(function (error) {
                console.log('error',typeof(error),error);
            });
        },
    }
}
</script>
</style>
