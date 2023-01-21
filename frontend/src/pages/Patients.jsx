import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import AuthContext from "../context/AuthContext";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import { useForm } from "react-hook-form";
import { Input } from "@material-tailwind/react";

export default function Patients() {
    const [data, setData] = useState([])
    const handleOpen = () => setOpen(true);
    const [open, setOpen] = React.useState(false);
    const handleClose = () => setOpen(false);
    const {authTokens} = useContext(AuthContext)
    const { handleSubmit, register, formState: { errors }} = useForm();
    const [formData, setFormData] = useState({});
    const style = {
        position: "absolute",
        top: "50%",
        left: "50%",
        transform: "translate(-50%, -50%)",
        width: 800,
        bgcolor: "background.paper",
        border: "1px solid #000",
        boxShadow: 24,
        p: 4,
      };
      const registerOptions = {
        name: { required: "Patient Name is required" ,minLength: {
            value: 6,
            message: "Name must have at least 8 characters",
          },},
        address: { required: "Address is required" },
        age: { required: "Age is required" },
        medicalcondition:{required: "Condition is required"}
      };

      const patientDetails = async data => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/patients/patientcreate/', data,{
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization": `Bearer ${
                    authTokens.access
                }`
                },}).then((response)=>{
                    if (response.status===201){
                        handleClose(true)

                    }
                })
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };
   

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/patients/patientlist/").then((response) => {
            setData(response.data)
        })
    }, []);



  return (
    <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
        <div className=" bg-slate-300 w-full rounded-md ">
      <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
        List of Patients
      </h1>
      <div className="">
        <button onClick={handleOpen} className="bg-fuchsia-600 w-36 rounded-full text-white flex hover:bg-fuchsia-400 justify-center mr-8 ">
          Add Patient
        </button>
      </div>
      <table class="p-5 w-full text-sm text-left  text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">
                    id
                </th>
                <th scope="col" class="px-6 py-3">
                    Name
                </th>
                <th scope="col" class="px-6 py-3">
                    Status
                </th>
                <th scope="col" class="px-6 py-3">
                    Date
                </th>
                <th scope="col" class="px-6 py-3">
                    Doctor
                </th>
                <th scope="col" class="px-6 py-3">
                    Action
                </th>
            </tr>
        </thead>
        <tbody>
            {data.map((list,id)=>{
                return(

              
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {id+1}
                </th>
                <td class="px-6 py-4">
                    {list.name}
                </td>
                <td class="px-6 py-4">
                    {list.status}
                </td>
                <td class="px-6 py-4">
                    {list.time}
                </td>
                <td class="px-6 py-4">
                    {list.doctors.length===0 ? <button className="w-[120px] h-[30px] bg-teal-600 text-white rounded">Assign Doctor</button>:<span>{list.doctors.map((doc,index)=>
                    {
                        return(<span>{doc.name}</span>)
                    })}</span>}
                </td>
                <td class="flex gap-2 px-6 py-4">
                    <button className="w-[30px] h-[30px] bg-teal-600 text-white rounded"> Edit</button>
                    <button className="w-[50px] h-[30px] align-middle text-white bg-red-500 rounded"> Delete</button>
                    <button className="w-[120px] h-[30px]  text-white rounded bg-yellow-600">Medical Condition</button>
                </td>
            </tr>
              )
            })}
            
        </tbody>
    </table>
    </div>
    <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={style}>
            <form onSubmit={handleSubmit(patientDetails)}>
                <div className="relative z-0 mb-6 w-full group justify-center">
                <h2 className="justify-center text-blue-800 font-medium">Enter the patients details</h2>
                </div>
              <div className="relative z-0 mb-6 w-full group flex  flex-col gap-4">
                <Input {...register("name", registerOptions.name)}
                  color="blue" variant="outlined" label="Name of the patient" name="name"
                  require placeholder="Patient Name"
                />
                <small className="text-red-500">
            {errors?.name && errors.name.message}
          </small>
              </div>
              <div className="relative z-0 mb-6 w-full group">
                <Input {...register("address",registerOptions.address)}
                    color="blue" label="Address of the patient"
                  required placeholder="Address"
                />
                <small className="text-red-500">
                {errors?.address}</small>
              </div>
              <div className="relative z-0 mb-6 w-full group">
                <Input {...register("medical_condition",registerOptions.medicalcondition)}
                    color="blue" label="Medical condition of the patient"
                  required
                  placeholder="Medical Condition"
                />
                <small className="text-red-500">
                {errors?.medicalcondition}</small>
              </div>
              <div className="grid md:grid-cols-2 md:gap-6">
                
                <div className="relative z-0 mb-6 w-full group">
                  <Input {...register("age")}
                    color="blue" label="Age of the patient"
                    required
                    placeholder="Age"
                  />
                  
                </div>
              </div>
              <div className="grid md:grid-cols-2 md:gap-6">
                <div className="relative z-0 mb-6 w-full group">
                  <Input {...register("phone")}
                  color="blue" label="Phonenumber of the patient"
                    required
                    placeholder="Phone number"
                  />
                  
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
    </div>
  );
}
