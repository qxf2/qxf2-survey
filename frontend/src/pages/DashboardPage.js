import React from 'react';
import ReactWordcloud from 'react-wordcloud';
import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';
import {HorizontalBar} from 'react-chartjs-2';

const SymmetryData = {
  labels: ['Shivahari', 'Arunkumar', 'Rahul', 'Raji', 'Avinash', 'Smitha', 'Rohit'],
  datasets: [
    {
      label: "Symmetry Score",
      backgroundColor: 'LightBlue',
      borderColor: 'black',
      borderWidth: 1,
      hoverBackgroundColor: 'blue',
      hoverBorderColor: 'black',
      data: [234, 212, 110, 107, 67, 55, 16]
    }
  ]
};

const OverallData = {
  labels: ['Rohan Joshi', 'Mohan Kumar', 'Kiran CV', 'Akkul DN', 'Rajkumar', 'Smitha', 'Rohan Dudam'],
  datasets: [
    {
      label: "Symmetry Score",
      backgroundColor: 'LightBlue',
      borderColor: 'black',
      borderWidth: 1,
      hoverBackgroundColor: 'blue',
      hoverBorderColor: 'black',
      data: [91, 100, 72, 91, 67, 66, 54]
    }
  ]
};

// Mock Content for the Wordcloud

const words = [
  {
    text: 'Python',
    value: 75,
  },
  {
    text: 'Git',
    value: 55,
  },
  {
    text: 'AWS',
    value: 64,
  },
  {
    text: 'API',
    value: 33,
  },
  {
    text: 'DynamoDB',
    value: 43,
  },
  {
    text: 'Elastic Beanstalk',
    value: 26,
  },
  {
    text: 'Github Actions',
    value: 87,
  },
  {
    text: 'AWS Lambda',
    value: 50,
  },
  {
    text: 'Neo4j',
    value: 23,
  },
  {
    text: 'MySQL',
    value: 35,
  },
  {
    text: 'Py2Neo',
    value: 23,
  },
  {
    text: 'SOAP',
    value: 31,
  },
  {
    text: 'Flask',
    value: 12,
  },
  {
    text: 'Django-REST',
    value: 15,
  },
  {
    text: 'GraphQL',
    value: 30,
  },
  {
    text: 'Selenium',
    value: 18,
  },
]

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