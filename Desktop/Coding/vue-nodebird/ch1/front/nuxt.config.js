module.exports = {
  head: {
      title: 'NodeBird',
  },
  modules: [  
    '@nuxtjs/axios' //중복이 생기지 않게 해준다.
  ],
  buildModules: [
    '@nuxtjs/vuetify',
  ],
  vuetify: {},
};