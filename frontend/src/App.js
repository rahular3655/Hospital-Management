import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css';
import * as React from 'react';
import Signin from './Pages/Signin/Signin';
import { AuthProvider } from './context/AuthContext';
import AdminHome from './Pages/AdminDashboard';

function App() {
  return (
    <div className="App">
      <Router>
        <AuthProvider>
          <Routes>
            <Route path="/" exact element={<Signin/>}  />
            <Route path="/adminhome" exact element={<AdminHome/>}  />
          </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
