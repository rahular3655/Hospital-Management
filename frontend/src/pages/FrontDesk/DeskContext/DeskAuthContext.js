import {createContext , useState , useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import { toast } from 'react-toastify';
import axios from "axios";
import jwt_decode from "jwt-decode";


const DeskAuthContext = createContext()

export default DeskAuthContext; 


export const DeskAuthProvider = ({children}) => {
    let [authTokens, setAuthTokens] = useState(()=> localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null);
    let [admin, setAdmin] = useState(()=> localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null);
    let [loading, setLoading] = useState(true);
    const Navigate = useNavigate ()


    let loginUser = async (e) => {
        
        console.log("loged in......");
        let response = await fetch("http://127.0.0.1:8000/user/login/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            
          },
          body: JSON.stringify({
            username: e.username,
            password: e.password,
          }),
        });
    


        let data = await response.json();

        if(response.status === 200){
            console.log("logged in succekkkkkkkkkkkkkkkkkkkkkkkkss")
            setAuthTokens(data)
            setAdmin(jwt_decode(data.access))
            console.log("logged in sytfuygu76t",jwt_decode(data.access).is_superuser)
            console.log('daiuhfihrufh9ehy9',admin,"jjjjjjjjjjjjjjjjjjj")

            localStorage.setItem("authTokens", JSON.stringify(data));
            if(jwt_decode(data.access).role==="FRONT-DESK"){

              toast.success('You have successfully logged in ! ',{
                position: "top-right",
                autoClose: 3000,
                hideProgressBar: true,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
                theme: "colored",
              });
              Navigate('/deskhome')

            }
            else{
              toast.success('You have successfully uuuuuuuuuuuuuuu logged in ! ',{
                position: "top-right",
                autoClose: 3000,
                hideProgressBar: true,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
                theme: "colored",
              });
              Navigate('/deskhome')
            }
        }else{
          toast.error('Invalid Credentials', {
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
      };

      let updateToken = async () => {
        console.log("update token......");
        let response = await fetch("http://127.0.0.1:8000/user/login/refresh/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            
          },
          body: JSON.stringify({ 'refresh': authTokens?.refresh })
        });
        let data = await response.json();
        if (response.status === 200) {
          setAuthTokens(data);
          setAdmin(jwt_decode(data.access));
          localStorage.setItem("authTokens", JSON.stringify(data));
        } else {
            logoutDesk();
        }
        if (loading) {
          setLoading(false)
        }
      };


      let logoutDesk = () => {
        setAuthTokens(null)
        setAdmin(null)
        localStorage.removeItem('authTokens')
        // Navigate('/frontdesksignin')
    }



    useEffect(()=> {

      console.log("looook here");
        if(loading){
            updateToken()
        }

        let fourMinutes = 1000 * 60 * 4

        let interval =  setInterval(()=> {
            if(authTokens){
                updateToken()
              //  updateAdminToken()
            }
        }, fourMinutes)
        return ()=> clearInterval(interval)

    }, [authTokens, loading])


      let contextData ={
        admin:admin,
        authTokens:authTokens,
        loginUser:loginUser,
        logoutDesk:logoutDesk,
      }

      return(
        <DeskAuthContext.Provider value={contextData} >
            {loading ? null : children}
        </DeskAuthContext.Provider>
    )
}
