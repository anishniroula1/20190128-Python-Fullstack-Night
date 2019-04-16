// randanimal.js
let app = new Vue({
  el: '#app',
  mounted: function(){
    this.getCat()
  },
  data: {
    catImg: null
  },
  methods: {
    getCat: async function() {
      try {
        const res = await fetch('https://aws.random.cat/meow')
        const json = await res.json()
        this.catImg = json.file
      } catch(err) {
        console.log(err)
      }
    }
  },
})