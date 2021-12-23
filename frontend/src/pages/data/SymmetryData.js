import axios from "axios";
import URL from "./urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var score = [];
var employee_name = [];

axios.get(`${URL}/survey/admin/symmetry-score`)
.then(function (response) {

  for(var name in response.data['employee_name']){
    employee_name.push(response.data['employee_name'][name]);
  }

  for(var value in response.data['data']){
    score.push(response.data['data'][value]);
  }  

})
.catch(function (error) {
  console.log(error.response);
});

const SymmetryData = {
  labels: employee_name,
  datasets: [
    {
      label: "Symmetry Score",
      backgroundColor: 'LightBlue',
      borderColor: 'black',
      borderWidth: 1,
      hoverBackgroundColor: 'blue',
      hoverBorderColor: 'black',
      data: score
    }
  ]
};

export default SymmetryData;