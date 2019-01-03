<template>
  <div class="sub-child">
    <h2>{{this.dataview}}</h2>

    <ul v-for="(child, index) in selectedSubGroups">
      <li>[{{index}}] {{child.title}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
      'groups': {
        type: Array,
        required: true
      },
      'dataview': {
        type: String,
        required: true,
        validator(value) {
          return ['list-view', 'grid-view'].includes(value);
        }
      }
  },
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
