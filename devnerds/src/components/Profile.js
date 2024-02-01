import React from "react";
import ProfileHeader from "./ProfileHeader";
import '../styles/profile.css';
import { BiUserCircle } from 'react-icons/bi';

const projects = [
    {
    title: 'Project 1',
    Progress: 'Progress: 20%',
    },
    {
    title: 'Project 2',
    Progress: 'Progress: 80%',
    },
];
const Profile = () => {
    return (
    <div className="profile">
        <ProfileHeader />

        <div className="user-profile">
            <div className="user-detail">
                <img src={BiUserCircle} alt=""/>
                <h3 className="username">Username</h3>
                <span className="profession">Software Developer</span>
            </div>

            <div className="user-project">
               {projects.map(projects=> (
               <div className="project">
                 <div className="project-detail">
                     <div className="project-name">
                            <h5 className="title">{projects.title}</h5>
                            <span className="progress">{projects.Progress}</span>
                     </div>
                 </div>
                 <div className="action">:</div>
               </div>
               ))} 
            </div>
        </div>
    </div>
    );
};

export default Profile;