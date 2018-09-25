<template>
  <div>
  <br>

      <!-- 自动播放语音 -->
      <audio src="" controls autoplay class="text-center" id="player">
      </audio>
      <!-- 自动播放语音 -->
  <br>

  </div>
</template>

<script>
// import Recorder from '@/js/Recorder.js'

export default {
  name: "Laudio",
  methods: {
    // 开始录音
    audio_start(){
        console.log('audio_start')
        // audio_record.record()
    },
  }
}

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


function create_stream(user_media){
    // 创建一个媒体流容器 用来记录媒体内容
    var stream_input = audio_obj.createMediaStreamSource(user_media);
    // 将这个容器传给Recorder
    audio_record = new Recorder(stream_input);
}
// 此段属舶来品 #################



// // 开始录音
// function audio_start(){
//     console.log('audio_start')
//     audio_record.record()
// }

// 向socket的server端发送录音数据流
function get_audio() {
    audio_record.exportWAV(function (wav_file) {
        ws.send(wav_file);
    })
}

// 停止录音 发送到server 并清空录音对象
function audio_stop(){
    console.log('audio_stop')
    audio_record.stop();    // 停止录音

    // // 向socket的server端发送录音数据流
    // audio_record.exportWAV(function (wav_file) {
    //     ws.send(wav_file);
    // })

    get_audio()

    // 清空录音对象
    audio_record.clear();
}

// 若server端传回回答语音文件名 拼接为获取语音文件数据流的类似接口地址 设置给audio的html标签进行调用（达到自动播放的目的）
ws.onmessage = function(data){
    console.log(get_file);
    console.log(data);
    console.log(data.data);
    document.getElementById('player').src = get_file + data.data;
}
</script>

<style>
</style>

