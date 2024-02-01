import React from 'react';
import Sidebar from './components/Sidebar';
import Profile from './components/Profile';
import Content from './components/Content';
import './App.css';

const App = () => {
  return ( 
    <div className='dashboard'>
      <Sidebar />
      <div className="dashboard-content"> 
        <Content />
        <Profile />
      </div>
    </div>
  );
};

export default App;