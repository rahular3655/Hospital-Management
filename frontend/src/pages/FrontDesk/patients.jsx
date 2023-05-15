import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import { useForm } from "react-hook-form";
import { Input } from "@material-tailwind/react";
import { toast } from "react-toastify";
import DeskAuthContext from "./DeskContext/DeskAuthContext";

export default function Patients() {
  const baseUrl = "http://127.0.0.1:8000/patients/patientlist/";
  const [data, setData] = useState([]);
  const handleOpen = () => setOpen(true);
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);
  const { authTokens } = useContext(DeskAuthContext);
  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm();
  const [formData, setFormData] = useState({});
  const [prevUrl, setprevUrl] = useState();
  const [nextUrl, setnextUrl] = useState();
  const [reload, setReload] = useState(0);
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
    name: {
      required: "Patient Name is required",
      minLength: {
        value: 6,
        message: "Name must have at least 8 characters",
      },
    },
    address: { required: "Address is required" },
    age: { required: "Age is required" },
    medicalcondition: { required: "Condition is required" },
  };

  const patientDetails = async (data) => {
    try {
      const response = await axios
        .post("http://127.0.0.1:8000/patients/patientcreate/", data, {
          method: "POST",
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${authTokens.access}`,
          },
        })
        .then((response) => {
          if (response.status === 201) {
            handleClose(true);
          }
        });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    try {
      axios.get(baseUrl).then((response) => {
        setnextUrl(response.data.next);
        setprevUrl(response.data.previous);
        setData(response.data.results);
      });
    } catch (error) {
      console.log(error);
    }
  }, [reload]);

  const paginationHandler = (url) => {
    try {
      axios.get(url).then((response) => {
        setData(response.data.results);
        setnextUrl(response.data.next);
        setprevUrl(response.data.previous);
      });
    } catch (error) {
      console.log(error);
    }
  };

  const deleteFuntion = (id) => {
    axios
      .delete(`http://127.0.0.1:8000/patients/deletepatient/${id}/`, {
        method: "POST",
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${authTokens.access}`,
        },
      })
      .then((response) => {
        if (response.status === 200) {
          setReload(Math.random() * Math.random());
          toast.success("Deleted ! ", {
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
      });
  };
  return (
    <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
      <div className=" bg-slate-300 w-full rounded-md ">
        <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
          List of Patients
        </h1>
        <div className="flex justify-end mb-3">
          <button
            onClick={handleOpen}
            className="bg-fuchsia-600 w-36 rounded-full text-white flex hover:bg-fuchsia-400 justify-center mr-8 "
          >
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
            {data.map((list, id) => {
              return (
                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                  <th
                    scope="row"
                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    {id + 1}
                  </th>
                  <td class="px-6 py-4">{list.name}</td>
                  <td class="px-6 py-4">{list.status}</td>
                  <td class="px-6 py-4">{list.time}</td>
                  <td class="px-6 py-4">
                    {list.doctors.length === 0 ? (
                      <button className="w-[120px] h-[30px] bg-teal-600 text-white rounded">
                        Assign Doctor
                      </button>
                    ) : (
                      <span>
                        {list.doctors.map((doc, index) => {
                          return <span>{doc.name}</span>;
                        })}
                      </span>
                    )}
                  </td>
                  <td class="flex gap-2 px-6 py-4">
                    <button className="w-[50px] h-[30px] bg-teal-600 text-white rounded">
                      {" "}
                      Admit
                    </button>
                    <button className="w-[50px] h-[30px] bg-teal-800 text-white rounded">
                      {" "}
                      Edit
                    </button>
                    <button
                      onClick={() => deleteFuntion(list.id)}
                      className="w-[50px] h-[30px] align-middle text-white bg-red-500 rounded"
                    >
                      Bills
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {/* pagination............................................ */}
        <div className="flex justify-center">
          {prevUrl && (
            <button
              onClick={() => paginationHandler(prevUrl)}
              className="inline-flex  px-4 py-2 mr-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
            >
              <svg
                aria-hidden="true"
                className="w-5 h-5 mr-2"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              Previous
            </button>
          )}
          {nextUrl && (
            <button
              onClick={() => paginationHandler(nextUrl)}
              className="inline-flex  px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
            >
              Next
              <svg
                aria-hidden="true"
                className="w-5 h-5 ml-2"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
          )}
        </div>
        {/* pagination end............................... */}
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
              <h2 className="justify-center text-blue-800 font-medium">
                Enter the patients details
              </h2>
            </div>
            <div className="relative z-0 mb-6 w-full group flex  flex-col gap-4">
              <Input
                {...register("name", registerOptions.name)}
                color="blue"
                variant="outlined"
                label="Name of the patient"
                name="name"
                require
                placeholder="Patient Name"
              />
              <small className="text-red-500">
                {errors?.name && errors.name.message}
              </small>
            </div>
            <div className="relative z-0 mb-6 w-full group">
              <Input
                {...register("address", registerOptions.address)}
                color="blue"
                label="Address of the patient"
                required
                placeholder="Address"
              />
              <small className="text-red-500">{errors?.address}</small>
            </div>
            <div className="relative z-0 mb-6 w-full group">
              <Input
                {...register(
                  "medical_condition",
                  registerOptions.medicalcondition
                )}
                color="blue"
                label="Medical condition of the patient"
                required
                placeholder="Medical Condition"
              />
              <small className="text-red-500">{errors?.medicalcondition}</small>
            </div>
            <div className="grid md:grid-cols-2 md:gap-6">
              <div className="relative z-0 mb-6 w-full group">
                <Input
                  {...register("age")}
                  color="blue"
                  label="Age of the patient"
                  required
                  placeholder="Age"
                />
              </div>
            </div>
            <div className="grid md:grid-cols-2 md:gap-6">
              <div className="relative z-0 mb-6 w-full group">
                <Input
                  {...register("phone")}
                  color="blue"
                  label="Phonenumber of the patient"
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
