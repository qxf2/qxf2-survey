import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom'
import './App.css';
import NavBar from './components/NavBar';
// import firstQuestion from './components/firstQuestion';
import NotFoundPage from './pages/NotFoundPage';
import SurveyPage from './pages/SurveyPage';
import AdminPage from './pages/AdminPage';
import DashboardPage from './pages/DashboardPage';

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <div id="page-body">
          <Switch>
            <Route path="/" component={SurveyPage} exact />
            <Route path="/survey" component={SurveyPage} />
            <Route path="/admin" component={AdminPage} />
            <Route path="/dashboard" component={DashboardPage} />
            <Route component={NotFoundPage} />
         </Switch>
         </div>
      </div>
    </Router>
  );
}

export default App;
