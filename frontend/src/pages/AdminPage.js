import React from 'react';
import Button from 'react-bootstrap/Button';

const AddEmployee = () => {
  return (
    <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title"><strong>Add Employee</strong></h3>
      </div>
      <div class="panel-body">
        <form>
          <div class="form-group">
            <label for="employee-first-name-input">First Name</label>
            <input class="form-control" id="employee-first-name-input" type="text"></input>
          </div>
          <div class="form-group">
            <label for="employee-last-name-input">Last Name</label>
            <input class="form-control" id="employee-last-name-input" type="text"></input>
          </div>
          <div class="form-group">
            <label for="email-input">E-Mail</label>
            <input class="form-control" id="email-input" type="text"></input>
          </div>
          <div class="form-group">
            <label for="status-input">Employee Status (Y/N)</label>
            <input class="form-control" id="status-input" type="text"></input>
          </div>
          <div className="col-md-4 offset-md-4">
            <Button variant="primary" size="lg" block>
                Submit
           </Button>
        </div>
        </form>
      </div>
    </div>
  );
};

class AdminPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            employees: [
                { id: 1, firstName: "Arunkumar", lastName: 'Muralidharan', Status: 'Y', email: 'mak@qxf2.com' },
                { id: 2, firstName: "Raji", lastName: 'Gali', Status: 'Y', email: 'raji@qxf2.com' },
                { id: 3, firstName: "Avinash", lastName: 'Shetty', Status: 'Y', email: 'avinash@qxf2.com' },
                { id: 4, firstName: "Shivahari", lastName: 'Pitchaikkannu', Status: 'Y', email: 'shivahari@qxf2.com	' },
                { id: 5, firstName: "Annapoorani", lastName: 'Gurusamy', Status: 'Y', email: 'annapoorani@qxf2.com' },
                { id: 6, firstName: "Rohan", lastName: 'Dudam', Status: 'Y', email: 'rohan@qxf2.com' },
                { id: 7, firstName: "Smitha", lastName: 'Rajesh', Status: 'Y', email: 'smitha@qxf2.com' },
                { id: 8, firstName: "Indira", lastName: 'Nellutla', Status: 'Y', email: 'indira@qxf2.com' },
                { id: 9, firstName: "Arunkumar", lastName: 'Muralidharan', Status: 'Y', email: 'mak@qxf2.com' },
                { id: 10, firstName: "Rohan", lastName: 'Joshi', Status: 'Y', email: 'rohan.j@qxf2.com' },
                { id: 11, firstName: "Nilaya", lastName: 'Indurkar', Status: 'Y', email: 'nilaya@qxf2.com' },
                { id: 12, firstName: "Sumeet", lastName: 'Dhawale', Status: 'N', email: 'sumeet@qxf2.com' },
                { id: 13, firstName: "Edward", lastName: 'Alan', Status: 'Y', email: 'edward@qxf2.com' },
                { id: 14, firstName: "Mohan", lastName: 'Kumar', Status: 'Y', email: 'mohan@qxf2.com' },
                { id: 15, firstName: "Kavitha", lastName: 'Duraiswamy', Status: 'Y', email: 'kavitha.d@qxf2.com' },
                { id: 16, firstName: "Rohini", lastName: 'Gopal', Status: 'Y', email: 'rohini.gopal@qxf2.com' },
                { id: 17, firstName: "Akkul", lastName: 'DN', Status: 'Y', email: 'akkul.dn@qxf2.com' },
                { id: 18, firstName: "Kiran", lastName: 'CV', Status: 'Y', email: 'kiran.cv@qxf2.com' },
                { id: 19, firstName: "Sravanti", lastName: 'Tatiraju', Status: 'Y', email: 'sravanti.tatiraju@qxf2.com' },
                { id: 21, firstName: "Rahul", lastName: 'Bhave', Status: 'Y', email: 'rahul.bhave@qxf2.com' },
                { id: 22, firstName: "Preedhi", lastName: 'Vivek', Status: 'Y', email: 'preedhi.vivek@qxf2.com' },
                { id: 23, firstName: "Rajkumar", lastName: 'M', Status: 'N', email: 'rajkumar.m@qxf2.com' },
                { id: 24, firstName: "Drishya", lastName: 'TM', Status: 'Y', email: 'drishya.tm@qxf2.com' },
                { id: 25, firstName: "Harsh", lastName: 'Bardhan', Status: 'Y', email: 'harsh.bardhan@qxf2.com' },
                { id: 26, firstName: "Rohit", lastName: 'Prasad', Status: 'Y', email: 'rohit.prasad@qxf2.com' },
                { id: 27, firstName: "Basavaraj", lastName: 'Hiremath', Status: 'Y', email: 'basavaraj.hiremath@qxf2.com' },
                { id: 28, firstName: "Namitha", lastName: 'Sathyananda', Status: 'Y', email: 'namitha.sathyananda@qxf2.com' },
                { id: 29, firstName: "Vidhya", lastName: 'Zierlein', Status: 'Y', email: 'vidhya.zierlein@qxf2.com' },
                { id: 30, firstName: "Rakhi", lastName: 'Chaudhuri', Status: 'Y', email: 'rakhi.chaudhuri@qxf2.com' }
            ]
        }
    }

    renderTableHeader() {
        let header = Object.keys(this.state.employees[0])
        return header.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    renderTableData() {
        return this.state.employees.map((employee, index) => {
            const { id, firstName, lastName, Status, email } = employee //destructuring
            return (
                <tr key={id}>
                    <td>{id}</td>
                    <td>{firstName}</td>
                    <td>{lastName}</td>
                    <td>{Status}</td>
                    <td>{email}</td>
                </tr>
            )
        })
    }

    render() {
        return (
            <>
            <div>
                <h1 id='title'>Employee Table</h1>
                <table id='employees'>
                    <tbody>
                        <tr>{this.renderTableHeader()}</tr>
                        {this.renderTableData()}
                    </tbody>
                </table>
                <br></br>
            </div>
            <AddEmployee />
            </>
        )
    }
};

export default AdminPage;