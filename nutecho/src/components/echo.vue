<template>
<div>
    <div class="button-sp-area" style="text-align: center;">
        <!-- <Audio/> -->
        <br>

          <!-- 自动播放语音 -->
          <audio src="" controls autoplay class="text-center" id="player">
          </audio>
          <!-- 自动播放语音 -->
        <br>

        <!-- @: 无效时改回用v-on -->
        <a v-on:click.prevent="audio_start" href="" class="weui-btn weui-btn_mini weui-btn_primary">audio_start</a>
        <a v-on:click.prevent="audio_stop" href="javascript:;" class="weui-btn weui-btn_mini weui-btn_default">audio_stop</a>
        <!-- <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_warn">按钮</a> -->
    </div>

    <div class="weui-flex">
        <div class="weui-flex__item"></div>
        <div class="weui-flex__item" style="text-align: center;">

           <!--  <a href="javascript:;" class="weui-btn weui-btn_warn">Send to Echo</a>

            <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_primary">按钮</a>
            <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_default">按钮</a>
            <a href="javascript:;" class="weui-btn weui-btn_mini weui-btn_warn">按钮</a> -->
            <!-- <div class="weui-cells__title">Add Echo</div> -->
            <div class="weui-cells">
                <router-link to="/echo_add" class="weui-cell weui-cell_access" href="javascript:;">
                    
                    <div class="weui-cell__bd">
                        <p>Add Echo</p>
                    </div>
                    <div class="weui-cell__hd"><img src="../svg/add.svg" alt="" style="width:20px;margin-right:5px;display:block"></div>
                </router-link>
            </div>
        </div>

        <div class="weui-flex__item"></div>
    </div>
</div>
</template>

<script>
import echo_add from '@/components/echo_add'

export default {
    name: "echo",
    data:function () {
        return {
            http : this.$store.state.http,
            wss : 'ws://0.0.0.0:5000/',
            // ws : new WebSocket(wss + 'echo/nut');  //建立socket连接
            audio_record : '',
        }
    },
    components:{
        echo_add,
    },
    // created: function () {
    //     // `this` 指向 vm 实例
    // },
    // created:function (){
    // mounted:() => {
    mounted:function(){
        const http = 'http://0.0.0.0:5000/'
        const wss = 'ws://0.0.0.0:5000/'
        // const wss = 'ws://127.0.0.1:5000/'
        // const wss = 'ws://192.168.11.78:5000/'


        var get_file = http + "get_file/"; // nutbot返回的答案语音文件地址
        var ws = new WebSocket(wss + 'echo/nut');  //建立socket连接
        var audio_record = null; // 录音对象 开辟一个储存audio数据的空间
        var audio_obj = new AudioContext(); // 浏览器打开麦克风的对象（不能录音） 实现录音功能需要Recorder.js



        // 此段属舶来品 #################
        // 获取各种浏览器的media对象
        navigator.getUserMedia = (navigator.getUserMedia ||
            navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia ||
            navigator.msGetUserMedia);

        navigator.getUserMedia({audio: true}, create_stream, function (err) {
            // 使用获取到的媒体对象
            // {audio: true} 打开audio的访问
            // create_stream 创建一个媒体流容器
            console.log(err)
        });

        var _this = this;
        function create_stream(user_media){
            // 创建一个媒体流容器 用来记录媒体内容
            var stream_input = audio_obj.createMediaStreamSource(user_media);
            // 将这个容器传给Recorder
            _this.audio_record = new Recorder(stream_input);
        }
        // 此段属舶来品 #################



        // 若server端传回回答语音文件名 拼接为获取语音文件数据流的类似接口地址 设置给audio的html标签进行调用（达到自动播放的目的）
        ws.onmessage = function(data){
            console.log(get_file);
            console.log(data);
            console.log(data.data);
            document.getElementById('player').src = get_file + data.data;
        }
    },
    methods: {
        // 开始录音
        audio_start(){
            console.log('audio_start')
            this.audio_record.record()
        },
        // 停止录音 发送到server 并清空录音对象
        audio_stop(){
            console.log('audio_stop')
            this.audio_record.stop();    // 停止录音

            // 向socket的server端发送录音数据流
            this.audio_record.exportWAV(function (wav_file) {
                ws.send(wav_file);
            })

            // get_audio()

            // 清空录音对象
            this.audio_record.clear();
        },
    }
}

</script>

<style>
</style>

