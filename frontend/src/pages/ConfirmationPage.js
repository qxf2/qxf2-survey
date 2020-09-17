import React from "react";

function ConfirmationPage(props) {
  var tagList = props.state.tags.toString();
  var whoHelp = JSON.parse(JSON.stringify(props.state.selectedHelp));
  var whomHelped = JSON.parse(JSON.stringify(props.state.selectedHelped));
  return (
    <div class="jumbotron text-center">
      <h1 class="display-3">Thank You!</h1>
      <p class="lead"><strong>Here is what we recorded!</strong></p>
      <p><b>E-Mail:</b> {props.state.email}</p>
      <p><b>Who helped you:</b> {whoHelp.map(whoHelp => whoHelp.label).join(', ')}</p>
      <p><b>Whom did you help:</b> {whomHelped.map(whomHelped => whomHelped.label).join(', ')} </p>
      <p><b>Tags:</b> {tagList} </p>
    </div>
  );
}

export default ConfirmationPage;
