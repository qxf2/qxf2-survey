import React, { useState } from 'react';
import MultiSelect from "react-multi-select-component";
import ReactTagInput from "@pathofdev/react-tag-input";
import "@pathofdev/react-tag-input/build/index.css";
import 'bootstrap/dist/css/bootstrap.min.css';  
import Button from 'react-bootstrap/Button';

const options = [
      { label: " Arunkumar Muralidharan", value: "mak@qxf2.com" },
      { label: "Raji Gali", value: "raji@qxf2.com" },
      { label: "Avinash Shetty", value: "avinash@qxf2.com" },
      { label: "Shivahari Pitchaikkannu", value: "shivahari@qxf2.com" },
      { label: "Annapoorani Gurusamy", value: "annapoorani@qxf2.com" },
      { label: "Rohan Dudam", value: "rohan@qxf2.com" },
      { label: "Smitha Rajesh", value: "smitha@qxf2.com" },
      { label: "Indira Nellutla", value: "indira@qxf2.com" },
      { label: "Rohan Joshi", value: "rohan.js@qxf2.com"},
      { label: "Nilaya Indurkar", value: "nilaya@qxf2.com" },
      { label: "Edward Alan", value: "edward@qxf2.com" },
      { label: "Mohan Kumar", value: "mohan@qxf2.com" },
      { label: "Kavitha Duraiswamy", value: "kavitha.d@qxf2.com" },
      { label: "Rohini Gopal", value: "rohini.gopal@qxf2.com" },
      { label: "Akkul DN", value: "akkul.dn@qxf2.com" },
      { label: "Kiran CV", value: "kiran.cv@qxf2.com" },
      { label: "Sravanti Tatiraju", value: "sravanti.tatiraju@qxf2.com" },
      { label: "Rahul Bhave", value: "rahul.bhave@qxf2.com" },
      { label: "Preedhi Vivek", value: "preedhi.vivek@qxf2.com" },
      { label: "Drishya TM", value: "drishya.tm@qxf2.com" },
      { label: "Harsh Bardhan", value: "harsh.bardhan@qxf2.com" },
      { label: "Rohit Prasad", value: "rohit.prasad@qxf2.com" },
      { label: "Basavaraj Hiremath", value: "basavaraj.hiremath@qxf2.com" },
      { label: "Namitha Sathyananda", value: "namitha.sathyananda@qxf2.com" },
      { label: "Vidhya Zierlein", value: "vidhya.zierlein@qxf2.com" },
      { label: "Rakhi Chaudhuri", value: "rakhi.chaudhuri@qxf2.com" },
    ];

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