import React from 'react';
import { BiHome, BiTask, BiCreditCard } from 'react-icons/bi';
import '../styles/sidebar.css';
import { Link } from 'react-router-dom';

const Sidebar = () => {
    return (
        <div className="menu">
            <div className="logo">
                <h3>DevNerds</h3>
            </div>

            <div className="menu-list">
                <Link to="/job" className="item">
                    <BiTask className="icon" />
                    Find Jobs
                </Link>
                {/* Other menu items can be added similarly */}
            </div>
        </div>
    );
};

export default Sidebar;