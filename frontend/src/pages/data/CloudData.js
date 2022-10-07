import axios from "axios";
import URL from "./urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var temp = [];
var tech=[];
var myCurrentDate = new Date();
var myPastDate = new Date(myCurrentDate);
myPastDate.setDate(myPastDate.getDate() - 90)
let past_date = `${myPastDate.getFullYear()}-${myPastDate.getMonth() + 1}-${myPastDate.getDate()}`;
let current_date = `${myCurrentDate.getFullYear()}-${myCurrentDate.getMonth() + 1}-${myCurrentDate.getDate()}`;

const date_range = {
  'start_date':  past_date.toLocaleString(),
  'end_date': current_date.toLocaleString()
}

const range = JSON.stringify(date_range)

axios.post(`${URL}/survey/admin/QElo_filter_technology` , range)
.then(function (response) {
  for(var i in response.data){
    temp.push(response.data[i]['technology']);
  }
    let n = temp.length;
    let visited = Array.from({length: n}, (_, i) => false);
    for (let i = 0; i < n; i++) {
 
      // Skip this element if already processed
      if (visited[i] === true)
          continue;
 
      // Count frequency
      let count = 1;
      for (let j = i + 1; j < n; j++) {
          if (temp[i] === temp[j]) {
              visited[j] = true;
              count++;
          }
      }
         
         tech.push({'text':temp[i],'value':count,});
  }

})
.catch(function (error) {
    console.log("Post request: Failed")
    console.log(error.response);

});

export default tech;