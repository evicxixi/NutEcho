# nutecho

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).


# nutecho项目webApp

## 功能介绍
~~~
1. 扫码添加echo设备，验证是否正品。
2. 绑定echo与app的朋友关系。
3. 加载音乐资源，并发送选中音乐到echo。
4. 人机对话：智能对话，支持配置自定义问答。
5. 查看所有对话记录
~~~

## 前端依赖模块
~~~
weui
    导入weui后似乎无js，后将js手动引入在index.html中。
    
vue-svg-icon
    最开始使用Vue-Awesome,配置失败，后改用vue-svg-icon
~~~


## 后端依赖模块
~~~
pip install gevent
pip install baidu-aip
pip install ffmpeg
pip install gevent-websocket

brew install mongodb
pip install pymongo
~~~


## 基于以下技术实现：
~~~
WebSocket、百度语音识别API、百度语义分析API、图灵机器人API、MongoDB
~~~

## 文件结构
~~~
main.py 主文件
aipspeech.py 语音识别相关
aipnlp.py 语义识别相关
~~~


## 开发日志
20180923
~~~
<debug> @: 无效时改回用v-on

标签内模板语法需用v-bind（支持字符串拼接）
<img class="weui-media-box__thumb" v-bind:src="http + 'get_file/' + content.content_id + '.jpg' " >

这里的属性content_list更新需要改用箭头函数（未完成)
data:function () {
    return {
        http : 'http://0.0.0.0:5000/',
        content_list:[2,3,4],
    }
},
mounted: function () {
    axios.post(this.http+'get_content_list', {})
    .then((data) => {
        this.content_list = data.data;
    })
},

组件从store中取值：
因data中仅能存放明确的值，从store中取值需放在computed中。
~~~

20180925
~~~
{__ob__: Observer}
A组件向store仓库的content_list字段提交一个值后 然后在A组件可以正常取到这个值
但是在B组件中取content_list字段的值  一直是打印{__ob__: Observer}
备注：大坑 搞了我整整一天 原来是vue单页面应用不能在两个浏览器窗口分别赋值 与 取值。
在同一个页面赋值在同一个页面取值没问题（不按是否同一个组件）。
~~~
