import { Typography , Box, useTheme } from "@mui/material";
import { tokens } from "../theme";

 const Headers=({title,subtitle})=>{
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return <Box>
        <Typography varient ="h2" color={colors.grey[100]} fontWeight="bold" sx={{mb:"5px"}}>{title}</Typography>
        <Typography varient ="h5" color={colors.greenAccent[400]}>{subtitle}</Typography>
    </Box>
}

export default Headers 