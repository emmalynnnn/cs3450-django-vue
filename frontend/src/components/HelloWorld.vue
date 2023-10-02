<script>
export default {
  name: 'HelloWorldComponent',
  data() {
    return {
      message: '',
    }
  },
  mounted() {
    fetch('http://localhost:8000/polls/')
      .then(res => {
        return res.json();
      })
      .then(result => {
        console.log(result);
        this.message = result.message;
      });
  },
}
</script>

<template>
  <div class="greetings">
    <h1 class="green">Hello here is some Vue!</h1>
    <p>{{ message }}</p>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
