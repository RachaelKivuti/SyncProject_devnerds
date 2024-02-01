import React from "react";
import ContentHeader from "./ContentHeader";
import "../styles/content.css";
import Card from '../components/Card';
import ProjectList from "./ProjectList";

const Content = () => {
    return (
        <div className="content">
          <ContentHeader />
          <Card />
          <ProjectList />
        </div>
    );
};

export default Content;