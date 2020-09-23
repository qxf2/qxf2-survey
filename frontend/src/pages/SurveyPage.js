import React from "react";
import { Steps, Step } from "react-step-builder";
import QuestionForm from "./QuestionForm";
import ConfirmationPage from "./ConfirmationPage";

function SurveyPage() {
  return (
    <div className="App">
      <Steps>
        <Step component={QuestionForm} />
        <Step component={ConfirmationPage} />
      </Steps>
    </div>
  );
}

export default SurveyPage;
