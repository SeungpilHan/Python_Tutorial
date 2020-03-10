(function(t){function e(e){for(var o,a,r=e[0],u=e[1],l=e[2],c=0,p=[];c<r.length;c++)a=r[c],i[a]&&p.push(i[a][0]),i[a]=0;for(o in u)Object.prototype.hasOwnProperty.call(u,o)&&(t[o]=u[o]);d&&d(e);while(p.length)p.shift()();return s.push.apply(s,l||[]),n()}function n(){for(var t,e=0;e<s.length;e++){for(var n=s[e],o=!0,a=1;a<n.length;a++){var u=n[a];0!==i[u]&&(o=!1)}o&&(s.splice(e--,1),t=r(r.s=n[0]))}return t}var o={},i={app:0},s=[];function a(t){return r.p+"js/"+({about:"about"}[t]||t)+"."+{about:"046e7186"}[t]+".js"}function r(e){if(o[e])return o[e].exports;var n=o[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.e=function(t){var e=[],n=i[t];if(0!==n)if(n)e.push(n[2]);else{var o=new Promise(function(e,o){n=i[t]=[e,o]});e.push(n[2]=o);var s,u=document.getElementsByTagName("head")[0],l=document.createElement("script");l.charset="utf-8",l.timeout=120,r.nc&&l.setAttribute("nonce",r.nc),l.src=a(t),s=function(e){l.onerror=l.onload=null,clearTimeout(c);var n=i[t];if(0!==n){if(n){var o=e&&("load"===e.type?"missing":e.type),s=e&&e.target&&e.target.src,a=new Error("Loading chunk "+t+" failed.\n("+o+": "+s+")");a.type=o,a.request=s,n[1](a)}i[t]=void 0}};var c=setTimeout(function(){s({type:"timeout",target:l})},12e4);l.onerror=l.onload=s,u.appendChild(l)}return Promise.all(e)},r.m=t,r.c=o,r.d=function(t,e,n){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},r.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)r.d(n,o,function(e){return t[e]}.bind(null,o));return n},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="/vuejs-todo/",r.oe=function(t){throw console.error(t),t};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=e,u=u.slice();for(var c=0;c<u.length;c++)e(u[c]);var d=l;s.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"56d7":function(t,e,n){"use strict";n.r(e);n("cadf"),n("551c"),n("097d");var o=n("2b0e"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container py-5",attrs:{id:"app"}},[n("h1",{staticClass:"fs-h1 text-center"},[t._v("\n\t\tVuejs Todo app\n\t")]),n("div",{staticClass:"nav text-center mt-3"},[n("router-link",{attrs:{to:"/"}},[t._v("Todos")]),n("router-link",{attrs:{to:"/about"}},[t._v("About")])],1),n("div",{staticClass:"main-content mt-5"},[n("router-view")],1)])},s=[],a=n("2877"),r={},u=Object(a["a"])(r,i,s,!1,null,null,null);u.options.__file="App.vue";var l=u.exports,c=n("8c4f"),d=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"ani-slideInDown row justify-content-center"},[n("div",{staticClass:"col-lg-6"},[n("ToDoInput",{on:{eventAddNewTask:t.onAddNewTask}}),n("ul",{staticClass:"list mt-3"},t._l(t.itemList,function(e){return n("ListItem",{key:e.id,attrs:{text:e.text,id:e.id,isDone:e.isDone},on:{eventTaskStatusChange:t.onTaskStatusChange,eventTaskDelete:t.onTaskDelete}})}))],1)])},p=[],f=(n("20d6"),n("7514"),function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("form",{on:{submit:t.onAddNewTask}},[n("input",{directives:[{name:"model",rawName:"v-model",value:t.text,expression:"text"}],attrs:{type:"text",placeholder:"What needs to be done?",required:""},domProps:{value:t.text},on:{input:function(e){e.target.composing||(t.text=e.target.value)}}})])}),m=[],h={name:"ToDoInput",data:function(){return{text:""}},methods:{onAddNewTask:function(t){t.preventDefault();var e=this.text;this.$emit("eventAddNewTask",e),this.text=""}}},v=h,g=Object(a["a"])(v,f,m,!1,null,null,null);g.options.__file="ToDoInput.vue";var b=g.exports,T=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("li",{staticClass:"list-item",class:{done:t.isDone}},[n("input",{staticClass:"checkbox",attrs:{type:"checkbox",id:t.idComputed},domProps:{checked:t.isDone},on:{change:t.onTaskStatusChange}}),n("label",{staticClass:"mr-3",attrs:{for:t.idComputed}}),n("span",{staticClass:"text"},[t._v("\n            "+t._s(t.text)+"\n        ")]),n("span",{staticClass:"icon-delete",on:{click:t.onTaskDelete}})])},k=[],x=(n("c5f6"),{name:"ListItem",props:{id:{type:Number,default:0},text:{type:String,default:""},isDone:{type:Boolean,default:!1}},computed:{idComputed:function(){return"item-".concat(this.id)}},methods:{onTaskStatusChange:function(t){var e=t.target.checked;this.$emit("eventTaskStatusChange",this.id,e)},onTaskDelete:function(t){this.$emit("eventTaskDelete",this.id)}}}),y=x,_=Object(a["a"])(y,T,k,!1,null,null,null);_.options.__file="ListItem.vue";var w=_.exports,C={name:"home",components:{ToDoInput:b,ListItem:w},data:function(){return{itemList:[]}},methods:{onAddNewTask:function(t){var e={id:(new Date).getTime(),text:t,isDone:!1};this.itemList.push(e)},onTaskStatusChange:function(t,e){console.log(t,e);var n=this.itemList.find(function(e){return e.id==t});n&&(n.isDone=e),console.log(this.itemList)},onTaskDelete:function(t){console.log(t);var e=this.itemList.findIndex(function(e){return e.id==t});e>-1&&this.itemList.splice(e,1),console.log(this.itemList)},loadItemList:function(){this.itemList=JSON.parse(localStorage.getItem("VuejsTodo"))||[],console.log("this.itemList =",this.itemList)},updateItemList:function(){localStorage.setItem("VuejsTodo",JSON.stringify(this.itemList))}},mounted:function(){this.loadItemList()},watch:{itemList:{handler:function(t){console.log("item changed"),this.updateItemList()},deep:!0}}},L=C,D=Object(a["a"])(L,d,p,!1,null,null,null);D.options.__file="Home.vue";var j=D.exports;o["a"].use(c["a"]);var I=new c["a"]({routes:[{path:"/",name:"home",component:j},{path:"/about",name:"about",component:function(){return n.e("about").then(n.bind(null,"f820"))}}]});n("dc44");o["a"].config.productionTip=!1,new o["a"]({router:I,render:function(t){return t(l)}}).$mount("#app")},dc44:function(t,e,n){}});
//# sourceMappingURL=app.f86b5f8d.js.map