<!-- global-top.vue -->
<template>
  <footer 
    v-if="$slidev.nav.currentLayout !== 'cover'"
    class="absolute bottom-0 right-0 p-2"
    >
    <img src="techage.png" class="h-5 opacity-50" />
  </footer>
  <footer 
    v-if="$slidev.nav.currentLayout !== 'cover'"
    class="absolute bottom-0 left-0 p-2"
    >
    <img src="nx-icon-dark.png" class="h-5 opacity-50" />
  </footer>
</template>
