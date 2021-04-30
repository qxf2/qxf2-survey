import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import axios from "axios";
import url_conf from "./data/urlConf";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

const AddEmployee = () => {

    const [formData, updateFormData] = React.useState([]);
    const [employees_data, setemployees_data]=React.useState([])

    useEffect(() =>{
        axios.get(`${url_conf}/survey/admin/employees`)
        .then(response=>{
          setemployees_data(response.data)
        })
      },[])

    const handleChange = (e) => {
      updateFormData({
        ...formData,
        // Trimming any whitespace
        [e.target.name]: e.target.value.trim()
      });
    };

    var newEmployeeData = {
        'firstName': formData["employee-first-name-input"],
        'lastName': formData["employee-last-name-input"],
        'email': formData["email-input"],
        'fullName': formData["employee-first-name-input"] + " " + formData["employee-last-name-input"],
        'status': formData["status-input"]
      }

    const HandleSubmit = (e) => {
      e.preventDefault()
      if (formData !== "") {
        console.log(newEmployeeData.email)

        var valid_email_flag=false
        var i=0
        for(i=0;i<=employees_data.length-1;i++)
        {
        if(employees_data[i]['email']===newEmployeeData.email)
        {
            valid_email_flag=true
            break;
        }
        }

        console.log(valid_email_flag)

        if(valid_email_flag===false){

            axios.post(`${url_conf}/survey/admin/new_employee` , {data: newEmployeeData})
            .then(function (response) {
                console.log("Post request: Success")
            })
            .catch(function (error) {
                console.log("Post request: Failed")
                console.log(error.response);

            });
        }
        else{
            alert("Email already exists")
        }

    };}

    return (
        <div className="panel panel-primary">
        <div className="panel-heading">
            <h3 className="panel-title"><strong>Add Employee</strong></h3>
        </div>
        <div className="panel-body">
            <form>
            <div className="form-group">
                <label htmlFor="employee-first-name-input">First Name</label>
                <input className="form-control" name="employee-first-name-input" type="text" onChange={handleChange}></input>
            </div>
            <div className="form-group">
                <label htmlFor="employee-last-name-input">Last Name</label>
                <input className="form-control" name="employee-last-name-input" type="text" onChange={handleChange}></input>
            </div>
            <div className="form-group">
                <label htmlFor="email-input">E-Mail</label>
                <input className="form-control" name="email-input" type="text" onChange={handleChange}></input>
            </div>
            <div className="form-group">
                <label htmlFor="status-input">Employee Status (Y/N)</label>
                <input className="form-control" name="status-input" type="text" onChange={handleChange}></input>
            </div>
            <div className="col-md-4 offset-md-4">
                <Button variant="primary" size="lg" block onClick={HandleSubmit}>
                    Submit
            </Button>
            </div>
            </form>
        </div>
        </div>
    );
    };

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

    const removeData = (id) => {
        axios.delete(`${URL}/${id}`).then(res => {
            const del = employees.filter(employee => id !== employee.ID)
            setEmployees(del)
        })
    }

    const renderHeader = () => {
        let headerElement = ['ID', 'first_name', 'last_name', 'active_flag', 'email','operation']
        return headerElement.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    const renderBody = () => {
        return employees && employees.map(({ ID, firstName, lastName, status, email}) => {
            return (
                <tr key={ID}>
                    <td>{ID}</td>
                    <td>{firstName}</td>
                    <td>{lastName}</td>
                    <td>{status}</td>
                    <td>{email}</td>
                    <td className='operation'>
                        <button className='button' onClick={() => removeData(ID)}>Delete</button>
                    </td>
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
        let headerElement = ['ID', 'Name']
        return headerElement.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    const renderBody = () => {
        return employees && employees.map(({ ID, firstName, lastName}) => {
            return (
                <tr key={ID}>
                    <td>{ID}</td>
                    <td>{firstName} {lastName}</td>
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
    return (
        <>
            <br></br>
            <EmployeeTable />
            <AddEmployee />
            <ToRespond />
        </>
    );
};

export default AdminPage;