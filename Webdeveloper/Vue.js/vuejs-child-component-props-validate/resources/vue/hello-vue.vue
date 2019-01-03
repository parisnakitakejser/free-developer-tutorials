<template>
  <div>
    <h1>{{ title }}</h1>
    <SubTestChild :groups="group.first" dataview="list-view" />
    <SubTestChild :groups="group.secound" dataview="grid-view" />
    <SubTestChild :groups="group.third" dataview="list-view" />
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
      title: 'Hello Vue',
      group: {
        'first': [{
          'title': 'First group - First title'
        },{
          'title': 'First group - Secound title'
        },{
          'title': 'First group - Third title'
        }],
        'secound': [{
          'title': 'Secound group - First title'
        },{
          'title': 'Secound group - Secound title'
        },{
          'title': 'Secound group - Third title'
        }],
        'third': [{
          'title': 'Third group - First title'
        },{
          'title': 'Third group - Secound title'
        },{
          'title': 'Third group - Third title'
        }]
      }
    }
  },
  method: {

  }
}
</script>
