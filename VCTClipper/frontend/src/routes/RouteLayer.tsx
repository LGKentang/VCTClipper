import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from '../pages/dashboard';
import Clips from '../pages/clips';
import Workers from '../pages/workers';
import WorkerDetails from '../pages/worker_details';

const RouteLayer: React.FC<{ children?: React.ReactNode }> = ({ children }) => {
    return (
        <Router>
                <Routes>
                    <Route path="/" element={<Navigate to="/dashboard" />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/workers" element={<Workers />} />
                    <Route path="/workers/:uuid" element={<WorkerDetails />} />
                    <Route path="/clips" element={<Clips />} />
                </Routes>
                {children}
        </Router>
    );
};

export default RouteLayer;
