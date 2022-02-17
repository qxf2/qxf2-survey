import React,{ useState, useEffect } from "react";
import axios from "axios";
import url_conf from "./data/urlConf"
import employeeList from "./data/employeeList.js";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

function ConfirmationPage(props) {
  var email = props.state.email;
  var tagList = props.state.tags.toString();
  var whoHelp = JSON.parse(JSON.stringify(props.state.selectedHelp));
  var whomHelped = JSON.parse(JSON.stringify(props.state.selectedHelped));
  const [employees_data, setemployees_data]=useState([])
  const [Loader, setLoader]=useState(true)

  useEffect(() =>{
      setemployees_data(employeeList)
      setLoader(false)
    
  },[])

  var check_valid_email=()=>{
    var valid_email_flag=false
    var i=0
    for(i=0;i<=employees_data.length-1;i++)
    {
      if(employees_data[i]['value']===email)
      {
        valid_email_flag=true
        break;
      }
    }

    return valid_email_flag
  }

  var conditional_render=()=>{
    if(Loader===false){

      var valid_email=check_valid_email()
      console.log(whoHelp)
      if(valid_email===true){
        var surveyResponse = {
          'userMail': email,
          'listHelp': whoHelp,
          'listHelped': whomHelped,
          'listTags': tagList
        }

        if (surveyResponse !== "") {
          axios.post(`${url_conf}/survey/response`, {data: surveyResponse})
            .then(function (response) {
              console.log(surveyResponse)
              console.log("Post request: Success")
            })
            .catch(function (error) {
              console.log("Post request: Failed")
              console.log(error.response);
            });
        } else {
          alert("Could not pass empty data")
        }
        return (
          <div className="jumbotron text-center">
            <h1 className="display-3">Thank You!</h1>
            <p className="lead"><strong>Here is what we recorded!</strong></p>
            <p><b>E-mail:</b> {email}</p>
            <p><b>Who helped you?:</b> {whoHelp.map(whoHelp => whoHelp.label).join(', ')}</p>
            <p><b>Whom did you help?:</b> {whomHelped.map(whomHelped => whomHelped.label).join(', ')} </p>
            <p><b>Tags:</b> {tagList} </p>
          </div>
      );

      }
      else{
        return (
          <div className="jumbotron text-center">
            <p className="lead"><strong>Please enter valid email</strong></p>
          </div>
        );

      }
    }
    else{
      return(<span>Loading.....</span>)
    }
  }

  return (
    conditional_render()
  );
}

export default ConfirmationPage;