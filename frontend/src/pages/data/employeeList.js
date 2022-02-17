import axios from "axios";
import URL from "./urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

var data = [];


axios.get(`${URL}/survey/admin/employees`)
  .then(function (response) {
    for (var i in response.data)
    {
      if (response.data[i]['status'].toLowerCase() === "y" && response.data[i]['email'] !== "test@qxf2.com"){
      data.push({label: response.data[i]['fullName'], value: response.data[i]['email']});
    }
      else if(response.data[i]['status'].toLowerCase() === "y" && response.data[i]['email'] ==="test@qxf2.com"){
      data.push({label: "External", value: "dummy@qxf2.com"})
      }
  }console.log(data)
  })
  .catch(function (error) {
    console.log(error.response);
  });

const options = data;

export default options;