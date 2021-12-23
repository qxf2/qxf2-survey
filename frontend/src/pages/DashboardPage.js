import React, { useState } from 'react';
import ReactWordcloud from 'react-wordcloud';
import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';
import {HorizontalBar} from 'react-chartjs-2';
import symData from './data/SymmetryData';
import overallData from './data/OverallData';
import CloudData from './data/CloudData';
import * as ReactBootStrap from 'react-bootstrap';
import axios from "axios";
import URL from "./data/urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY


const SymmetryData = symData;
const OverallData = overallData;
const words = CloudData;
//const [loading, setLoading] = useState(false);

const DashboardPage = () => {

  var overall_score = [];
  var overall_employee_name = [];
  var symmetry_employee_name = [];
  var symmetry_score = [];

  const [loading, setLoading] = useState(false);
  
  axios.get(`${URL}/survey/admin/overall_response`)
  .then(function (response) {
    for(var name in response.data['name']){
      overall_employee_name.push(response.data['name'][name]);
    }
  
    for(var score in response.data['response_data']){
      overall_score.push(response.data['response_data'][score]);
    } 
    
  })
  .catch(function (error) {
    console.log(error.response);
  });
  
  axios.get(`${URL}/survey/admin/symmetry-score`)
  .then(function (response) {
    for(var name in response.data['employee_name']){
      symmetry_employee_name.push(response.data['employee_name'][name]);
    }
  
    for(var score in response.data['data']){
      symmetry_score.push(response.data['data'][score]);
    }  
    setLoading(true)
  })
  .catch(function (error) {
    console.log(error.response);
  });

  return (
    <div>
      { (loading)?(
    <>
      <h2>Survey Analysis Dashboard</h2>
      <div style={{ backgroundColor: '#efefef', height: '300px', width: '100%' }}>
        <ReactWordcloud words={words} />
      </div>

      <div>
        <h2>Symmetry Score</h2>
        <HorizontalBar data={SymmetryData} />
      </div>

      <div>
        <h2>Overall Data</h2>
        <HorizontalBar data={OverallData} />
      </div>
    </>
      ):<ReactBootStrap.Spinner animation="border" />
    }
  </div>
  );
};

export default DashboardPage;