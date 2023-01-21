import React, { Fragment, useEffect, useState } from "react";
import axios from "axios";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";

export default function Beds() {
  const [data, setData] = useState([]);
  const[count,setCount] = useState([]);
  const [open, setOpen] = React.useState(false);
  const [expanded, setExpanded] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setModalOpen('');
  const [modalOpen, setModalOpen] = useState('');

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

  useEffect(() => {
    Blocklist()
    Countof()
  }, []);

  async function Blocklist(){
    await axios
    .get("http://127.0.0.1:8000/infrastructure/blocklist/")
    .then((response) => {
      setData(response.data);
    });
  } 

  async function Countof(){
    await axios
    .get("http://127.0.0.1:8000/infrastructure/countof/")
    .then((response) => {
      setCount(response.data);
    });
  }
  return (
    <div>
      <div className=" ml-72 min-h-[800px] flex  mt-3 p-4">
        <div className=" bg-slate-300 w-full rounded-md ">
          <h1 className="flex justify-center  text-2xl font-bold text-blue-800">
            List of Beds
          </h1>
          <div className="grid col-6">
            <div className="px-5 grid grid-cols-2 gap-4">
              {data.map((item, id) => {
                return (
                  <div
                    key={id}
                    className={`border rounded ${
                      expanded === id ? "bg-gray-200" : "bg-white"
                    }`}
                  >
                    <h2 className="accordion-header mb-0" id="headingOne">
                      <button
                        className="
                        accordion-button
                        relative
                        flex
                        items-center
                        w-full
                        py-4
                        px-5
                        text-base font-bold text-fuchsia-800 text-left
                        bg-white
                        border-0
                        rounded-none
                        transition
                        focus:outline-none
                      "
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#collapseOne"
                        aria-expanded="true"
                        aria-controls="collapseOne"
                      >
                        Block : {item.name}
                      </button>
                    </h2>
                    <div className="mx-auto p-5">
                      <div className="">
                        {item.floor.length === 0 ? (
                          <button className="w-[120px] h-[30px] bg-blue-800 text-white rounded">
                            No Floors
                          </button>
                        ) : (
                          <span className="flex justify-center">
                            <div className="grid grid-cols-3 gap-4 ">
                              {item.floor.map((doc, index) => {
                                return (
                                  <Modalbutton key={index} data={doc}/>
                                  
                                );
                                
                              })}
                              
                            </div>
                            
                          </span>
                          
                        )}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
          <div className="flex justify-center pt-8">
            <div className="grid w-[600px] h-auto bg-slate-400 rounded">
        <span className="text-red-700 font-medium">Total Beds : {count.totalbed}</span><span className="text-red-700 font-medium">Available Beds :{count.availablebed}</span><span className="text-red-700 font-medium">Allotted Beds : {count.unavailablebed}</span>
        </div>
      </div>
        </div>
        
      </div>
              
    </div>
  );
  function Modalbutton(props){

    return(

        <div key={props.key}>
        <button onClick={()=>{setModalOpen(props.data.name)}}
                                    className="w-[160px] h-[50px] bg-fuchsia-700 text-white rounded"
                                  >
                                    {props.data.name}
                                  </button>
        <Modal
        open={modalOpen=== props.data.name? true:false}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        >
        <Box sx={style}>
              <div className="grid grid-cols-4 gap-4">
              {props.data.bed.map((bed,index)=>{
                return(
                    <div>
                    {bed.is_available=== false ? (<button className="w-[100px] h-[50px] bg-yellow-600 text-white rounded">{bed.name}</button>):(<button className="w-[100px] h-[50px] bg-green-800 text-white rounded">{bed.name}</button>)}
                    </div>
                    
                )
              })}
              </div>
      </Box>
      </Modal>
      
          </div>
          
    )
  }
}
