<template>
  <div class="sub-child">
    <h2>{{title}}</h2>
    <hr />
    <ul>
      <li v-for="(child, index) in childLoop">
        <u>[{{index}}]</u> <strong>{{child.title}}</strong><br />
        <i>{{child.desc}}</i>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      'title': 'This is child.vue file',
      'childLoop': [{
        'title': 'First title',
        'desc': 'first desc from child.vue file coming here!'
      },{
        'title': 'Secound title',
        'desc': 'secound desc from child.vue file coming here!'
      },{
        'title': 'Thrid helloe child.vue',
        'desc': 'thrid desc from child.vue file coming here!'
      }]
    }
  }
}
</script>
