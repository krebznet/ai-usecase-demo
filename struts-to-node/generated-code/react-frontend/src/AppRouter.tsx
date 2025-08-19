import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import VehiclePreference from './pages/VehiclePreference';
import Welcome from './pages/Welcome';
import ApplicantInfo from './pages/ApplicantInfo';

const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  // Add authentication logic here
  return <div>{children}</div>;
};

const AppRouter: React.FC = () => {
  return (
    <Router>
      <Routes>
    <Route path="/" element={<Welcome />} />
    <Route path="/welcome" element={<Welcome />} />
    <Route path="/applicantInfo" element={<ProtectedRoute><Applicantinfo /></ProtectedRoute>} />
    <Route path="/vehiclePreference" element={<ProtectedRoute><Vehiclepreference /></ProtectedRoute>} />
    <Route path="/financialInfo" element={<ProtectedRoute><Financialinfo /></ProtectedRoute>} />
    <Route path="/backgroundCheck" element={<ProtectedRoute><Backgroundcheck /></ProtectedRoute>} />
    <Route path="/leaseReview" element={<Leasereview />} />
    <Route path="/submitApplication" element={<Submitapplication />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;
