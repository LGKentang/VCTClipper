import React from 'react';
import { useParams } from 'react-router-dom';

const WorkerDetails: React.FC = () => {
    const { uuid } = useParams<{ uuid: string }>();

    return (
        <div>
            <h1>Worker Details for UUID: {uuid}</h1>
            
        </div>
    );
};

export default WorkerDetails;
