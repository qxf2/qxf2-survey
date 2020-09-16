import React, { useState } from 'react';
import MultiSelect from "react-multi-select-component";
import ReactTagInput from "@pathofdev/react-tag-input";
import "@pathofdev/react-tag-input/build/index.css";
import 'bootstrap/dist/css/bootstrap.min.css';  
import Button from 'react-bootstrap/Button';
import employeeList from './data/employeeList.js';

const options = employeeList;

const Email = () => {
    return (
        <div className="form-group">
            <h3>Enter your Mail ID?</h3>
            <input id="email" type="email" class="form-control" />
        </div>
    );
};

const SubmitButton = () => {
    return (
        <div className="col-md-4 offset-md-4">
            <Button variant="primary" size="lg" block>
                Submit
        </Button>
        </div>
    );
};

const TagOption = () => {
        const [tags, setTags] = React.useState([])
        return (
            <div className="new-tech">
                <h3>What new technologies did you learn?</h3>
                <ReactTagInput
                    tags={tags}
                    onChange={(newTags) => setTags(newTags)}
                />
                <br></br>
            </div>
        );
    };

const WhoHelped = () => {
    const [selectedHelp, setSelectedHelp] = useState([]);
    return (
      <div className="who-helped">
        <h3>Who helped you this week?</h3>
        <MultiSelect
          options={options}
          value={selectedHelp}
          onChange={setSelectedHelp}
          labelledBy={"Select"}
        />
        <br></br>
      </div>
    );
};

const WhomDidHelp = () => {
    const [selectedHelped, setSelectedHelped] = useState([]);;
    return (
      <div className="whom-did-you-help">
        <h3>Whom did you help this week?</h3>
        <MultiSelect
          options={options}
          value={selectedHelped}
          onChange={setSelectedHelped}
          labelledBy={"Select"}
        />
        <br></br>
      </div>
    );
};

const SurveyPage = () => {
    return (
        <>
            <br></br>
            <Email />
            <WhoHelped />
            <WhomDidHelp />
            <TagOption />
            <SubmitButton />
        </>
    );
};  

export default SurveyPage;