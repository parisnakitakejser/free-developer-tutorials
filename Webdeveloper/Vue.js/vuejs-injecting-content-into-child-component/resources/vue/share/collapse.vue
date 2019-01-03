<template>
  <div>
    <div style="background: gray; cursor: pointer;">
      <span v-if="open" @click="open = !open">
        &#x25B2; Collapse
      </span>
      <span v-if="!open" @click="open = !open">
        &#x25BC; Expand
      </span>
    </div>

    <slot v-if="open">
      Collapse need data to show/hide
    </slot>
  </div>
</template>

<script>
export default {
  name: 'Collasible',
  data: function() {
    return {
      open: true
    }
  }
}
</script>
