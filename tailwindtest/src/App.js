import { BrowserRouter as Router , Routes,Route } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import './App.css';
import Sidebar from './Components/Sidebar';
import { AuthProvider } from './context/AuthContext';
import Dashboard from './pages/Dashboard';
import Doctors from './pages/Doctors';
import Nurse from './pages/Nurse';
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

          <Route path='/adminhome' element={<Sidebar/>}>
            <Route path='dashboard' element={<Dashboard/>}/>
            <Route path='user' element={<Users/>}/>
            <Route path='doctor' element={<Doctors/>}/>
            <Route path='nurse' element={<Nurse/>}/>
            <Route path='staff' element={<Staff/>}/>
           </Route>
          
            
        </Routes>
      </AuthProvider>
      </Router>
      <ToastContainer />
    </div>
  );
}

export default App;
