import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { Link, Navigate, Outlet } from "react-router-dom";
import DeskAuthContext from "../DeskContext/DeskAuthContext";

export default function DeskSidebar() {
  const Navigate=useNavigate()
  const [isSidebarOpen, setIsSidebarOpen] = React.useState(false);
  const {logoutDesk} = useContext(DeskAuthContext)
  const logout=()=>{
    logoutDesk()
    Navigate('/frontdesksignin')
  }
  function toggleSidebar() {
    setIsSidebarOpen(!isSidebarOpen);
  }
  return (
    <div>

    <div className="relative flex ">
      <button
        className="lg:hidden px-3 py-2 rounded-lg text-blue-600 hover:text-fuchsia-600 focus:outline-none focus:text-blue-600"
        onClick={toggleSidebar}
      >
        Menu
      </button>
      <div
        className={`${
          isSidebarOpen ? "block" : "hidden"
        } lg:bloc lg:flex lg:items-center lg:w-auto w-full lg:static  h-0 lg:h-auto px-6 pt-5 pb-4 overflow-y-auto `}
      >
        <aside className="bg-red- w-64 mt-32 h-screen absolute fixed top-8 left-0 z-50 p-4 overflow-y-hidden  md:block">
          <div className="text-blue-800 text-xl font-semibold mb-4">Menu</div>
          <ul className="mb-4">
            <li className="mb-2">
              <Link
                to="/deskhome/dashboard"
                className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full text-center mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block"
              >
                Dashboard
              </Link>
            </li>
            <li className="mb-2">
              <Link
                to="/deskhome/doctors"
                className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full  mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block"
              >
                Doctor
              </Link>
            </li>
            <li className="mb-2">
              <Link
                to="/deskhome/patients"
                className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full  mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block"
              >
                Patient
              </Link>
            </li>
            <li className="mb-2">
              <Link
                to="/deskhome/bill"
                className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full  mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block"
              >
                Bills
              </Link>
            </li>
            <li className="mb-2">
              <Link
                to="/deskhome/staff"
                className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full  mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block"
              >
                Staffs
              </Link>
            </li>
            <li className="mb-2">
              <Link
                to="/deskhome/accounts"
                className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full  mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block"
              >
                Accounts
              </Link>
            </li>
          </ul>
        </aside>
      </div>
      <div className="lg:flex-grow flex-grow">
        {/* main content goes here */}
      </div>
    </div>

    <nav className="bg-white text-black p-3">
      <div className="container mx-auto flex items-center justify-between">
        <div className="text-3xl font-bold text-blue-800">
          MM Hospital <span className="text-5xl text-red-700">+</span> 
        </div>
        <div className="hidden md:flex">
          

        <div className="relative flex-grow flex-shrink-0">
      <input
        className="appearance-none block w-full bg-gray-200 text-gray-700 border-2 rounded-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-fuchsia-600"
        type="text"
        placeholder="Search"
      />
      <button className="absolute top-0 right-0 mt-3 mr-4">
        <svg className="h-6 w-6 fill-current text-gray-500" viewBox="0 0 24 24">
          <path d="M10 18a7.952 7.952 0 01-5.711-2.306 7.982 7.982 0 01-.497-.578l4.571-4.571a1 1 0 011.414 1.414L10 16.414l4.146 4.146a1 1 0 01-1.414 1.414l-4.571-4.571A7.982 7.982 0 0110 18zM10 4a6 6 0 100 12 6 6 0 000-12z" />
        </svg>
      </button>
    </div>



          
          <button onClick={()=>logout()} className="bg-gray-200 font-semibold py-2 px-4 rounded-full w-full mb-4 text-fuchsia-600 hover:bg-blue-800 hover:text-white block">Logout</button>
        </div>
        <button className="block md:hidden">
          <svg className="h-6 w-6 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
        </button>
      </div>
      
    </nav>

    <Outlet />

    </div>
  );
}
