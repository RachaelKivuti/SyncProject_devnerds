import  React from 'react';
import {BiEdit}from 'react-icons/bi';

const ProfileHeader = () => {
    return (
    <div className='profile-header'>  
        <h3 className='header-title'>Profile</h3>
        <div className='edit'>
            <BiEdit className='icon'/>
        </div>
    </div>
    );
};

export default ProfileHeader;