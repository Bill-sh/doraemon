"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[799],{80226:function(U,g,e){e.r(g),e.d(g,{default:function(){return O}});var x=e(17061),r=e.n(x),y=e(17156),h=e.n(y),j=e(27424),C=e.n(j),T=e(42122),A=e.n(T),B="https://service-kq8occro-1303058007.gz.apigw.tencentcs.com/release/",S=e(9927);function F(s){return l.apply(this,arguments)}function l(){return l=h()(r()().mark(function s(u){return r()().wrap(function(a){for(;;)switch(a.prev=a.next){case 0:return a.abrupt("return",(0,S.request)("".concat(B,"/auth/"),A()({method:"GET"},u||{})));case 1:case"end":return a.stop()}},s)})),l.apply(this,arguments)}var Z=e(87547),E=e(94149),I=e(26),m=e(5966),P=e(63434),v=e(49053),G=e(54689),L=e(67294),n=e(85893),O=function(){var s=(0,L.useState)("account"),u=C()(s,2),i=u[0],a=u[1];return(0,n.jsx)("div",{style:{backgroundColor:"white",height:"calc(100vh - 48px)",margin:-24},children:(0,n.jsxs)(I.B,{backgroundImageUrl:"https://login.sufe.edu.cn/login/img/BG_1.png",logo:"https://login.sufe.edu.cn/oss/public/file/4023af54770ac3c4dd153fcf5e054a39021148d6ee59dee72426c0145ddedcdac37436ae1994611bad42ad37276e279f5ee5b13d29cd3d716b12e80faf151e7ffccca91c91cdbe0bf6681f35efd49da2?_=0.2574402783172467",title:"\u5B66\u751F\u7BA1\u7406\u5E73\u53F0",subTitle:"\u5168\u7403\u6700\u4E13\u5C5E\u7684\u5E73\u53F0",onFinish:function(){var c=h()(r()().mark(function o(z){var d,p,f;return r()().wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,F({params:z});case 2:return d=t.sent,p=d.token,f=d.user,window.localStorage.setItem("token",p),window.localStorage.setItem("name",f.name),window.localStorage.setItem("groups",f.groups),window.location.assign("/"),t.abrupt("return",!0);case 10:case"end":return t.stop()}},o)}));return function(o){return c.apply(this,arguments)}}(),children:[(0,n.jsx)(v.Z,{centered:!0,activeKey:i,onChange:function(o){return a(o)},children:(0,n.jsx)(v.Z.TabPane,{tab:"\u8D26\u53F7\u5BC6\u7801\u767B\u5F55"},"account")}),i==="account"&&(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(m.Z,{name:"username",initialValue:"Oyan",fieldProps:{size:"large",prefix:(0,n.jsx)(Z.Z,{className:"prefixIcon"})},placeholder:"\u7528\u6237\u540D: Oyan",rules:[{required:!0,message:"\u8BF7\u8F93\u5165\u7528\u6237\u540D!"}]}),(0,n.jsx)(m.Z.Password,{name:"password",fieldProps:{size:"large",prefix:(0,n.jsx)(E.Z,{className:"prefixIcon"})},placeholder:"\u5BC6\u7801: \u4F60\u77E5\u9053\u7684",rules:[{required:!0,message:"\u8BF7\u8F93\u5165\u5BC6\u7801\uFF01"}]})]}),(0,n.jsxs)("div",{style:{marginBlockEnd:24},children:[(0,n.jsx)(P.Z,{noStyle:!0,name:"autoLogin",initialValue:!0,children:"\u81EA\u52A8\u767B\u5F55"}),(0,n.jsx)("a",{style:{float:"right"},onClick:function(){G.Z.open({message:"\u5FD8\u8BB0\u5BC6\u7801\u4E86\uFF1F",description:"\u6253\u7535\u8BDD\u7ED9\u7BA1\u7406\u5458\u8FDB\u884C\u91CD\u7F6E"})},children:"\u5FD8\u8BB0\u5BC6\u7801"})]})]})})}}}]);