import React from 'react'
import { useEffect,useState,useContext } from 'react'
import {Box,Typography,useTheme} from '@mui/material'
import { DataGrid } from '@mui/x-data-grid'
import { tokens } from '../theme'
import { AdminPanelSettingsOutlinedIcon } from '@mui/icons-material/AdminPanelSettingsOutlined'
import { LockOpenOutlinedIcon } from '@mui/icons-material/LockOpenOutlined'
import { SecurityOutlinedIcon } from '@mui/icons-material/SecurityOutlined'
import Headers from '../Components/Headers'
import axios from "axios";
import AuthContext from '../context/AuthContext';

const Users = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [data, setData] = useState([])
  const {authTokens} = useContext(AuthContext)
  const columns = [
    { field:"id" , headerName: "ID"},
    {
      field:"username",
      headerName:"Username",
      flex:1,
      cellClassName: "name-column--cell",

    },
    {
      field:"email",
      headerName:"Email",
      flex:1,

    },
  ]
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/user/listuser/",{
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${
                authTokens.access
            }`
        }
    }).then((response) => {
        setData(response.data)

    })
    console.log(data, "ssssssssssssssssss")

}, []);

  return (
    <Box m="20px">
      <Headers title="User" subtitle="Managing the Users" />
      <Box m="40px 0 0 0" height="75vh">
        <DataGrid rows={data} columns={columns} />
        
      </Box>
    </Box>
  )
}

export default Users
