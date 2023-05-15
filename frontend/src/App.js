import { BrowserRouter as Router , Routes,Route, Navigate } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import './App.css';
import Sidebar from './Components/Sidebar';
import { AuthProvider } from './context/AuthContext';
import Accounts from './pages/Admin/Accounts';
import Beds from './pages/Admin/Beds';
import Dashboard from './pages/Admin/Dashboard';
import Home from './pages/Doctor/Home';
import Profile from './pages/Doctor/Profile';
import DocPat from './pages/Doctor/Patients';
import Doctors from './pages/Admin/Doctors';
import Inventory from './pages/Admin/Inventory';
import Nurse from './pages/Admin/Nurse';
import Patients from './pages/Admin/Patients';
import Signin from './pages/Admin/Signin';
import Staff from './pages/Admin/Staff';
import Users from './pages/Admin/Users';
import { DeskAuthProvider } from './pages/FrontDesk/DeskContext/DeskAuthContext';
import FdSignin from './pages/FrontDesk/FDSignin/fdSignin';
import DeskSidebar from './pages/FrontDesk/Components/Sidebar';
import DeskDashboard from './pages/FrontDesk/Dashboard';
import DeskPatients from './pages/FrontDesk/patients';
import DeskDoctors from './pages/FrontDesk/Doctors';
import DeskStaff from './pages/FrontDesk/staff';

function App() {
  return (
    <div className="App">
      <Router>
      <AuthProvider>

        <Routes>
          <Route path='/' element={<Signin/>}/>

          <Route path='' element={<Sidebar/>}>
          <Route path='/adminhome' element={<Navigate replace to="/adminhome/dashboard"/>} />
            <Route path='/adminhome/dashboard' element={<Dashboard/>}/>
            <Route path='/adminhome/user' element={<Users/>}/>
            <Route path='/adminhome/doctor' element={<Doctors/>}/>
            <Route path='/adminhome/nurse' element={<Nurse/>}/>
            <Route path='/adminhome/staff' element={<Staff/>}/>
            <Route path='/adminhome/patient' element={<Patients/>}/>
            <Route path='/adminhome/bed' element={<Beds/>}/>
            <Route path='/adminhome/inventory' element={<Inventory/>}/>
            <Route path='/adminhome/accounts' element={<Accounts/>}/>
           </Route>


          <Route>
            <Route path='/doctorhome' element={<Home/>}/>
              <Route path='/doctorprofile' element={<Profile/>}/>
              <Route path='/patientslist' element={<DocPat/>}/>
          </Route>
            
        </Routes>
      </AuthProvider>


      {/* ..............................fRONTDESK.......................................... */}
      <DeskAuthProvider>
          <Routes>
            <Route path='/frontdesksignin' element={<FdSignin/>} />
            <Route path='' element={<DeskSidebar/>}>
            <Route exact path='/deskhome' element={<Navigate replace to="/deskhome/dashboard"/>} />
            <Route path='/deskhome/dashboard' element={<DeskDashboard/>} />
            <Route path='/deskhome/patients' element={<DeskPatients/>} />
            <Route path='/deskhome/doctors' element={<DeskDoctors/>} />
            <Route path='/deskhome/staff' element={<DeskStaff/>} />
            <Route path='/deskhome/bill' element={<DeskStaff/>} />
            </Route>
          </Routes>
        </DeskAuthProvider> 



      </Router>
      <ToastContainer />
    </div>
  );
}

export default App;
