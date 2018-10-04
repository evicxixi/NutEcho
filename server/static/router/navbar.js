
Vue.component('navbar', {
  template: `
    <yd-navbar slot="center" title="Nut Echo">
        <router-link to="/" slot="left">
            <yd-icon name="qrscan" size="25px" color="#777"></yd-icon>
        </router-link>
        <router-link to="/login" slot="right">
            <yd-icon name="ucenter-outline" size="25px" color="#777"></yd-icon>
        </router-link>
        <router-link to="/foo" slot="right">
            <yd-icon name="ucenter-outline" size="25px" color="#777"></yd-icon>
        </router-link>
        <router-link to="/bar" slot="right">
            <yd-icon name="ucenter-outline" size="25px" color="#777"></yd-icon>
        </router-link>
    </yd-navbar>
    `
})

