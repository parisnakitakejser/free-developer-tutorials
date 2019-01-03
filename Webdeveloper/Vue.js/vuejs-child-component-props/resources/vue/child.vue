<template>
  <div class="sub-child">
    <h2>{{title}}</h2>
    <ul v-for="(child, index) in selectedSubGroups">
      <li>[{{index}}] {{child.title}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['groups'],
  data: function() {
    return {
      'title': 'Test child.vue - props'
    }
  },
  computed: {
    selectedSubGroups() {
      return this.groups;
    }
  }
}
</script>
