<template>
<div>
    
    <article v-if="user">
    <h1 style="text-align: center;">Person</h1>
    <div class="weui-cells__title">Person Info</div>
    <div class="weui-cells weui-cells_form">
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Username</label></div>
            <div class="weui-cell__bd">
                <input id="username" class="weui-input" type="text" placeholder="Username" :value="user.username" />
            </div>
        </div>
        <div class="weui-cell">
            <div class="weui-cell__hd"><label class="weui-label">Nickname</label></div>
            <div class="weui-cell__bd">
                <input id="nickname" class="weui-input" type="text" placeholder="Nickname" :value="user.nickname"/>
            </div>
        </div>

    </div>

    <div class="weui-cells__title">My Echo</div>
    <div class="weui-cells">
        <a v-for="echo in echo_list" class="weui-cell weui-cell_access" href="javascript:;">
            <div class="weui-cell__bd" v-bind:id="echo.serial">
                <p>{{echo.echo_name}}</p>
            </div>
            <div class="weui-cell__ft">
            </div>
        </a>
    </div>




    <!-- <div class="page list js_show">
        <div class="page__hd">
            <h1 class="page__title"></h1>
        </div>
        <div class="page__bd">

            <div class="weui-cells__title">My Echo</div>
            <div class="weui-cells">
                <a class="weui-cell weui-cell_access" href="javascript:;">
                    <div class="weui-cell__bd">
                        <p>cell standard</p>
                    </div>
                    <div class="weui-cell__ft">
                    </div>
                </a>
                <a class="weui-cell weui-cell_access" href="javascript:;">
                    <div class="weui-cell__bd">
                        <p>cell standard</p>
                    </div>
                    <div class="weui-cell__ft">
                    </div>
                </a>
            </div>

            <div class="weui-cells__title">带说明、跳转的列表项</div>
            <div class="weui-cells">
                <a class="weui-cell weui-cell_access" href="javascript:;">
                    <div class="weui-cell__bd">
                        <p>cell standard</p>
                    </div>
                    <div class="weui-cell__ft">说明文字</div>
                </a>
                <a class="weui-cell weui-cell_access" href="javascript:;">
                    <div class="weui-cell__bd">
                        <p>cell standard</p>
                    </div>
                    <div class="weui-cell__ft">说明文字</div>
                </a>

            </div>

            <div class="weui-cells__title">带图标、说明、跳转的列表项</div>
            <div class="weui-cells">

                <a class="weui-cell weui-cell_access" href="javascript:;">
                    <div class="weui-cell__hd"><img src="" alt="" style="width:20px;margin-right:5px;display:block"></div>
                    <div class="weui-cell__bd">
                        <p>cell standard</p>
                    </div>
                    <div class="weui-cell__ft">说明文字</div>
                </a>
                <a class="weui-cell weui-cell_access" href="javascript:;">
                    <div class="weui-cell__hd"><img src="" alt="" style="width:20px;margin-right:5px;display:block"></div>
                    <div class="weui-cell__bd">
                        <p>cell standard</p>
                    </div>
                    <div class="weui-cell__ft">说明文字</div>
                </a>
            </div>
        </div>
        <div class="page__ft">
            <a href="javascript:home()"><img src=""></a>
        </div>
    </div> -->
















    <div class="weui-btn-area">
        <a v-on:click="logout" class="weui-btn weui-btn_warn">Logout</a>
    </div>
    </article>
    <article v-else class="weui-article" style="text-align: center;">
        <h1 class="">您尚未登录！</h1>

        <i class="weui-icon-info weui-icon_msg"></i>

        <div class="weui-flex__item">
            <router-link to="/login" class="weui-btn weui-btn_mini weui-btn_primary">Login</router-link>
            <router-link to="/signin" class="weui-btn weui-btn_mini weui-btn_default"> Signin </router-link>
        </div>
        <!-- <foot/> -->
    </article>
<!-- </router-view> -->
</div>
</template>

<script>
import login from '@/components/login'
import signin from '@/components/signin'// import foot from '@/components/foot'
import axios from 'axios'
export default {
    name: 'person',
    data () {
        return {
            http : this.$store.state.http,
        }
    },
    components:{
        login,
        signin,
        // foot,
    },
    computed:{
        user(){
            // var ret = this.$store.state.user;
            var user = window.localStorage.getItem('user');
            // console.log('data',typeof(data),data);
            var user = JSON.parse(user);
            return user
        },
        echo_list(){
            var data = this.$store.state.echo_list;
            console.log('echo_list',typeof(data),data)
            return data
        },
    },
    methods:{
        logout(){
            this.$store.commit('logout');
            this.$router.go(0); //刷新路由
        }
    },
    // created(){
    mounted(){
    },
}
</script>
</style>
