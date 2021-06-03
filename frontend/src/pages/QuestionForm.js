import React, { useEffect } from "react";
import MultiSelect from "react-multi-select-component";
import "@pathofdev/react-tag-input/build/index.css";
import ReactTagInput from "@pathofdev/react-tag-input";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import employeeList from "./data/employeeList.js";

const options = employeeList;

function QuestionForm({ setState, ...props }) {
  const [selectedHelp, setSelectedHelp] = React.useState([]);
  const [tags, setTags] = React.useState([]);
  const [selectedHelped, setSelectedHelped] = React.useState([]);

  useEffect(() => {
    setState("selectedHelp", selectedHelp);
  }, [selectedHelp, setState]);

  useEffect(() => {
    setState("tags", tags);
  }, [tags, setState]);

  useEffect(() => {
    setState("selectedHelped", selectedHelped);
  }, [selectedHelped, setState]);

  return (
    <div>
      <div className="form-group">
        <h3>Enter Email ID</h3>
        <input
          name="email"
          type="email"
          onChange={props.handleChange}
          className="form-control"
        />
      </div>

      <div className="new-tech">
        <h3>What new technologies did you learn this week?<sub id="reference"><a href="https://wiki.qxf2.com/home/r-d/newbie-orientation/what-technologies-did-you-work-on-this-week">Help</a></sub></h3>
        <ReactTagInput tags={tags} onChange={(newTags) => setTags(newTags)} />
        <br></br>
      </div>

      <div className="who-helped">
        <h3>Who helped you this week?<sub id="reference"><a href="https://wiki.qxf2.com/home/r-d/newbie-orientation/helping-others">Help</a></sub></h3>
        <MultiSelect
          options={options}
          value={selectedHelp}
          onChange={setSelectedHelp}
          labelledBy={"Select"}
        />
        <br></br>
      </div>

      <div className="whom-did-you-help">
        <h3>Whom did you help this week?<sub id="reference"><a href="https://wiki.qxf2.com/home/r-d/newbie-orientation/helping-others">Help</a></sub></h3>
        <MultiSelect
          options={options}
          value={selectedHelped}
          onChange={setSelectedHelped}
          labelledBy={"Select"}
        />
        <br></br>
      </div>
      <div className="col-md-4 offset-md-4">
        <Button
          variant="primary"
          size="lg"
          block
          button="true"
          disabled={props.step.isLast()}
          onClick={props.next}
        >
          Submit
        </Button>
      </div>
    </div>
  );
}

export default QuestionForm;