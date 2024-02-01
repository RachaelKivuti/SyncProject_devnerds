import React from "react";

const projects = [
    {
        title: 'Project 1',
        client: 'Client A',
        deadline: '2024-02-15',
        content: 'Description of Project 1...',
    },
    {
        title: 'Project 2',
        client: 'Client B',
        deadline: '2024-02-15',
        content: 'Description of Project 2...',
    },
];

const Card = () => {
    return <div className="card-container"> 
      {projects.map((item, index) =>(
        <div className="card" key={index}>
           <div className="card-title">
            <h3>{item.title}</h3>
           </div>
           <div className="card-content">
           <    p><strong>Client:</strong> {item.client}</p>
                <p><strong>Deadline:</strong> {item.deadline}</p>
                <p><strong>Description:</strong> {item.content}</p>
           </div>
        </div>
      ))}
    </div>
};

export default Card;