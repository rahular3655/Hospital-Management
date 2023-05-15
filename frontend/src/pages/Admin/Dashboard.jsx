import React from 'react'
// import Navbar from '../Components/Navbar'
// import Sidebar from '../Components/Sidebar'
// import { Outlet } from 'react-router'

export default function Dashboard() {
  return (
    <div>
      <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
        <div className=" bg-slate-300 w-full rounded-md ">
          <div className='grid grid-cols-4 justify-items-center gap-3 px-2 pt-5 md:justify-items-center '>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Users</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Doctors</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Nurse</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Patients</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Bills</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Bed</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Infrastrucute</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Staffs</div>
          </div>
        </div>
      </div>
    </div>
  )
}
