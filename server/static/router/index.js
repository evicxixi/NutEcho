
// import Vue from 'vue'
import Vue from "/static/js/vue.min.js"
// import Router from '/static/js/vue-router.js'
import routers from "/static/router/router.js"



var app = new Vue({
    el: '#app',
    routers,
    // components:{
    //     // 'record-button':record-button,
    //     // 'localComponent':localComponent,
    // },
    methods:{
        audio_start: function(){
            // alert(223);
            console.log('audio_start.......')
            // audio_record.record();
        },
        say: function (message) {
          alert(message);
        }
    }
})