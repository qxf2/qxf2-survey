(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{127:function(e,t,a){e.exports=a(262)},132:function(e,t,a){},133:function(e,t,a){},157:function(e,t,a){},165:function(e,t){},262:function(e,t,a){"use strict";a.r(t);var n=a(0),l=a.n(n),r=a(104),o=a.n(r),c=(a(132),a(36)),s=a(5),u=(a(133),function(){return l.a.createElement("nav",null,l.a.createElement("ul",null,l.a.createElement("li",null,l.a.createElement(c.b,{to:"/"},"Survey")),l.a.createElement("li",null,l.a.createElement(c.b,{to:"/dashboard"},"Dashboard")),l.a.createElement("li",null,l.a.createElement(c.b,{to:"/admin"},"Admin"))))}),i=function(){return l.a.createElement("div",{style:{backgroundColor:"white",position:"absolute",top:0,bottom:0,left:0,right:0}},l.a.createElement("div",{style:{position:"absolute",top:"50%",left:"50%",height:"150px",width:"500px",margin:"-75px 0 0 -250px",padding:"20px",fontFamily:"Arial",fontSize:"75px",textAlign:"center",textTransform:"uppercase",textShadow:"0 0 80px red, 0 0 30px FireBrick, 0 0 6px DarkRed",color:"red"}},l.a.createElement("p",{style:{color:"#fff",textShadow:"0 0 80px #ffffff, 0 0 30px #008000, 0 0 6px #0000ff"}},"error"),l.a.createElement("p",{id:"code"},"404")))},m=a(58),d=a(8),p=a(121),f=a(75),h=(a(138),a(118)),E=(a(139),a(120)),g=a(4),b=a.n(g),v="https://survey-backend.qxf2.com";b.a.defaults.headers.common.User="qxf2";var y=[];b.a.get("".concat(v,"/survey/admin/employees")).then((function(e){for(var t in e.data)"y"===e.data[t].status.toLowerCase()&&"test@qxf2.com"!==e.data[t].email?y.push({label:e.data[t].fullName,value:e.data[t].email}):"y"===e.data[t].status.toLowerCase()&&"test@qxf2.com"===e.data[t].email&&y.push({label:"External",value:"dummy@qxf2.com"})})).catch((function(e){console.log(e.response)}));var x=y,S=x;var w=function(e){var t=e.setState,a=Object(p.a)(e,["setState"]),r=l.a.useState([]),o=Object(d.a)(r,2),c=o[0],s=o[1],u=l.a.useState([]),i=Object(d.a)(u,2),m=i[0],g=i[1],b=l.a.useState([]),v=Object(d.a)(b,2),y=v[0],x=v[1];return Object(n.useEffect)((function(){t("selectedHelp",c)}),[c,t]),Object(n.useEffect)((function(){t("tags",m)}),[m,t]),Object(n.useEffect)((function(){t("selectedHelped",y)}),[y,t]),l.a.createElement("div",null,l.a.createElement("div",{className:"form-group"},l.a.createElement("h3",null,"Enter Email ID"),l.a.createElement("input",{name:"email",type:"email",onChange:a.handleChange,className:"form-control"})),l.a.createElement("div",{className:"new-tech"},l.a.createElement("h3",null,"What new technologies did you learn this week?",l.a.createElement("sub",{id:"reference"},l.a.createElement("a",{href:"https://wiki.qxf2.com/home/r-d/newbie-orientation/what-technologies-did-you-work-on-this-week"},"Help"))),l.a.createElement(h.a,{tags:m,onChange:function(e){return g(e)}}),l.a.createElement("br",null)),l.a.createElement("div",{className:"who-helped"},l.a.createElement("h3",null,"Who helped you this week?",l.a.createElement("sub",{id:"reference"},l.a.createElement("a",{href:"https://wiki.qxf2.com/home/r-d/newbie-orientation/helping-others"},"Help"))),l.a.createElement(f.a,{options:S,value:c,onChange:s,labelledBy:"Select"}),l.a.createElement("br",null)),l.a.createElement("div",{className:"whom-did-you-help"},l.a.createElement("h3",null,"Whom did you help this week?",l.a.createElement("sub",{id:"reference"},l.a.createElement("a",{href:"https://wiki.qxf2.com/home/r-d/newbie-orientation/helping-others"},"Help"))),l.a.createElement(f.a,{options:S,value:y,onChange:x,labelledBy:"Select"}),l.a.createElement("br",null)),l.a.createElement("div",{className:"col-md-4 offset-md-4"},l.a.createElement(E.a,{variant:"primary",size:"lg",block:!0,button:"true",disabled:a.step.isLast(),onClick:a.next},"Submit")))};b.a.defaults.headers.common.User="qxf2";var O=function(e){var t=e.state.email,a=e.state.tags.toString(),r=JSON.parse(JSON.stringify(e.state.selectedHelp)),o=JSON.parse(JSON.stringify(e.state.selectedHelped)),c=Object(n.useState)([]),s=Object(d.a)(c,2),u=s[0],i=s[1],m=Object(n.useState)(!0),p=Object(d.a)(m,2),f=p[0],h=p[1];return Object(n.useEffect)((function(){i(x),h(!1)}),[]),function(){if(!1===f){if(!0===function(){var e=!1,a=0;for(a=0;a<=u.length-1;a++)if(u[a].value===t){e=!0;break}return e}()){var e={userMail:t,listHelp:r,listHelped:o,listTags:a};return""!==e?b.a.post("".concat(v,"/survey/response"),{data:e}).then((function(t){console.log(e),console.log("Post request: Success")})).catch((function(e){console.log("Post request: Failed"),console.log(e.response)})):alert("Could not pass empty data"),l.a.createElement("div",{className:"jumbotron text-center"},l.a.createElement("h1",{className:"display-3"},"Thank You!"),l.a.createElement("p",{className:"lead"},l.a.createElement("strong",null,"Here is what we recorded!")),l.a.createElement("p",null,l.a.createElement("b",null,"E-mail:")," ",t),l.a.createElement("p",null,l.a.createElement("b",null,"Who helped you?:")," ",r.map((function(e){return e.label})).join(", ")),l.a.createElement("p",null,l.a.createElement("b",null,"Whom did you help?:")," ",o.map((function(e){return e.label})).join(", ")," "),l.a.createElement("p",null,l.a.createElement("b",null,"Tags:")," ",a," "))}return l.a.createElement("div",{className:"jumbotron text-center"},l.a.createElement("p",{className:"lead"},l.a.createElement("strong",null,"Please enter valid email")))}return l.a.createElement("span",null,"Loading.....")}()};var j=function(){return l.a.createElement("div",{className:"App"},l.a.createElement(m.b,null,l.a.createElement(m.a,{component:w}),l.a.createElement(m.a,{component:O})))},k=a(27),N=a.n(k),q=a(73),C=a(43),_=(a(157),"361336870916-q88h5gho5ee7p1mudg32je26th6pjlv5.apps.googleusercontent.com");function L(e){var t=e.Login,a=Object(n.useState)(!0),r=Object(d.a)(a,2),o=r[0],c=r[1],s=Object(n.useState)(!1),u=Object(d.a)(s,2),i=u[0],m=u[1],p=Object(n.useState)(!1),f=Object(d.a)(p,2),h=f[0],E=f[1],g=Object(n.useState)(null),b=Object(d.a)(g,2),y=b[0],x=b[1];return l.a.createElement("div",{className:"g-signin"},o?l.a.createElement("h3",null,"Sign in with Google"):null,o?l.a.createElement(C.GoogleLogin,{clientId:_,buttonText:"Sign In",onSuccess:function(e){var a=e.getAuthResponse().id_token;x(e.profileObj.email),c(!1);var n=new XMLHttpRequest;n.open("POST","".concat(v,"/survey/admin/admin-login")),n.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),n.setRequestHeader("User","qxf2"),n.onload=function(){if(200===n.status){t(!0,e.profileObj.email)}else E(!0)},n.send("idtoken="+a),m(!0)},onFailure:function(e){console.log("Login Failed:",e)},cookiePolicy:"single_host_origin",isSignedIn:!0}):null,h?l.a.createElement("span",null,"Logged in as ",y,l.a.createElement("br",null)," ",l.a.createElement("h5",null,"You are Unauthorized to view this page")):null,i?l.a.createElement(C.GoogleLogout,{clientId:_,buttonText:"Sign Out",onLogoutSuccess:function(){alert("You have been logged out successfully"),console.clear(),c(!0),m(!1),E(!1)}}):null)}b.a.defaults.headers.common.User="qxf2";var H=function(){var e="".concat(v,"/survey/admin/employees"),t=Object(n.useState)([]),a=Object(d.a)(t,2),r=a[0],o=a[1],c=function(){var t=Object(q.a)(N.a.mark((function t(){var a;return N.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,b.a.get(e);case 2:a=t.sent,o(a.data);case 4:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();Object(n.useEffect)((function(){c()}),[]);return l.a.createElement("div",null,l.a.createElement("h1",{id:"title"},"Employee Table"),l.a.createElement("table",{id:"employees"},l.a.createElement("tbody",null,l.a.createElement("tr",null,["ID","first_name","last_name","active_flag","email"].map((function(e,t){return l.a.createElement("th",{key:t},e.toUpperCase())}))),r&&r.map((function(e){var t=e.ID,a=e.firstName,n=e.lastName,r=e.status,o=e.email;return l.a.createElement("tr",{key:o},l.a.createElement("td",null,t),l.a.createElement("td",null,a),l.a.createElement("td",null,n),l.a.createElement("td",null,r),l.a.createElement("td",null,o))})))),l.a.createElement("br",null))},B=function(){var e="".concat(v,"/survey/admin/not_responded_users"),t=Object(n.useState)([]),a=Object(d.a)(t,2),r=a[0],o=a[1],c=function(){var t=Object(q.a)(N.a.mark((function t(){var a;return N.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,b.a.get(e);case 2:a=t.sent,o(a.data);case 4:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();Object(n.useEffect)((function(){c()}),[]);return l.a.createElement("div",null,l.a.createElement("h1",{id:"title"},"Employees yet to Respond"),l.a.createElement("table",{id:"employees"},l.a.createElement("tbody",null,l.a.createElement("tr",null,["Name","email"].map((function(e,t){return l.a.createElement("th",{key:t},e.toUpperCase())}))),r&&r.map((function(e){var t=e.firstName,a=e.lastName,n=e.email;return l.a.createElement("tr",{key:n},l.a.createElement("td",null,t," ",a),l.a.createElement("td",null,n))})))),l.a.createElement("br",null))},D=function(){var e=l.a.useState(!1),t=Object(d.a)(e,2),a=t[0],n=t[1],r=l.a.useState(null),o=Object(d.a)(r,2),c=o[0],s=o[1];return l.a.createElement("div",{className:"App"},!0===a?l.a.createElement(l.a.Fragment,null,l.a.createElement("br",null),l.a.createElement("span",{style:{float:"right",marginRight:"-350px"}},l.a.createElement("p",{style:{float:"center"}},"Logged in as ",c),l.a.createElement(C.GoogleLogout,{clientId:"361336870916-q88h5gho5ee7p1mudg32je26th6pjlv5.apps.googleusercontent.com",buttonText:"Sign Out",onLogoutSuccess:function(){alert("You have been logged out successfully"),console.clear(),n(!1)}})),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(H,null),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(B,null)):l.a.createElement(L,{Login:function(e,t){!0===e&&(n(!0),s(t))}}))},U=a(117),F=(a(166),a(167),a(74));b.a.defaults.headers.common.User="qxf2";var T=[],A=[];b.a.get("".concat(v,"/survey/admin/symmetry-score")).then((function(e){for(var t in e.data.employee_name)A.push(e.data.employee_name[t]);for(var a in e.data.data)T.push(e.data.data[a])})).catch((function(e){console.log(e.response)}));var I={labels:A,datasets:[{label:"Symmetry Score",backgroundColor:"LightBlue",borderColor:"black",borderWidth:1,hoverBackgroundColor:"blue",hoverBorderColor:"black",data:T}]};b.a.defaults.headers.common.User="qxf2";var W=[],R=[];b.a.get("".concat(v,"/survey/admin/overall_response")).then((function(e){for(var t in e.data.name)R.push(e.data.name[t]);for(var a in e.data.response_data)W.push(e.data.response_data[a])})).catch((function(e){console.log(e.response)}));var J={labels:R,datasets:[{label:"Overall Response",backgroundColor:"LightBlue",borderColor:"black",borderWidth:1,hoverBackgroundColor:"blue",hoverBorderColor:"black",data:W}]};b.a.defaults.headers.common.User="qxf2";var P=[],Y=[],z=new Date,M=new Date(z);M.setDate(M.getDate()-90);var G="".concat(M.getFullYear(),"-").concat(M.getMonth()+1,"-").concat(M.getDate()),Q="".concat(z.getFullYear(),"-").concat(z.getMonth()+1,"-").concat(z.getDate()),X={start_date:G.toLocaleString(),end_date:Q.toLocaleString()},$=JSON.stringify(X);b.a.post("".concat(v,"/survey/admin/QElo_filter_technology"),$).then((function(e){for(var t in e.data)P.push(e.data[t].technology);for(var a=P.length,n=Array.from({length:a},(function(e,t){return!1})),l=0;l<a;l++)if(!0!==n[l]){for(var r=1,o=l+1;o<a;o++)P[l]===P[o]&&(n[o]=!0,r++);Y.push({text:P[l],value:r})}})).catch((function(e){console.log("Post request: Failed"),console.log(e.response)}));var K=Y,V=a(270);b.a.defaults.headers.common.User="qxf2";var Z=I,ee=J,te=K,ae=function(){var e=[],t=[],a=[],r=[],o=Object(n.useState)(!1),c=Object(d.a)(o,2),s=c[0],u=c[1];return b.a.get("".concat(v,"/survey/admin/overall_response")).then((function(a){for(var n in a.data.name)t.push(a.data.name[n]);for(var l in a.data.response_data)e.push(a.data.response_data[l])})).catch((function(e){console.log(e.response)})),b.a.get("".concat(v,"/survey/admin/symmetry-score")).then((function(e){for(var t in e.data.employee_name)a.push(e.data.employee_name[t]);for(var n in e.data.data)r.push(e.data.data[n]);u(!0)})).catch((function(e){console.log(e.response)})),l.a.createElement("div",null,s?l.a.createElement(l.a.Fragment,null,l.a.createElement("h2",null,"Survey Analysis Dashboard"),l.a.createElement("div",{style:{backgroundColor:"#efefef",height:"300px",width:"100%"}},l.a.createElement(U.a,{words:te})),l.a.createElement("div",null,l.a.createElement("h2",null,"Symmetry Score"),l.a.createElement(F.HorizontalBar,{data:Z})),l.a.createElement("div",null,l.a.createElement("h2",null,"Overall Data"),l.a.createElement(F.HorizontalBar,{data:ee}))):l.a.createElement(V.a,{animation:"border"}))};var ne=function(){return l.a.createElement(c.a,null,l.a.createElement("div",{className:"App"},l.a.createElement(u,null),l.a.createElement("div",{id:"page-body"},l.a.createElement(s.c,null,l.a.createElement(s.a,{path:"/",component:j,exact:!0}),l.a.createElement(s.a,{path:"/survey",component:j}),l.a.createElement(s.a,{path:"/admin",component:D}),l.a.createElement(s.a,{path:"/dashboard",component:ae}),l.a.createElement(s.a,{component:i})))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(l.a.createElement(l.a.StrictMode,null,l.a.createElement(ne,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[127,1,2]]]);
//# sourceMappingURL=main.3e4a3da1.chunk.js.map