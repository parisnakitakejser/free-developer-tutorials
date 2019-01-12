<template>
  <div id="AboutComponent">
    <p>AboutComponent works!</p>

    <ul>
      <li><router-link :to="{name: 'AboutMe'}">Me</router-link></li>
      <li><router-link :to="{name: 'AboutDog'}">Dog</router-link></li>
    </ul>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'AboutComponent'
}
</script>
