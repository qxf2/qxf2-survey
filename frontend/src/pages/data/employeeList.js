import axios from "axios";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var data = [];

axios.get('http://3.239.35.79:8000/survey/admin/employees')
  .then(function (response) {
    for (var i in response.data)
    {
      if (response.data[i]['status'] === "Y"){
      data.push({label: response.data[i]['fullName'], value: response.data[i]['email']});
    }}
  })
  .catch(function (error) {
    console.log(error.response);     
  });

const options = data;

export default options;