import React from "react";
import Navbar from "../global/Navbar";
import { ColorModeContext, useMode } from "../../theme";
import { CssBaseline,ThemeProvider } from '@mui/material';
import "../Dashboard/AdminDashboard.css"
import  Sidebar from "../global/Sidebar";
import {  Route ,Routes } from "react-router-dom";
import  Dashboard from "../Dashhboard";
import  Users from "../Users";
import  Patients from "../Patients";
import  Doctors from "../Doctors";
import  Staff from "../Staff";

const AdminHome = ()=>{
    const[theme,colorMode]=useMode();
    return(
        <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline/>
        <div className="app">
            <Sidebar />
            <main className="content">
                <Navbar/>
                <Routes>
                    <Route path="/" element={<Dashboard/>}/> 
                    <Route path="/users" element={<Users/>}/>
                    <Route path="/patients" element={<Patients/>}/>
                    <Route path="/Doctors" element={<Doctors/>}/>
                    <Route path="/Staffs" element={<Staff/>}/>
                </Routes>
            </main>
        </div>
        </ThemeProvider>
    </ColorModeContext.Provider>
    )
};

export default AdminHome