<template>
  <div class="root">
    <h1>{{ title }}</h1>
    <hr />

    <SubTestChild />
  </div>
</template>

<script>
import SubChild from './child.vue';

export default {
  name: 'hello-vue',
  components: {
    'SubTestChild': SubChild
  },
  data: function() {
    return {
      title: 'Hello Vue'
    }
  },
  method: {

  }
}
</script>
