import React, { useContext, useEffect, useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { TableCell } from '@mui/material';
import {Button }from "@mui/material";
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate } from "react-router";
import Swal from 'sweetalert2';
import AuthContext from "../../context/AuthContext";






export default function Nurse() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const [age, setAge] = React.useState('');
  const [data, setData] = useState([])
  const {authTokens} = useContext(AuthContext)


  const [modalOpen, setModalOpen] = useState(false);
  const [modalOpenn, setModalOpenn] = useState(false);

  const renderCell = (cellValues) => {
    return (
      <Button
        variant="contained"
        color="primary"
        onClick={(event) => {
          handleClick(event, cellValues);
        }}
      >
        Edit{}
      </Button>
    );
  };


  const renderCelll = (cellValues) => {
    return (
      <Button
        variant="contained"
        color="error"
        onClick={(event) => {
          handleClickk(event, cellValues);
        }}
      >
        Delete{}
      </Button>
    );
  };

  

  const handleClick = (event, cellValues) => {
    setModalOpen(true);
  };

  const handleClickk = (event, cellValues) => {
    // setModalOpenn(true);
    Swal.fire({
  title: 'Are you sure?',
  text: 'You will not be able to recover this imaginary file!',
  icon: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Yes, delete it!',
  cancelButtonText: 'No, keep it'
}).then((result) => {
  if (result.isConfirmed===true) {
    axios.delete(`http://127.0.0.1:8000/staffs/doctor/${selectionid}/`,{
    headers:{
      'Content-Type': 'application/json',
      "Authorization": `Bearer ${
          authTokens.access
      }`
    }
  }).then(response=>{
    const post = response.data;
    console.log(post);
  }).catch(error=>{
    console.log(error);
  })
  console.log(selectionid)
  Swal.fire(
    'Deleted!',
    'Your imaginary file has been deleted.',
    'success'
    )
    window.location.reload()
  } else if (result.dismiss === Swal.DismissReason.cancel) {
    Swal.fire(
      'Cancelled',
      'Your imaginary file is safe',
      'error'
    )
  }
})
  };

  const handleClosee = () => {
    setModalOpen(false);
  };

  const columns = [
    { field: "id", headerName: "ID", width: 70 },
    { field: "name", headerName: "Name", width: 170 },
    { field: "created_by", headerName: "Added by", width: 130 },
    {
      field: "age",
      headerName: "Age",
      headerAlign: "center",
      type: "number",
      width: 90,
      align:"center"
    },
    {
      field: "status",
      headerName: "Status",
      headerAlign: "center",
      type: "number",
      width: 180,
      align:"center"
    },
    {
      field: "bloodGroup",
      headerName: "Blood Group",
      headerAlign: "center",
      width: 110,
      align:"center"
    },
    {
      field: "phonenumber",
      headerName: "Phonenumber",
      headerAlign: "center",
      width: 150,
      align:"center"
    },
      {
        field: "action",
        headerName: "Action",
        headerAlign: "center",
        width: 60,
        align:"center",
        flex:1,
        renderCell:renderCell
      },
      {
        field: "delete",
        headerName: "Delete",
        headerAlign: "center",
        width: 60,
        align:"center",
        flex:1,
        renderCell:renderCelll
      },
  ];
  
  
  const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 600,
    bgcolor: "background.paper",
    border: "2px solid #000",
    boxShadow: 24,
    p: 4,
  };

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  const handleImageChange=(e)=>{
    setDetails({...details,[e.target.name]:e.target.files[0]})
  }

  const handleImageChangee=(e)=>{
    setDetails({...detailsupdate,[e.target.name]:e.target.files[0]})
  }

  const onHandlechange = (e) => {
    setDetails({ ...details, [e.target.name]: e.target.value });}

  const [selectionid,setSelectionid]=useState('')

  const onUpdatechange = (e) => {
    setDetailsupdate({ ...detailsupdate, [e.target.name]: e.target.value });
  console.log(detailsupdate,"values...................")}

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/staffs/nurselist/",{
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


const deletedata = (e,id)=>{
  axios.delete(`http://127.0.0.1:8000/staffs/nurse/${id}/`,{
    headers:{
      'Content-Type': 'application/json',
      "Authorization": `Bearer ${
          authTokens.access
      }`
    }
  }).then(response=>{
    const post = response.data;
    console.log(post);
  }).catch(error=>{
    console.log(error);
  })
}

