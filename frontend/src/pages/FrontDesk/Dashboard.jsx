import React from 'react'

export default function DeskDashboard() {
  return (
    <div>
      <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
        <div className=" bg-slate-300 w-full rounded-md ">
          <div className='grid grid-cols-4 justify-items-center gap-3 px-2 pt-5 md:justify-items-center '>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Doctors</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Patients</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Bills</div>
            <div className='bg-teal-700 h-40 rounded w-48 text-center text-white font-semibold pt-14'>Staffs</div>
          </div>
        </div>
      </div>
    </div>
  )
}
