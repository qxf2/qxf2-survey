import React, { useState, useEffect } from 'react';
import axios from "axios";
import url_conf from "./data/urlConf";
import LoginForm from "./login"
import { GoogleLogout } from 'react-google-login';

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY
const clientId = process.env.REACT_APP_CLIENT_ID

const EmployeeTable = () => {

    const URL = `${url_conf}/survey/admin/employees`
    const [employees, setEmployees] = useState([])

    const getData = async () => {
        const response = await axios.get(URL)
        setEmployees(response.data)
    }

    useEffect(() => {
        getData()
    }, [])// eslint-disable-line react-hooks/exhaustive-deps


    const renderHeader = () => {
        let headerElement = ['ID', 'first_name', 'last_name', 'active_flag', 'email']
        return headerElement.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    const renderBody = () => {
        return employees && employees.map(({ID, firstName, lastName, status, email}) => {
            return (
                <tr key={email}>
                    <td>{ID}</td>
                    <td>{firstName}</td>
                    <td>{lastName}</td>
                    <td>{status}</td>
                    <td>{email}</td>
                </tr>
            )
        })
    }

    return (
        <div>
            <h1 id='title'>Employee Table</h1>
            <table id='employees'>
                <tbody>
                    <tr>{renderHeader()}</tr>
                    {renderBody()}
                </tbody>
            </table>
            <br></br>
        </div>
    )
}

const ToRespond = () => {

    const URL = `${url_conf}/survey/admin/not_responded_users`
    const [employees, setEmployees] = useState([])
    const getData = async () => {
        const response = await axios.get(URL)
        setEmployees(response.data)
    }

    useEffect(() => {
        getData()
    }, [])// eslint-disable-line react-hooks/exhaustive-deps

    const renderHeader = () => {
        let headerElement = ['Name','email']
        return headerElement.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    const renderBody = () => {
        return employees && employees.map(({firstName, lastName, email}) => {
            return (
                <tr key={email}>
                    <td>{firstName} {lastName}</td>
                    <td>{email}</td>
                </tr>
            )
        })
    }

    return (
        <div>
            <h1 id='title'>Employees yet to Respond</h1>
            <table id='employees'>
                <tbody>
                    <tr>{renderHeader()}</tr>
                    {renderBody()}
                </tbody>
            </table>
            <br></br>
        </div>
    )
}

const AdminPage = () => {
    const [LoginStatus, updateLoginStatus] = React.useState(false);
    const [useremail, setUseremail] = React.useState(null)
    const Login = (login_status,email) => {
        if(login_status === true){
            updateLoginStatus(true)
            setUseremail(email)
        }
    }

    const onSignoutSuccess = () => {
        alert("You have been logged out successfully");
        console.clear();
        updateLoginStatus(false)
    };
    return (
        <div className="App">
        {
        (LoginStatus === true)?
        (
        <>
            <br></br>
            <span style={{float:"right",marginRight:"-350px"}}>
            <p style={{float:'center'}}>Logged in as {useremail}</p>
            <GoogleLogout
                clientId={clientId}
                buttonText="Sign Out"
                onLogoutSuccess={onSignoutSuccess}
            >
            </GoogleLogout>
            </span>
            <br></br>
            <br></br>
            <br></br>
            <EmployeeTable />
            <br></br>
            <br></br>
            <ToRespond />
        </>
        ): (<LoginForm Login={Login}/>)
        }
        </div>
    );
};

export default AdminPage;