const {admin} = useContext(AuthContext)
  
  const Swal = require("sweetalert2")
  const Navigate=useNavigate()

  console.log(admin.user_id)
  console.log(authTokens,"tokensssssssssssssss")
  const [details, setDetails] = useState({
    created_by:admin.user_id,
    name: "",
    phonenumber: "",
    bloodGroup: "",
    age: "",
    image: "",
    status:"",
    date_of_join:""
  });

  // for editing the previous data............................................................................

  const [updatadata, setUpdatedata] = useState([])
  const [detailsupdate, setDetailsupdate] = useState({
    created_by:admin.user_id,
    name: "",
    phonenumber: "",
    bloodGroup: "",
    age: "",
    image: "",
    status:"",
    date_of_join:""
  });
  // console.log(e,detailsupdate)
  const uploadUpdated =(e,id)=>{
    console.log(id,"iddddddddddd...............")
    console.log(detailsupdate,"HEllooo details  ")
    e.preventDefault();
    const formUpdateSent=new FormData();
    for (let key in detailsupdate){
    formUpdateSent.append(key,detailsupdate[key]);
    console.log(formUpdateSent)
  }

  axios.patch(`http://127.0.0.1:8000/staffs/nurse/${id}/`,formUpdateSent,{
    headers: {
        'Content-Type': 'multipart/form-data',
        "Authorization": `Bearer ${
            authTokens.access
        }`
    }
}).then((response)=>{
  
    console.log(response.data)
  setDetailsupdate('')
  toast.success('Doctor details is updated successfully! ', {
    position: "top-right",
    autoClose: 3000,
    hideProgressBar: true,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: "colored",
  });
  if(response.status === 200){
    Navigate("/adminhome")
  };
  
}).catch((error)=>{
toast.success('Something went wrong !', {
  position: "top-right",
  autoClose: 3000,
  hideProgressBar: true,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  progress: undefined,
  theme: "colored",
});

})

  }


  const uploadData = (e) => {  
      e.preventDefault();
      console.log(details)
    console.log(details.image)
    
    const formSent = new FormData();
    for (let key in details) {
        console.log(key in details,"hgfsewawesrdrt")
      formSent.append(key, details[key]);
    }
    console.log(formSent,"form in..............")
    
    axios.post('http://127.0.0.1:8000/staffs/nursecreate/',formSent,{
        headers: {
            'Content-Type': 'multipart/form-data',
            "Authorization": `Bearer ${
                authTokens.access
            }`
        }
    }).then((response)=>{
      
        console.log(response.data)
      setDetails('')
      toast.success('Doctor details is added successfully! ', {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "colored",
      });
      if(response.status === 200 || 201){
        window.location.reload()
      };
      
  }).catch((error)=>{
    toast.success('Something went wrong !', {
      position: "top-right",
      autoClose: 3000,
      hideProgressBar: true,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "colored",
    });

  })
  };



  return (
    <div className=" ml-72 min-h-[800px] bg-slate-300 rounded-md w-[1500px] grid gap-x-6 gap-y-4 grid-cols-1 content-center mt-3">
      <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
        List of Nurse
      </h1>
      <div className="justify-self-end">
        <button
          onClick={handleOpen}
          className="bg-fuchsia-600 w-36 rounded-full text-white flex hover:bg-blue-600 justify-center mr-8 "
        >
          Add Doctor
        </button>
      </div>
      <div className="mx-10 rounded-md bg-gray-300 h-[700px]  ">
        <div style={{ height: "100%", width: "100%" }}>
          <DataGrid
            rows={data}
            columns={columns}
            pageSize={9}
            rowsPerPageOptions={[5]}
            onSelectionModelChange={(newSelectionArrayindex)=>{
              setSelectionid(newSelectionArrayindex[0])
            }}
           
            
            
          />
        </div>
        <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={style}>
            <form onSubmit={uploadData}>
                <div className="relative z-0 mb-6 w-full group justify-center">
                <h2 className="justify-center text-blue-800 font-medium">Add Doctor</h2>
                </div>
              <div className="relative z-0 mb-6 w-full group">
                <input
                  type="text"
                  value={details.name}
                  onChange={onHandlechange}
                  name="name"
                  id="name"
                  className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=""
                  required
                />
                <label
                  htmlFor="name"
                  className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >
                  Name
                </label>
              </div>
              <div className="relative z-0 mb-6 w-full group">
                <input
                value={details.date_of_join}
                onChange={onHandlechange}
                  type="date"
                  name="date_of_join"
                  id="date_of_join"
                  className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=""
                  required
                />
                <label
                  htmlFor="floating_repeat_password"
                  className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >
                  Date of join
                </label>
              </div>
              <div className="grid md:grid-cols-2 md:gap-6">
                <div className="relative z-0 mb-6 w-full group">
                  <input
                  value={details.bloodGroup}
                  onChange={onHandlechange}
                    type="text"
                    name="bloodGroup"
                    id="blood_Group"
                    className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=" "
                    required
                  />
                  <label
                    htmlFor="floating_first_name"
                    className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >
                    Blood Group
                  </label>
                </div>
                <div className="relative z-0 mb-6 w-full group">
                  <input
                    value={details.age}
                    onChange={onHandlechange}
                    type="text"
                    name="age"
                    id="age"
                    className="block py-2.5 px-0 w-full text-sm  bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=""
                    required
                  />
                  <label
                    htmlFor="floating_last_name"
                    className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >
                    Age
                  </label>
                </div>
              </div>
              <div className="grid md:grid-cols-2 md:gap-6">
                <div className="relative z-0 mb-6 w-full group">
                  <input
                    type="tel"
                    onChange={onHandlechange}
                    name="phonenumber"
                    id="phonenumber"
                    className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=""
                    required
                  />
                  <label
                    htmlFor="floating_phone"
                    className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >
                    Phone number (123-456-7890)
                  </label>
                </div>
                <div className="relative z-0 mb-6 w-full group">
                <FormControl variant="standard" sx={{ m: 1, minWidth: 200 }}>
                    <InputLabel id="demo-simple-select-standard-label">Status</InputLabel>
                    <Select
                    name="status"
                    labelId=""
                    id=""
                    value={age}
                    onChange={onHandlechange}
                    
                    label="Status"
                    >
                    <MenuItem value="new">
                        <em>None</em>
                    </MenuItem>
                    <MenuItem value="Senior">Senior</MenuItem>
                    <MenuItem value="HeadNurse">HeadNurse</MenuItem>
                    </Select>
                </FormControl>
                </div>
                <div className="relative z-0 mb-6 w-full group">
                  
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-black" htmlFor="large_size">image</label>
                    <input onChange={handleImageChange} className="block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-black focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="large_size" name="image" type="file"/>

                </div>
                
              </div>
              <button
                type="submit"
                className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              >
                Submit
              </button>
            </form>
          </Box>
        </Modal>


{/* editform.................................. */}



        <Modal open={modalOpen} onClose={handleClosee}>
        <Box sx={style}>
        <form >
                <div className="relative z-0 mb-6 w-full group justify-center">
                <h2 className="justify-center text-blue-800 font-medium">Add Doctor</h2>
                </div>
              <div className="relative z-0 mb-6 w-full group">
                <input
                  type="text"
                  value={detailsupdate.name}
                  onChange={onUpdatechange}
                  name="name"
                  id="name"
                  className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=""
                  
                />
                <label
                  htmlFor="name"
                  className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >
                  Name
                </label>
              </div>
              <div className="relative z-0 mb-6 w-full group">
                <input
                value={detailsupdate.date_of_join}
                onChange={onUpdatechange}
                  type="date"
                  name="date_of_join"
                  id="date_of_join"
                  className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=""
                  
                />
                <label
                  htmlFor="floating_repeat_password"
                  className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >
                  Date of join
                </label>
              </div>
              <div className="grid md:grid-cols-2 md:gap-6">
                <div className="relative z-0 mb-6 w-full group">
                  <input
                  value={detailsupdate.bloodGroup}
                  onChange={onUpdatechange}
                    type="text"
                    name="bloodGroup"
                    id="blood_Group"
                    className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=" "
                    
                  />
                  <label
                    htmlFor="floating_first_name"
                    className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >
                    Blood Group
                  </label>
                </div>
                <div className="relative z-0 mb-6 w-full group">
                  <input
                    value={detailsupdate.age}
                    onChange={onUpdatechange}
                    type="text"
                    name="age"
                    id="age"
                    className="block py-2.5 px-0 w-full text-sm  bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=""
                    
                  />
                  <label
                    htmlFor="floating_last_name"
                    className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >
                    Age
                  </label>
                </div>
              </div>
              <div className="grid md:grid-cols-2 md:gap-6">
                <div className="relative z-0 mb-6 w-full group">
                  <input
                    type="tel"
                    onChange={onUpdatechange}
                    name="phonenumber"
                    id="phonenumber"
                    value={detailsupdate.phonenumber}
                    className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=""
                    
                  />
                  <label
                    htmlFor="floating_phone"
                    className="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >
                    Phone number (123-456-7890)
                  </label>
                </div>
                <div className="relative z-0 mb-6 w-full group">
                <FormControl variant="standard" sx={{ m: 1, minWidth: 200 }}>
                    <InputLabel id="demo-simple-select-standard-label">Status</InputLabel>
                    <Select
                    name="status"
                    labelId=""
                    id=""
                    value={age}
                    onChange={onUpdatechange}
                    
                    label="Status"
                    >
                    <MenuItem value="">
                        <em>None</em>
                    </MenuItem>
                    <MenuItem value="Senior">Senior</MenuItem>
                    <MenuItem value="HeadNurse">HeadNurse</MenuItem>
                    </Select>
                </FormControl>
                </div>
                <div className="relative z-0 mb-6 w-full group">
                  
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-black" htmlFor="large_size">image</label>
                    <input onChange={handleImageChangee} className="block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-black focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="large_size" name="image" type="file"/>

                </div>
                
              </div>
              <button
                type="submit" onClick={(e)=>uploadUpdated(e,selectionid)}

                className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              >
                Submit
              </button>
            </form>
        </Box>
      </Modal>

      </div>
    </div>
  );
}
