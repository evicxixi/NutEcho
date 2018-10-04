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
            http : this.$store.state.http,
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
            axios.post(this.http + 'login', data).then((data) => {
                    console.log('data.data',typeof(data.data),data.data);
                    if (data.data['code'] == 1){
                        var ret = JSON.stringify(data.data);
                        // console.log('ret',typeof(ret),ret);
                        window.localStorage.setItem("user", ret);
                        this.$store.commit('login',ret);
                        this.$router.push('/person');
                    }
                }).catch(function (error) {
                    console.log('error',typeof(error),error);
                }
            );
        }
    }
}
</script>
</style>
