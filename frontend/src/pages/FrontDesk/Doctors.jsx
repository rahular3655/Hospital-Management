import axios from "axios";
import React, { useContext, useEffect, useState } from "react";
import DeskAuthContext from "./DeskContext/DeskAuthContext";

export default function DeskDoctors() {
    const [prevUrl,setprevUrl]=useState()
    const [nextUrl,setnextUrl]=useState()
    const [data, setData] = useState([])
    const {authTokens} = useContext(DeskAuthContext)



    const doctorList=async data=>{
        try{ 
            axios.get("http://127.0.0.1:8000/staffs/fddoctorlist/", {
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `Bearer ${authTokens.access}`,
                },
              }).then((response) => {
                
                    setnextUrl(response.data.next)
                    setprevUrl(response.data.previous)
                setData(response.data.results)
            })
            }catch(error){
                console.log(error)
            }
            }

    const paginationHandler=(url)=>{
        try{ 
            axios.get(url).then((response) => {
                setData(response.data.results)
                setnextUrl(response.data.next)
                setprevUrl(response.data.previous)
            })
            }catch(error){
                console.log(error)
            }
    }

    useEffect(()=>{
      doctorList()
      paginationHandler()
    },[])
  return (
    <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
      <div className=" bg-slate-300 w-full rounded-md ">
        <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
          List of Doctors
        </h1>
        <div className="grid grid-cols-4 justify-items-center gap-3 px-2 pt-5 md:justify-items-center ">
          {/* <div className=" bg-slate-300 w-full rounded-md ">
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Doctors</div> */}
            {data.map((list,id)=>{return(
          <div className="w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <div className="flex flex-col items-center pb-10">
              <img
                className="w-24 h-24 mb-3 rounded-full shadow-lg mt-5"
                src={list.image}
                alt="Bonnie image"
              />
              <h5 className="mb-1 text-xl font-medium text-gray-900 dark:text-white">
                {list.name}
              </h5>
              <span className="text-sm font-bold text-gray-500 dark:text-gray-400">
                {list.specialized_in}
              </span>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                {list.status}
              </span>
              <span className="text-sm text-gray-500 dark:text-gray-400">
               Ph: {list.phonenumber}
              </span>
            </div>
          </div>
        )})}
        </div>
        <div className="flex justify-center">
            {prevUrl && 
            <button onClick={()=>paginationHandler(prevUrl)} className="inline-flex  px-4 py-2 mr-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                <svg aria-hidden="true" className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
            Previous
            </button>
            }
            {nextUrl && 
            <button onClick={()=>paginationHandler(nextUrl)} className="inline-flex  px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            Next
                <svg aria-hidden="true" className="w-5 h-5 ml-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            </button>
            }
        </div>
      </div>
    </div>
    // </div>
  );
}
