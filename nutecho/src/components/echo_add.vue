<template>
<div>
    </toast>
    <article class="weui-article" style="text-align: center;">
    <h1>Add Echo</h1>
    </article>
    <div v-if="is_verify">
        <toast/>
        <div class="weui-cells__title">完善Echo信息</div>
        <div class="weui-cells weui-cells_form">
            <div class="weui-cell">
                <div class="weui-cell__hd"><label class="weui-label">Echo Name</label></div>
                <div class="weui-cell__bd">
                    <input id="echo_name" class="weui-input" type="text" placeholder="Echo name" value="小萝卜"/>
                </div>
            </div>
            <div class="weui-cell">
                <div class="weui-cell__hd"><label class="weui-label">Master</label></div>
                <div class="weui-cell__bd">
                    <input id="user_remark" class="weui-input" type="text" placeholder="Master Remark" value="爸爸" />
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
            <a v-on:click="echo_add" class="weui-btn weui-btn_primary">Add Echo</a>
        </div>
    </div>
    <div v-else>
        
        <div class="weui-cells__title">输入编号 校验设备</div>
        <div class="weui-cells weui-cells_form">
            <div class="weui-cell">
                <div class="weui-cell__hd"><label class="weui-label">设备编号</label></div>
                <div class="weui-cell__bd">
                    <input id="serial" class="weui-input" type="text" placeholder="请输入Echo底部8位数字编号" value="111" />
                </div>
            </div>
        </div>
        <div class="weui-btn-area">
            <a v-on:click="verify" class="weui-btn weui-btn_primary">Verify</a>
        </div>
    </div>


</div>
</template>

<script>
import toast from '@/components/toast'
import hex_md5 from 'js-md5';
import axios from 'axios'
export default {
    name: 'verify',
    data () {
        return {
            http : 'http://0.0.0.0:5000/API/',
            is_verify: false,
            // toast_msg: '设备校验通过，感谢您选择NutEcho产品！',
        }
    },
    components: { 
        toast,
    },
    computed:{
        user(){
            // var ret = this.$store.state.user;
            var user = window.localStorage.getItem('user');
            // console.log('ret',typeof(ret),ret);
            var user = JSON.parse(user);
            return user
        },
    },
    methods:{
        verify(){
            // console.log('signin');            
            // 取值serial字段
            var serial = document.getElementById("serial").value;
            var data = {
                    'serial': serial,
                };

            // 发送serial设备校验请求
            axios.post(this.http + 'verify', data).then((data) => {
                    console.log('data.data',typeof(data.data),data.data);
                    if (data.data['code'] == 1){
                        this.is_verify = true;
                        this.serial = serial;
                        this.$store.commit('msg_toast',data.data['msg']);
                    }
                    else{
                        this.$store.commit('msg_toast',data.data['msg']);
                    }
                }).catch(function (error) {
                    console.log('error',typeof(error),error);
                }
            );
        },
        echo_add(){
            // console.log('signin');            
            // 取值serial字段
            var echo_name = document.getElementById("echo_name").value;
            var user_remark = document.getElementById("user_remark").value;
            var gender_list = document.getElementsByName('radio1')
            for(var i = 0; i < gender_list.length; i++) {
                if(gender_list[i].checked) {
                    var gender = gender_list[i].value;
                }
            };
            var user_obj = window.localStorage.getItem("user");
            var user_obj = JSON.parse(user_obj);
            // console.log('user',typeof(user),user);
            var data = {
                'echo_name': echo_name,
                'gender': gender,
                'serial': this.serial,
                'user_id': user_obj['_id'],
                'user_remark': user_remark,
                // 'user_username': user['username'],
            };
            // console.log('data',typeof(data),data);

            // 发送echo设备信息请求（含绑定用户信息）
            axios.post(this.http + 'echo_add', data).then((data) => {
                    console.log('data.data',typeof(data.data),data.data);
                    if (data.data['code'] == 1){
                        this.$store.commit('msg_toast',data.data['msg']);
                        this.$router.push('/person');
                    }
                    else{
                        this.$store.commit('msg_toast',data.data['msg']);
                    }
                }).catch((error) => {
                    console.log('error',typeof(error),error);
                }
            );
        }
    }
}
</script>
</style>
