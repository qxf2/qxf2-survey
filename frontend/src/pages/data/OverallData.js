import axios from "axios";
import URL from "./urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var score = [];
var employee_name = [];

axios.get(`${URL}/survey/admin/overall_response`)
.then(function (response) {

  for(var name in response.data['name']){
    employee_name.push(response.data['name'][name]);
  }

  for(var value in response.data['response_data']){
    score.push(response.data['response_data'][value]);
  }  

})
.catch(function (error) {
  console.log(error.response);
});

const OverallData = {
  labels: employee_name,
  datasets: [
    {
      label: "Overall Response",
      backgroundColor: 'LightBlue',
      borderColor: 'black',
      borderWidth: 1,
      hoverBackgroundColor: 'blue',
      hoverBorderColor: 'black',
      data: score
    }
  ]
};

export default OverallData;