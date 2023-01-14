import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import AuthContext from "../context/AuthContext";

export default function Patients() {
    const [data, setData] = useState([])
    const {authTokens} = useContext(AuthContext)
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/patients/patientlist/").then((response) => {
            setData(response.data)
        })
    }, []);
  return (
    <div className=" ml-72 min-h-[800px] bg-slate-300 rounded-md w-[1500px] grid gap-x-6 gap-y-4 grid-cols-1 content-center mt-3">
      <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
        List of Patients
      </h1>
      <div className="justify-self-end">
        <button className="bg-fuchsia-600 w-36 rounded-full text-white flex hover:bg-blue-600 justify-center mr-8 ">
          Add Patient
        </button>
      </div>
      <table class="p-5 w-full   text-sm text-left text-gray-500 dark:text-gray-400">
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
                    {list.doctors}
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
  );
}
