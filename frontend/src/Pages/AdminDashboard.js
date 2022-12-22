import React from "react";
import Nav from "../Components/Navbar";
import Sidebar from "../Components/Sidebar";

const AdminHome = ()=>{
    return(
        // <section className="flex gap-6">
        //     <Sidebar/>
        //     <Nav/>
        // </section>

<div class="grid grid-rows-3 grid-flow-col gap-2">
<div class="row-span-3   bg-red-700 ...">
    <Sidebar/></div>
<div class="col-span-2 bg-red-300 "><Nav/></div>
<div class="row-span-2 col-span-2 bg-red-800 ...">03</div>
</div>
    )
};

export default AdminHome