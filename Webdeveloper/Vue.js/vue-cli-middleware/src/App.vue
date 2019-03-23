<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <hr />

    <div style="width: 800px; margin: 0 auto;">
      <ul>
        <li><router-link :to="{name: 'Home'}">Home</router-link></li>
        <li><router-link :to="{name: 'Account'}">Account</router-link></li>
      </ul>
      <div style="clear: both;"></div>
    </div>

    <hr />
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

  ul {
    list-style: none;
    display: block;
  }

  ul li {
    float: left;
    margin-right: 5px;
    margin-left: 5px;
  }
</style>
