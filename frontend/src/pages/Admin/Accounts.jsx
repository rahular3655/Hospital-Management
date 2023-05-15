import React from 'react'

export default function Accounts() {
  return (
    <div>
      <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
        <div className=" bg-slate-300 w-full  rounded-md ">
          <div className="grid grid-rows-2 grid-flow-row gap-4">
            <div className=" min-w-[300px]">
              <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
                List of Patients
              </h1>
              <div className="flex justify-end mb-3">
                <button className="bg-fuchsia-600 w-36 rounded-full text-white flex hover:bg-fuchsia-400 justify-center mr-8 ">
                  Add Patient
                </button>
              </div>
            </div>
            <div className=" flex px-6">
              <table class="p-5 w-full h-full text-sm text-left  text-gray-500 dark:text-gray-400">
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
                      Date of installation
                    </th>
                    <th scope="col" class="px-6 py-3">
                      floor 
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Action
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                    <th
                      scope="row"
                      class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                    ></th>
                    <td class="px-6 py-4"></td>
                    <td class="px-6 py-4"></td>
                    <td class="px-6 py-4"></td>
                    <td class="px-6 py-4"></td>
                    <td class="flex gap-2 px-6 py-4">
                      <button className="w-[30px] h-[30px] bg-teal-600 text-white rounded">
                        Edit
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
