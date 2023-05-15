// import { LockClosedIcon } from '@heroicons/react/20/solid'
import { useContext } from 'react'
import './Signin.css'
import { useForm } from "react-hook-form";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import AuthContext from '../../context/AuthContext';


export default function Signin() {
  const {loginUser} =useContext(AuthContext)
  const{register,handleSubmit,formState: { errors },}=useForm()

  const registerOptions = {
    username: { required: "username is required" },
    password: {
      required: "Password is required",
      minLength: {
        value: 6,
        message: "Password will have at least 6 characters",
      },
    },
  };
  return (
    <div className='flex items-center justify-center h-screen bg-fuchsia-900'>

      <form onSubmit={handleSubmit(loginUser)}>
          <div className='bg-fuchsia-600 w-95 p-6 rounded shadow-sm' >
            <div className='flex items-center justify-center pb-10'>
              <h1 className='text-white text-bold'>Admin LOGIN</h1>
            </div>
            <label htmlFor='username' className='text-white'>Username</label>
            <input className='w-full py-2 bg-gray-50 text-grey-500 rounded px-1 outline-none mb-4' typeof='email' name='username' placeholder='email' {...register("username", registerOptions.username)}></input>
            <small className="text-danger">
          {errors?.email && errors.username.message}
        </small>
            <label htmlFor='password' className='text-white'>Password</label>
            <input className='w-full py-2 bg-gray-50 text-grey-500 rounded px-1 outline-none mb-4' typeof='password' name='password' placeholder='password' {...register("password", registerOptions.password)}></input>
            <small className="text-danger">
          {errors?.password && errors.password.message}
        </small>
            <div className='flex items-center justify-center'>
            <button type='submit' className="bg-white hover:bg-purple text-purple font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
              Login
            </button>
            </div> 
          </div>
      </form>
    </div>
  )
}