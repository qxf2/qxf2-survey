(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{129:function(e,t,a){e.exports=a(264)},134:function(e,t,a){},135:function(e,t,a){},159:function(e,t,a){},167:function(e,t){},264:function(e,t,a){"use strict";a.r(t);var n=a(0),l=a.n(n),r=a(107),o=a.n(r),c=(a(134),a(36)),s=a(5),m=(a(135),function(){return l.a.createElement("nav",null,l.a.createElement("ul",null,l.a.createElement("li",null,l.a.createElement(c.b,{to:"/"},"Survey")),l.a.createElement("li",null,l.a.createElement(c.b,{to:"/dashboard"},"Dashboard")),l.a.createElement("li",null,l.a.createElement(c.b,{to:"/admin"},"Admin"))))}),u=function(){return l.a.createElement("div",{style:{backgroundColor:"white",position:"absolute",top:0,bottom:0,left:0,right:0}},l.a.createElement("div",{style:{position:"absolute",top:"50%",left:"50%",height:"150px",width:"500px",margin:"-75px 0 0 -250px",padding:"20px",fontFamily:"Arial",fontSize:"75px",textAlign:"center",textTransform:"uppercase",textShadow:"0 0 80px red, 0 0 30px FireBrick, 0 0 6px DarkRed",color:"red"}},l.a.createElement("p",{style:{color:"#fff",textShadow:"0 0 80px #ffffff, 0 0 30px #008000, 0 0 6px #0000ff"}},"error"),l.a.createElement("p",{id:"code"},"404")))},i=a(60),d=a(6),p=a(123),f=a(78),h=(a(140),a(121)),E=(a(141),a(59)),g=a(3),b=a.n(g),v="http://15.206.119.69:8000";b.a.defaults.headers.common.User="qxf2";var y=[];b.a.get("".concat(v,"/survey/admin/employees")).then((function(e){for(var t in e.data)"y"===e.data[t].status.toLowerCase()&&y.push({label:e.data[t].fullName,value:e.data[t].email})})).catch((function(e){console.log(e.response)}));var S=y;var O=function(e){var t=e.setState,a=Object(p.a)(e,["setState"]),r=l.a.useState([]),o=Object(d.a)(r,2),c=o[0],s=o[1],m=l.a.useState([]),u=Object(d.a)(m,2),i=u[0],g=u[1],b=l.a.useState([]),v=Object(d.a)(b,2),y=v[0],O=v[1];return Object(n.useEffect)((function(){t("selectedHelp",c)}),[c,t]),Object(n.useEffect)((function(){t("tags",i)}),[i,t]),Object(n.useEffect)((function(){t("selectedHelped",y)}),[y,t]),l.a.createElement("div",null,l.a.createElement("div",{className:"form-group"},l.a.createElement("h3",null,"Enter Email ID"),l.a.createElement("input",{name:"email",type:"email",onChange:a.handleChange,className:"form-control"})),l.a.createElement("div",{className:"new-tech"},l.a.createElement("h3",null,"What new technologies did you learn this week?",l.a.createElement("sub",{id:"reference"},l.a.createElement("a",{href:"https://wiki.qxf2.com/home/r-d/newbie-orientation/what-technologies-did-you-work-on-this-week"},"Help"))),l.a.createElement(h.a,{tags:i,onChange:function(e){return g(e)}}),l.a.createElement("br",null)),l.a.createElement("div",{className:"who-helped"},l.a.createElement("h3",null,"Who helped you this week?",l.a.createElement("sub",{id:"reference"},l.a.createElement("a",{href:"https://wiki.qxf2.com/home/r-d/newbie-orientation/helping-others"},"Help"))),l.a.createElement(f.a,{options:S,value:c,onChange:s,labelledBy:"Select"}),l.a.createElement("br",null)),l.a.createElement("div",{className:"whom-did-you-help"},l.a.createElement("h3",null,"Whom did you help this week?",l.a.createElement("sub",{id:"reference"},l.a.createElement("a",{href:"https://wiki.qxf2.com/home/r-d/newbie-orientation/helping-others"},"Help"))),l.a.createElement(f.a,{options:S,value:y,onChange:O,labelledBy:"Select"}),l.a.createElement("br",null)),l.a.createElement("div",{className:"col-md-4 offset-md-4"},l.a.createElement(E.a,{variant:"primary",size:"lg",block:!0,button:"true",disabled:a.step.isLast(),onClick:a.next},"Submit")))};b.a.defaults.headers.common.User="qxf2";var j=function(e){var t=e.state.email,a=e.state.tags.toString(),r=JSON.parse(JSON.stringify(e.state.selectedHelp)),o=JSON.parse(JSON.stringify(e.state.selectedHelped)),c=Object(n.useState)([]),s=Object(d.a)(c,2),m=s[0],u=s[1],i=Object(n.useState)(!0),p=Object(d.a)(i,2),f=p[0],h=p[1];return Object(n.useEffect)((function(){b.a.get("".concat(v,"/survey/admin/employees")).then((function(e){u(e.data),h(!1)}))}),[]),function(){if(!1===f){if(!0===function(){var e=!1,a=0;for(a=0;a<=m.length-1;a++)if(m[a].email===t){e=!0;break}return e}()){var e={userMail:t,listHelp:r,listHelped:o,listTags:a};return""!==e?b.a.post("".concat(v,"/survey/response"),{data:e}).then((function(t){console.log(e),console.log("Post request: Success")})).catch((function(e){console.log("Post request: Failed"),console.log(e.response)})):alert("Could not pass empty data"),l.a.createElement("div",{className:"jumbotron text-center"},l.a.createElement("h1",{className:"display-3"},"Thank You!"),l.a.createElement("p",{className:"lead"},l.a.createElement("strong",null,"Here is what we recorded!")),l.a.createElement("p",null,l.a.createElement("b",null,"E-mail:")," ",t),l.a.createElement("p",null,l.a.createElement("b",null,"Who helped you?:")," ",r.map((function(e){return e.label})).join(", ")),l.a.createElement("p",null,l.a.createElement("b",null,"Whom did you help?:")," ",o.map((function(e){return e.label})).join(", ")," "),l.a.createElement("p",null,l.a.createElement("b",null,"Tags:")," ",a," "))}return l.a.createElement("div",{className:"jumbotron text-center"},l.a.createElement("p",{className:"lead"},l.a.createElement("strong",null,"Please enter valid email")))}return l.a.createElement("span",null,"Loading.....")}()};var x=function(){return l.a.createElement("div",{className:"App"},l.a.createElement(i.b,null,l.a.createElement(i.a,{component:O}),l.a.createElement(i.a,{component:j})))},w=a(27),N=a.n(w),k=a(75),C=a(53),_=a(76),q=a(43),L=(a(159),"361336870916-q88h5gho5ee7p1mudg32je26th6pjlv5.apps.googleusercontent.com");function F(e){var t=e.Login,a=Object(n.useState)(!0),r=Object(d.a)(a,2),o=r[0],c=r[1],s=Object(n.useState)(!1),m=Object(d.a)(s,2),u=m[0],i=m[1],p=Object(n.useState)(!1),f=Object(d.a)(p,2),h=f[0],E=f[1],g=Object(n.useState)(null),b=Object(d.a)(g,2),y=b[0],S=b[1];return l.a.createElement("div",{className:"g-signin"},o?l.a.createElement("h3",null,"Sign in with Google"):null,o?l.a.createElement(q.GoogleLogin,{clientId:L,buttonText:"Sign In",onSuccess:function(e){var a=e.getAuthResponse().id_token;S(e.profileObj.email),c(!1);var n=new XMLHttpRequest;n.open("POST","".concat(v,"/survey/admin/admin-login")),n.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),n.setRequestHeader("User","qxf2"),n.onload=function(){if(200===n.status){t(!0,e.profileObj.email)}else E(!0)},n.send("idtoken="+a),i(!0)},onFailure:function(e){console.log("Login Failed:",e)},cookiePolicy:"single_host_origin",isSignedIn:!0}):null,h?l.a.createElement("span",null,"Logged in as ",y,l.a.createElement("br",null)," ",l.a.createElement("h5",null,"You are Unauthorized to view this page")):null,u?l.a.createElement(q.GoogleLogout,{clientId:L,buttonText:"Sign Out",onLogoutSuccess:function(){alert("You have been logged out successfully"),console.clear(),c(!0),i(!1),E(!1)}}):null)}b.a.defaults.headers.common.User="qxf2";var H=function(){var e=l.a.useState([]),t=Object(d.a)(e,2),a=t[0],r=t[1],o=l.a.useState([]),c=Object(d.a)(o,2),s=c[0],m=c[1];Object(n.useEffect)((function(){b.a.get("".concat(v,"/survey/admin/employees")).then((function(e){m(e.data)}))}),[]);var u=function(e){r(Object(_.a)(Object(_.a)({},a),{},Object(C.a)({},e.target.name,e.target.value.trim())))},i={firstName:a["employee-first-name-input"],lastName:a["employee-last-name-input"],email:a["email-input"],fullName:a["employee-first-name-input"]+" "+a["employee-last-name-input"],status:a["status-input"]};return l.a.createElement("div",{className:"panel panel-primary"},l.a.createElement("div",{className:"panel-heading"},l.a.createElement("h3",{className:"panel-title"},l.a.createElement("strong",null,"Add Employee"))),l.a.createElement("div",{className:"panel-body"},l.a.createElement("form",null,l.a.createElement("div",{className:"form-group"},l.a.createElement("label",{htmlFor:"employee-first-name-input"},"First Name"),l.a.createElement("input",{className:"form-control",name:"employee-first-name-input",type:"text",onChange:u})),l.a.createElement("div",{className:"form-group"},l.a.createElement("label",{htmlFor:"employee-last-name-input"},"Last Name"),l.a.createElement("input",{className:"form-control",name:"employee-last-name-input",type:"text",onChange:u})),l.a.createElement("div",{className:"form-group"},l.a.createElement("label",{htmlFor:"email-input"},"E-Mail"),l.a.createElement("input",{className:"form-control",name:"email-input",type:"text",onChange:u})),l.a.createElement("div",{className:"form-group"},l.a.createElement("label",{htmlFor:"status-input"},"Employee Status (Y/N)"),l.a.createElement("input",{className:"form-control",name:"status-input",type:"text",onChange:u})),l.a.createElement("div",{className:"col-md-4 offset-md-4"},l.a.createElement(E.a,{variant:"primary",size:"lg",block:!0,onClick:function(e){if(e.preventDefault(),""!==a){var t=!1,n=0;for(n=0;n<=s.length-1;n++)if(s[n].email===i.email){t=!0;break}!1===t?b.a.post("".concat(v,"/survey/admin/new_employee"),{data:i}).then((function(e){console.log("Post request: Success")})).catch((function(e){console.log("Post request: Failed"),console.log(e.response)})):alert("Email already exists")}}},"Submit")))))},D=function(){var e="".concat(v,"/survey/admin/employees"),t=Object(n.useState)([]),a=Object(d.a)(t,2),r=a[0],o=a[1],c=function(){var t=Object(k.a)(N.a.mark((function t(){var a;return N.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,b.a.get(e);case 2:a=t.sent,o(a.data);case 4:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();Object(n.useEffect)((function(){c()}),[]);return l.a.createElement("div",null,l.a.createElement("h1",{id:"title"},"Employee Table"),l.a.createElement("table",{id:"employees"},l.a.createElement("tbody",null,l.a.createElement("tr",null,["ID","first_name","last_name","active_flag","email"].map((function(e,t){return l.a.createElement("th",{key:t},e.toUpperCase())}))),r&&r.map((function(e){var t=e.ID,a=e.firstName,n=e.lastName,r=e.status,o=e.email;return l.a.createElement("tr",{key:t},l.a.createElement("td",null,t),l.a.createElement("td",null,a),l.a.createElement("td",null,n),l.a.createElement("td",null,r),l.a.createElement("td",null,o))})))),l.a.createElement("br",null))},B=function(){var e="".concat(v,"/survey/admin/not_responded_users"),t=Object(n.useState)([]),a=Object(d.a)(t,2),r=a[0],o=a[1],c=function(){var t=Object(k.a)(N.a.mark((function t(){var a;return N.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,b.a.get(e);case 2:a=t.sent,o(a.data);case 4:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();Object(n.useEffect)((function(){c()}),[]);return l.a.createElement("div",null,l.a.createElement("h1",{id:"title"},"Employees yet to Respond"),l.a.createElement("table",{id:"employees"},l.a.createElement("tbody",null,l.a.createElement("tr",null,["Name"].map((function(e,t){return l.a.createElement("th",{key:t},e.toUpperCase())}))),r&&r.map((function(e){var t=e.firstName,a=e.lastName;return l.a.createElement("tr",null,l.a.createElement("td",null,t," ",a))})))),l.a.createElement("br",null))},U=function(){var e=l.a.useState(!1),t=Object(d.a)(e,2),a=t[0],n=t[1],r=l.a.useState(null),o=Object(d.a)(r,2),c=o[0],s=o[1];return l.a.createElement("div",{className:"App"},!0===a?l.a.createElement(l.a.Fragment,null,l.a.createElement("br",null),l.a.createElement("span",{style:{float:"right",marginRight:"-350px"}},l.a.createElement("p",{style:{float:"center"}},"Logged in as ",c),l.a.createElement(q.GoogleLogout,{clientId:"361336870916-q88h5gho5ee7p1mudg32je26th6pjlv5.apps.googleusercontent.com",buttonText:"Sign Out",onLogoutSuccess:function(){alert("You have been logged out successfully"),console.clear(),n(!1)}})),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement(D,null),l.a.createElement(H,null),l.a.createElement(B,null)):l.a.createElement(F,{Login:function(e,t){!0===e&&(n(!0),s(t))}}))},A=a(120),T=(a(168),a(169),a(77));b.a.defaults.headers.common.User="qxf2";var I=[],W=[];b.a.get("".concat(v,"/survey/admin/symmetry-score")).then((function(e){for(var t in e.data.employee_name)W.push(e.data.employee_name[t]);for(var a in e.data.data)I.push(e.data.data[a])})).catch((function(e){console.log(e.response)}));var P={labels:W,datasets:[{label:"Symmetry Score",backgroundColor:"LightBlue",borderColor:"black",borderWidth:1,hoverBackgroundColor:"blue",hoverBorderColor:"black",data:I}]};b.a.defaults.headers.common.User="qxf2";var R=[],J=[];b.a.get("".concat(v,"/survey/admin/overall_response")).then((function(e){for(var t in e.data.name)J.push(e.data.name[t]);for(var a in e.data.response_data)R.push(e.data.response_data[a])})).catch((function(e){console.log(e.response)}));var Y={labels:J,datasets:[{label:"Overall Response",backgroundColor:"LightBlue",borderColor:"black",borderWidth:1,hoverBackgroundColor:"blue",hoverBorderColor:"black",data:R}]};b.a.defaults.headers.common.User="qxf2";var z=[],M=[],G=new Date,Q=new Date(G);Q.setDate(Q.getDate()-90);var X="".concat(Q.getFullYear(),"-").concat(Q.getMonth()+1,"-").concat(Q.getDate()),$="".concat(G.getFullYear(),"-").concat(G.getMonth()+1,"-").concat(G.getDate()),K={start_date:X.toLocaleString(),end_date:$.toLocaleString()},V=JSON.stringify(K);b.a.post("".concat(v,"/survey/admin/QElo_filter_technology"),V).then((function(e){for(var t in e.data)z.push(e.data[t].technology);for(var a=z.length,n=Array.from({length:a},(function(e,t){return!1})),l=0;l<a;l++)if(!0!==n[l]){for(var r=1,o=l+1;o<a;o++)z[l]===z[o]&&(n[o]=!0,r++);M.push({text:z[l],value:r})}})).catch((function(e){console.log("Post request: Failed"),console.log(e.response)}));var Z=M,ee=a(272);b.a.defaults.headers.common.User="qxf2";var te=P,ae=Y,ne=Z,le=function(){var e=[],t=[],a=[],r=[],o=Object(n.useState)(!1),c=Object(d.a)(o,2),s=c[0],m=c[1];return b.a.get("".concat(v,"/survey/admin/overall_response")).then((function(a){for(var n in a.data.name)t.push(a.data.name[n]);for(var l in a.data.response_data)e.push(a.data.response_data[l])})).catch((function(e){console.log(e.response)})),b.a.get("".concat(v,"/survey/admin/symmetry-score")).then((function(e){for(var t in e.data.employee_name)a.push(e.data.employee_name[t]);for(var n in e.data.data)r.push(e.data.data[n]);m(!0)})).catch((function(e){console.log(e.response)})),l.a.createElement("div",null,s?l.a.createElement(l.a.Fragment,null,l.a.createElement("h2",null,"Survey Analysis Dashboard"),l.a.createElement("div",{style:{backgroundColor:"#efefef",height:"300px",width:"100%"}},l.a.createElement(A.a,{words:ne})),l.a.createElement("div",null,l.a.createElement("h2",null,"Symmetry Score"),l.a.createElement(T.HorizontalBar,{data:te})),l.a.createElement("div",null,l.a.createElement("h2",null,"Overall Data"),l.a.createElement(T.HorizontalBar,{data:ae}))):l.a.createElement(ee.a,{animation:"border"}))};var re=function(){return l.a.createElement(c.a,null,l.a.createElement("div",{className:"App"},l.a.createElement(m,null),l.a.createElement("div",{id:"page-body"},l.a.createElement(s.c,null,l.a.createElement(s.a,{path:"/",component:x,exact:!0}),l.a.createElement(s.a,{path:"/survey",component:x}),l.a.createElement(s.a,{path:"/admin",component:U}),l.a.createElement(s.a,{path:"/dashboard",component:le}),l.a.createElement(s.a,{component:u})))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(l.a.createElement(l.a.StrictMode,null,l.a.createElement(re,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[129,1,2]]]);
//# sourceMappingURL=main.cb69a991.chunk.js.map