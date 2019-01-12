<template>
  <div id="app">
    <router-link :to="{name:'Home'}">Home</router-link>
    <router-link :to="{name: 'About'}">About</router-link>
    <router-link :to="{name: 'Contact'}">Contact</router-link>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>
