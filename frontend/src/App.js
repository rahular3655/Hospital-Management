import { BrowserRouter as Router , Routes,Route, Navigate } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import './App.css';
import Sidebar from './Components/Sidebar';
import { AuthProvider } from './context/AuthContext';
import Beds from './pages/Beds';
import Dashboard from './pages/Dashboard';
import Doctors from './pages/Doctors';
import Nurse from './pages/Nurse';
import Patients from './pages/Patients';
import Signin from './pages/Signin';
import Staff from './pages/Staff';
import Users from './pages/Users';

function App() {
  return (
    <div className="App">
      <Router>
      <AuthProvider>

        <Routes>
          <Route path='/' element={<Signin/>}/>

          <Route path='' element={<Sidebar/>}>
          <Route exact path='/adminhome' element={<Navigate replace to="/adminhome/dashboard"/>} />
            <Route path='/adminhome/dashboard' element={<Dashboard/>}/>
            <Route path='/adminhome/user' element={<Users/>}/>
            <Route path='/adminhome/doctor' element={<Doctors/>}/>
            <Route path='/adminhome/nurse' element={<Nurse/>}/>
            <Route path='/adminhome/staff' element={<Staff/>}/>
            <Route path='/adminhome/patient' element={<Patients/>}/>
            <Route path='/adminhome/bed' element={<Beds/>}/>
            
           
           </Route>
          
            
        </Routes>
      </AuthProvider>
      </Router>
      <ToastContainer />
    </div>
  );
}

export default App;
