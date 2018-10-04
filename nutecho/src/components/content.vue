<template>
<div>

    <div id="actionSheet_wrap">
<!--         <div v-bind:style=style_mask class="weui-mask_transparent actionsheet__mask" id="mask"></div> -->
    <!-- <div v-bind:class="{'iosmask':isSelected}" class="weui-mask" id="iosMask" ></div> -->
    <div v-bind:class="[isSelected ? 'iosmask' : 'un_iosmask']" class="weui-mask" id="iosMask" ></div>
        <div v-bind:class="{'weui-actionsheet_toggle':isSelected}" class="weui-actionsheet" id="weui-actionsheet">
            <div class="weui-actionsheet__menu">
                <div v-for="echo in echo_list" class="weui-actionsheet__cell">{{echo.echo_name}}</div>
            </div>
            <div class="weui-actionsheet__action">
                <div v-on:click="echo_list_show" class="weui-actionsheet__cell" id="echo_list_hide">取消</div>
            </div>
        </div>
    </div>
    <div class="" v-bind:style=style_cover_div >
        <audio id="audio" v-bind:src=content_current_audio style="display:none" controlos="controls" loop="loop"></audio>
        <img v-bind:src=content_current_cover :class="[isPlaying ? 'rotate' : '']" style="width: 130px;height: 130px; border-radius: 50%; border:0.5px solid #aaa; box-shadow:1px 1px 5px #888888;" id="avatar" />
        <!-- <div v-bind:style="style_cover" id="avatar"></div> -->
    </div>
    <!-- <br> -->
    <div class="weui-loadmore weui-loadmore_line">
        <span class="weui-loadmore__tips">{{content_current.title}}</span>
    </div>
    <div class="weui-flex">
        <div class="weui-flex__item"></div>
        <div class="weui-flex__item" style="text-align: center;">

            

            <a v-on:click="play" href="javascript:;" id="audio_btn" class="weui-btn" v-bind:class="[ isPlaying ? 'weui-btn_warn' : 'weui-btn_primary']"><img src="../svg/play.svg" style="width:16px;margin-right:5px;" >{{isPlaying ? 'Stop' : 'Player'}}</a>

           <!--  <a href="javascript:;" class="weui-btn weui-btn_warn">Send to Echo</a>

            <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_primary">按钮</a>
            <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_default">按钮</a>
            <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_warn">按钮</a> -->
            <div class="weui-cells__title">Send to Echo</div>
            <div class="weui-cells">
                <a class="weui-cell weui-cell_access" href="javascript:;" id="echo_list" v-on:click="echo_list_show">
                    <div class="weui-cell__bd">
                        <p>Choice Echo</p>
                    </div>
                    <div class="weui-cell__ft">
                    </div>
                </a>
            </div>
        </div>

        <div class="weui-flex__item"></div>
    </div>
</div>

</template>

<script>



export default {
    name: "content_current",
    data:function () {
        return {
            http : this.$store.state.http,
            isPlaying : false,
            style_cover_div:{
                textAlign: 'center',
                marginTop: '5px',
            },
            isSelected:false,
        }
    },
    computed: {
        content_current() {
            var data = this.$store.state.content_current;
            // var data = JSON.parse(JSON.stringify(data));    
            // console.log('data',typeof(data),data);
            return data
        },
        content_current_cover() {
            // 当前文件的cover请求url
            var url = this.http + "get_file/" + this.$store.state.content_current.content_id + ".jpg";
            return url
        },
        content_current_audio() {
            // 当前文件的cover请求url
            var url = this.http + "get_file/" + this.$store.state.content_current.content_id + ".mp3";
            return url
        },
        class_audio_btn(){
            return {
              active: this.isActive && !this.error,
              'text-danger': this.error && this.error.type === 'fatal'
            }
        },
        echo_list(){
            return this.$store.state.echo_list;
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
        play(){
            var audio = document.getElementById('audio');
            var audio_btn = document.getElementById('audio_btn');
            if(!this.isPlaying){
                audio.play();
                this.isPlaying = true;
                // audio_btn.innerText = 'Stop';
                // audio_btn.class = 'weui-btn weui-btn_warn';
            }
            else{
                audio.pause();
                this.isPlaying = false;
                // audio_btn.innerText = 'Player';
                // audio_btn.class = 'weui-btn weui-btn_primary';
            }
        },
        echo_list_show(){
            // var echo_list = document.getElementById('echo_list');
            // var echo_list_hide = document.getElementById('echo_list_hide');
            // if(!this.isSelected){
                this.isSelected = !this.isSelected;
            // }
        },
    }
}


</script>

<style>

@-webkit-keyframes rotation {
    from {-webkit-transform: rotate(0deg);
}to {
    -webkit-transform: rotate(360deg);
}}
.rotate {
    -webkit-transform: rotate(360deg);
    animation: rotation 16s linear infinite;
    -moz-animation: rotation 16s linear infinite;
    -webkit-animation: rotation 16s linear infinite;
    -o-animation: rotation 16s linear infinite;
}
.iosmask{
    opacity:1;
}

.un_iosmask{
    display:None;
}
</style>

