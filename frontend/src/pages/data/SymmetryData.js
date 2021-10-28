import axios from "axios";
import URL from "./urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var data = [];


axios.get(`${URL}/survey/admin/employees`)
  .then(function (response) {
    for (var i in response.data)
    {
      if (response.data[i]['status'].toLowerCase() === "y"){
      data.push(response.data[i]['fullName']);
    }}
  })
  .catch(function (error) {
    console.log(error.response);
  });

const SymmetryData = {
  labels: data,
  datasets: [
    {
      label: "Symmetry Score",
      backgroundColor: 'LightBlue',
      borderColor: 'black',
      borderWidth: 1,
      hoverBackgroundColor: 'blue',
      hoverBorderColor: 'black',
      data: [234, 212, 110, 107, 67, 55, 16]
    }
  ]
};

export default SymmetryData;