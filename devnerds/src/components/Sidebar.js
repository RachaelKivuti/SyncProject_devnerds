import React from 'react';
import { BiHome, BiTask, BiMessage, BiStats, BiCreditCard  } from 'react-icons/bi';
import '../styles/sidebar.css';
const  Sidebar = () => {
    return  <div className="menu">
        <div className= "logo">
            <h3>DevNerds</h3>
        </div>

        <div className="menu-list">
           <a href="#" className="item">
             <BiHome classname= "icon"/>
             Dashboard   
            </a> 
            {/* // <a href="#" className="item">
             //<BiTask classname= "icon"/>
             Projects  
            </a>  */}
            <a href="#" className="item">
             <BiTask classname= "icon"/> Find Jobs 
            </a> 
            <a href="#" className="item">
             <BiCreditCard classname= "icon"/>
             Withdraw  
            </a> 
            {/* <a href="#" className="item">
             <BiMessage classname= "icon"/>
             Message   
            </a> 
            <a href="#" className="item">
             <BiStats classname= "icon"/>
             Stats
            </a>  */}
        </div>

    </div>
    
};

export default Sidebar;