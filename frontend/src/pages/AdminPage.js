import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import axios from "axios";

axios.defaults.headers.common['User'] = process.env.REACT_APP_API_KEY

const AddEmployee = () => {

    const [formData, updateFormData] = React.useState([]);

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
        'fullName': formData["employee-first-name-input"] + formData["employee-last-name-input"],
        'status': formData["status-input"]
      }
    
    const handleSubmit = (e) => {
      e.preventDefault()
      if (formData !== "") {
        axios.post('http://3.239.35.79:8000/survey/admin/new_employee' , {data: newEmployeeData})
          .then(function (response) {
            console.log("Post request: Success")
          })
          .catch(function (error) {
            console.log("Post request: Failed")
            console.log(error.response);     
          });
    };}

    return (
        <div class="panel panel-primary">
        <div class="panel-heading">
            <h3 class="panel-title"><strong>Add Employee</strong></h3>
        </div>
        <div class="panel-body">
            <form>
            <div class="form-group">
                <label for="employee-first-name-input">First Name</label>
                <input class="form-control" name="employee-first-name-input" type="text" onChange={handleChange}></input>
            </div>
            <div class="form-group">
                <label for="employee-last-name-input">Last Name</label>
                <input class="form-control" name="employee-last-name-input" type="text" onChange={handleChange}></input>
            </div>
            <div class="form-group">
                <label for="email-input">E-Mail</label>
                <input class="form-control" name="email-input" type="text" onChange={handleChange}></input>
            </div>
            <div class="form-group">
                <label for="status-input">Employee Status (Y/N)</label>
                <input class="form-control" name="status-input" type="text" onChange={handleChange}></input>
            </div>
            <div className="col-md-4 offset-md-4">
                <Button variant="primary" size="lg" block onClick={handleSubmit}>
                    Submit
            </Button>
            </div>
            </form>
        </div>
        </div>
    );
    };

const EmployeeTable = () => {

    const URL = 'http://3.239.35.79:8000/survey/admin/employees'
    const [employees, setEmployees] = useState([])

    useEffect(() => {
        getData()
    }, [])

    const getData = async () => {
        const response = await axios.get(URL)
        setEmployees(response.data)
    }

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
        return employees && employees.map(({ ID, firstName, lastName, status, email }) => {
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

    const URL = 'http://3.239.35.79:8000/survey/admin/not_responded_users'
    const [employees, setEmployees] = useState([])
    useEffect(() => {
        getData()
    }, [])

    const getData = async () => {
        const response = await axios.get(URL)
        setEmployees(response.data)
    }

    const renderHeader = () => {
        let headerElement = ['ID', 'Name']
        return headerElement.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    const renderBody = () => {
        return employees && employees.map(({ ID, firstName, lastName }) => {
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