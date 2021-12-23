import axios from "axios";
import URL from "./urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var temp = [];
var tech=[];

const date_range = {
  'start_date':  Date().toLocaleString(),
  'end_date': '2022-11-30'
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