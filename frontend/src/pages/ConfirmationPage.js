import React from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";

function ConfirmationPage(props) {
  var email = props.state.email;
  var tagList = props.state.tags.toString();
  var whoHelp = JSON.parse(JSON.stringify(props.state.selectedHelp));
  var whomHelped = JSON.parse(JSON.stringify(props.state.selectedHelped));

  let axiosConfig = {
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
    }
  };

  var employeeData = {
    'userMail': email,
    'listHelp': whoHelp,
    'listHelped': whomHelped,
    'listTags': tagList
  }
  console.log("Stored Data and passing it now");
  console.log(employeeData);
  if (employeeData !== "") {
    axios.post('http://localhost:8000/api/get_data', employeeData, axiosConfig)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
        //Perform action based on error
      });
  } else {
    alert("Could not pass the Data")
  }
  return (
    <div class="jumbotron text-center">
      <h1 class="display-3">Thank You!</h1>
      <p class="lead"><strong>Here is what we recorded!</strong></p>
      <p><b>E-Mail:</b> {email}</p>
      <p><b>Who helped you:</b> {whoHelp.map(whoHelp => whoHelp.label).join(', ')}</p>
      <p><b>Whom did you help:</b> {whomHelped.map(whomHelped => whomHelped.label).join(', ')} </p>
      <p><b>Tags:</b> {tagList} </p>
      <div className="col-md-4 offset-md-4">
        <Button
          variant="primary"
          size="lg"
          block
          button
          disabled={props.step.isLast()}
          onClick={props.next}
        >
          Back to Survey
        </Button>
      </div>
    </div>
  );
}

export default ConfirmationPage;