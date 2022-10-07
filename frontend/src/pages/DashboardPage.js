import React from 'react';
import ReactWordcloud from 'react-wordcloud';
import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';
import {HorizontalBar} from 'react-chartjs-2';
import symData from './data/SymmetryData';
import overallData from './data/OverallData';
import CloudData from './data/CloudData';


const SymmetryData = symData;
const OverallData = overallData;
const words = CloudData;

const DashboardPage = () => {
  return (
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
  );
};

export default DashboardPage;