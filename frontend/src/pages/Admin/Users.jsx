import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import { Outlet } from "react-router";
import { useForm } from "react-hook-form";
import { toast } from 'react-toastify';
import AuthContext from "../../context/AuthContext";

export default function Users() {
  const [data, setData] = useState([]);
  const { register, handleSubmit, watch, formState: { errors } } = useForm();
  const [formData, setFormData] = useState({});
  const {authTokens} = useContext(AuthContext)


  useEffect(() => {
    User();
  }, []);

  async function User() {
    await axios.get("http://127.0.0.1:8000/user/listuser/").then((response) => {
      setData(response.data);
    });
  }

  useEffect(() => {
    async function postData() {
        try {
            const response = await axios.post("http://127.0.0.1:8000/user/register/", formData, {
                      method: "POST",
                      headers: {
                        "Content-Type": "multipart/form-data",
                        "Authorization": `Bearer ${
                          authTokens.access
                      }`
                      },}).then((res)=>{
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
                               User();
                      })
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    }
    if(Object.keys(formData).length !== 0) postData();
}, [formData]);

const onSubmit = (data) => {
  console.log(data)
    setFormData(data);
};

const deleteFunction=(id)=>{
  axios.delete(`http://127.0.0.1:8000/user/deleteuser/${id}/`,{
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data",
      "Authorization": `Bearer ${
        authTokens.access
    }`
    },}).then((res)=>{
    console.log(res)
    console.log("wrk");
    if (res.status === 200){
      toast.success('Deleted ! ',{
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "colored",
      });
      User();
    }
    else{
      toast.error('Unauthorized ! ',{
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "colored",
      });
    }
  })
  
}



  const registerOptions = {
    username: { required: "Name is required" },
    email: {
      required: "Email is required.",
      pattern: {
        value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
        message: "Email is not valid.",
      },
    },
    password: {
      required: "Password is required",
      minLength: {
        value: 8,
        message: "Password must have atleast 8 characters",
      },
    },
    password2: {
      required: "Re-enter password",
      minLength: {
        message: "Password must be equal",
      },
    },
  };
  return (
    <div>
      <div className=" ml-72 min-h-[800px] bg-slate-300 rounded-md w-[1500px] grid gap-x-6 gap-y-4 grid-cols-2 content-center mt-3">
        <div className="ml-32 rounded-md bg-gray-300 h-[700px]  ">
          <h1 className="flex justify-center mt-4 text-2xl font-bold text-purple-600">
            List of Users
          </h1>
          <div className=" mt-20 overflow-x-hidden relative shadow-md sm:rounded-lg ">
            <table className="w-full  text-sm text-left text-gray-500 dark:text-gray-400">
              <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                  <th scope="col" className="py-3 px-6">
                    Username
                  </th>
                  <th scope="col" className="py-3 px-6">
                    Role
                  </th>
                  <th scope="col" className="py-3 px-6">
                    Action
                  </th>
                </tr>
              </thead>
              <tbody>
                {data.map((user, index) => {
                  return (
                    <tr className="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                      <th
                        scope="row"
                        className="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                      >
                        {user.username}
                      </th>
                      <td className="py-4  px-6">
                        {user.is_superuser === false ? (
                          <div className="w-[100px] h-[30px] text-center bg-yellow-600 text-white rounded">
                            Admin
                          </div>
                        ) : (
                          <div className="w-[100px] h-[30px]  bg-green-700 text-center text-white rounded">
                            SuperAdmin
                          </div>
                        )}
                      </td>

                      <td className="py-4 px-6">
                        <button onClick={()=>deleteFunction(user.id)}
                          className="w-[100px] h-[30px]  bg-red-800 text-center text-white rounded "
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>

        <div className="rounded-md bg-blue-600 w-[700px]">
          <div className="flex flex-col items-center min-h-full pt-6 sm:justify-center sm:pt-0 bg-gray-200 rounded">
            <div>
              <a href="/">
                <h3 className="text-4xl font-bold text-purple-600">
                  Create User
                </h3>
              </a>
            </div>
            <div className="w-full px-6 py-4 mt-6 overflow-hidden bg-gray-400 shadow-md sm:max-w-md sm:rounded-lg">
              <form onSubmit={handleSubmit(onSubmit)}>
                <div>
                  <label
                    htmlFor="name"
                    className="block text-sm font-medium text-gray-700 undefined"
                  >
                    Username
                  </label>
                  <div className="flex flex-col items-start">
                    <input {...register("username",registerOptions.username)}
                    aria-invalid={errors.username ? "true" : "false"}
                      type="text"
                      name="username"
                      className="block w-full mt-1 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    />
                    {errors.username?.type === 'required' && <p role="alert">Username is required</p>}
                  </div>
                </div>
                <div className="mt-4">
                  <label
                    htmlFor="email"
                    className="block text-sm font-medium text-gray-700 undefined"
                  >
                    Email
                  </label>
                  <div className="flex flex-col items-start">
                    <input  {...register("email" ,registerOptions.email)}
                    aria-invalid={errors.mail ? "true" : "false"} 

                      type="email"
                      name="email"
                      className="block w-full mt-1 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    />
                    {errors.mail && <p role="alert">{errors.mail?.message}</p>}

                  </div>
                </div>
                <div className="mt-4">
                  <label
                    htmlFor="password"
                    className="block text-sm font-medium text-gray-700 undefined"
                  >
                    Password
                  </label>
                  <div className="flex flex-col items-start">
                    <input {...register("password" , registerOptions.password)}
                      type="password"
                      name="password"
                      className="block w-full mt-1 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    />{errors.password && <p>{errors.password.message}</p>}
                  </div>
                </div>
                <div className="mt-4">
                  <label
                    htmlFor="password_confirmation"
                    className="block text-sm font-medium text-gray-700 undefined"
                  >
                    Confirm Password
                  </label>
                  <div className="flex flex-col items-start">
                    <input {...register("password2" ,registerOptions.password2)}
                      type="password"
                      name="password2"
                      className="block w-full mt-1 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    />{errors.password2 && <p>{errors.password2.message}</p>}
                  </div>
                </div>
                <div className="flex items-center justify-center mt-4">
                  <button
                    type="submit"
                    className="inline-flex items-center px-4 py-2 ml-4 text-xs font-semibold tracking-widest text-white uppercase transition duration-150 ease-in-out bg-fuchsia-800 hover:bg-fuchsia-500 border border-transparent rounded-md active:bg-gray-900 false"
                  >
                    Create
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
        <Outlet />
      </div>
    </div>
  );
}
