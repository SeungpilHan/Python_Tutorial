module.exports = {
  head: {
      title: 'NodeBird',
  },
  modules: [
    '@nuxtjs/vuetify',
    '@nuxtjs/axios' //중복이 생기지 않게 해준다.
  ],
  plugins: [], //모든 페이지에 적용시켜줌
  vuetify: {},
};