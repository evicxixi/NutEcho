<template>
<div>
    <nut_head/>
    <article class="weui-article" style="text-align: center;">
    <h1>Signin</h1>
    </toast>
    </article>
    <div class="weui-cells__title">单选列表项</div>
    <div class="weui-cells weui-cells_form">
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Username</label></div>
            <div class="weui-cell__bd">
                <input id="username" class="weui-input" type="text" placeholder="Username" value="rednut"/>
            </div>
        </div>
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Password</label></div>
            <div class="weui-cell__bd">
                <input id="password" class="weui-input" type="password" placeholder="Password" value="1"/>
            </div>
        </div>
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Re-Password</label></div>
            <div class="weui-cell__bd">
                <input id="re_password" class="weui-input" type="password" placeholder="Re-Password" value="1"/>
            </div>
        </div>
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Nickname</label></div>
            <div class="weui-cell__bd">
                <input id="nickname" class="weui-input" type="text" placeholder="Nickname" value="红果"/>
            </div>
        </div>
    </div>

    <div class="weui-cells__title">Sex</div>
    <div class="weui-cells weui-cells_radio">
        <label class="weui-cell weui-check__label">
            <div class="weui-cell__bd">
                <p>Male</p>
            </div>
            <div class="weui-cell__ft">
                <input type="radio" class="weui-check" name="radio1" value="1">
                <span class="weui-icon-checked"></span>
            </div>
        </label>
        <label class="weui-cell weui-check__label">
            <div class="weui-cell__bd">
                <p>Famale</p>
            </div>
            <div class="weui-cell__ft">
                <input type="radio" name="radio1" class="weui-check" value="0" checked="checked">
                <span class="weui-icon-checked"></span>
            </div>
        </label>
    </div>


    <div class="weui-btn-area">
        <a v-on:click="signin" class="weui-btn weui-btn_primary">Signin</a>
    </div>


</div>
</template>

<script>
import nut_head from '@/components/head'

import toast from '@/components/toast'
import hex_md5 from 'js-md5';
import axios from 'axios'
export default {
    name: 'signin',
    data () {
        return {
            // http : this.$store.state.http,
            http : 'http://0.0.0.0:5000/',
        }
    },
    components: { 
        toast,
        nut_head,
    },
    methods:{
        signin(){
            // console.log('signin');            
            // 取值4个signin字段 同时对密码做前端校验
            var password = document.getElementById("password").value;
            var re_password = document.getElementById("re_password").value;
            if(password != re_password) {
                alert('密码不一致');
                return false;
            } else {
                var password = hex_md5(password);
                // console.log('password',password)
            }

            var username = document.getElementById("username").value;
            var nickname = document.getElementById("nickname").value;

            var gender_list = document.getElementsByName('radio1')
            for(var i = 0; i < gender_list.length; i++) {
                if(gender_list[i].checked) {
                    var gender = gender_list[i].value;
                }
            };

            var data = {
                    'username': username,
                    'password': password,
                    'nickname': nickname,
                    'gender': gender,
                };

            // 发送singnin注册请求
            axios.post(this.http + 'signin', data).then((data) => {
                    console.log('data.data',typeof(data.data),data.data);
                    // window.localStorage.setItem("username", username);
                }).catch(function (error) {
                    console.log('error',typeof(error),error);
                }
            );
        }
    }
}
</script>
</style>
