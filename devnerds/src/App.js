import React from 'react';
import Sidebar from './components/Sidebar';
import Profile from './components/Profile';
import Content from './components/Content';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom'; // Change Router to BrowserRouter
import Dashboard from './pages/Dashboard';
import Jobs from './pages/jobs'; // Correct capitalization
import Withdraw from './pages/withdraw'; // Correct capitalization

const App = () => {
  return (
    <Router>
      <div className='dashboard'>
        <Sidebar />
        <div className="dashboard-content">
          <Content />
          <Profile />
        </div>
        <Route exact path='/dashboard'> {/* Assuming this is your dashboard route */}
          <Dashboard />
        </Route>
        <Route exact path='/jobs'> {/* Correct path to 'jobs' */}
          <Jobs />
        </Route>
        <Route exact path='/withdraw'> {/* Correct path to 'withdraw' */}
          <Withdraw />
        </Route>
      </div>
    </Router>
  );
};

export default App;
