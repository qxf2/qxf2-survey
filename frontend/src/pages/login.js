import React, { useState } from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import "../Login.css";
import url_conf from "./data/urlConf";

const clientId = process.env.REACT_APP_CLIENT_ID;

export default function Login({Login}) {

    const [showloginButton, setShowloginButton] = useState(true);
    const [showlogoutButton, setShowlogoutButton] = useState(false);
    const [unauthorized, setUnauthorized] = useState(false);
    const [useremail, setUseremail] = useState(null);
    const onLoginSuccess = (res) => {
        var id_token = res.getAuthResponse().id_token;
        setUseremail(res.profileObj.email)
        setShowloginButton(false);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', `${url_conf}/survey/admin/admin-login`);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('User', process.env.REACT_APP_API_KEY);
        xhr.onload = function() {
          if(xhr.status === 200){
            const login_status = true
            Login(login_status, res.profileObj.email);
          }
          else{
              setUnauthorized(true)
          }
        };
        xhr.send('idtoken=' + id_token);
        setShowlogoutButton(true);
    };

    const onLoginFailure = (res) => {
        console.log('Login Failed:', res);
    };

    const onSignoutSuccess = () => {
        alert("You have been logged out successfully");
        console.clear();
        setShowloginButton(true);
        setShowlogoutButton(false);
        setUnauthorized(false)
    };

    return (
        <div className = "g-signin">
            { showloginButton ?
            <h3>Sign in with Google</h3>
             : null}

            { showloginButton ?
                <GoogleLogin
                    clientId={clientId}
                    buttonText="Sign In"
                    onSuccess={onLoginSuccess}
                    onFailure={onLoginFailure}
                    cookiePolicy={'single_host_origin'}
                    isSignedIn={true}
                /> : null}

            { unauthorized ?
                <span>Logged in as {useremail}<br></br> <h5>You are Unauthorized to view this page</h5></span>:null
            }

            { showlogoutButton ?
                <GoogleLogout
                    clientId={clientId}
                    buttonText="Sign Out"
                    onLogoutSuccess={onSignoutSuccess}
                >
                </GoogleLogout> : null
            }
        </div>
    );
}
