import React from "react";
import axios from "axios";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

function ConfirmationPage(props) {
  var email = props.state.email;
  var tagList = props.state.tags.toString();
  var whoHelp = JSON.parse(JSON.stringify(props.state.selectedHelp));
  var whomHelped = JSON.parse(JSON.stringify(props.state.selectedHelped));

  var surveyResponse = {
    'userMail': email,
    'listHelp': whoHelp,
    'listHelped': whomHelped,
    'listTags': tagList
  }

  console.log("Stored Data and passing it now");
  
  if (surveyResponse !== "") {
    axios.post('http://3.239.35.79:8000/survey/response', {data: surveyResponse})
      .then(function (response) {
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
    <div class="jumbotron text-center">
      <h1 class="display-3">Thank You!</h1>
      <p class="lead"><strong>Here is what we recorded!</strong></p>
      <p><b>E-mail:</b> {email}</p>
      <p><b>Who helped you?:</b> {whoHelp.map(whoHelp => whoHelp.label).join(', ')}</p>
      <p><b>Whom did you help?:</b> {whomHelped.map(whomHelped => whomHelped.label).join(', ')} </p>
      <p><b>Tags:</b> {tagList} </p>
    </div>
  );
}

export default ConfirmationPage;