import { Box } from '@mui/system'
import React from 'react'
import Headers from "../../src/Components/Headers"

const Dashhboard = () => {
  return (
    <Box m="20px">
        <Box display="flex" justifyContent= "space-between" alignItems="center">
            <Headers title="Dashboard" subtitle="Welcome to admin dashboard"/>
        </Box>
    </Box>
  );
};

export default Dashhboard
