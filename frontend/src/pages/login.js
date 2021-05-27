import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "../Login.css";

const {REACT_APP_ADMIN_EMAIL, REACT_APP_ADMIN_PASS} = process.env;
export default function Login({Login}) {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  //const[details, setDetails] = useState("");

  function validateForm() {
    return email.length > 0 && password.length > 0;
  }

  function handleSubmit(event) {
    event.preventDefault();
    if(event.target['email'].value===REACT_APP_ADMIN_EMAIL){
      if(event.target['password'].value===REACT_APP_ADMIN_PASS){
        //console.log("Successfull")
        const login_status = true
        alert("Login Success")
        Login(login_status);
      }
      else{
        console.log("Incorrect password")
      }
    }
    else{
      console.log("Unauthorized")
    }

    //console.log(REACT_APP_ADMIN_EMAIL)
    //console.log(REACT_APP_ADMIN_PASS)
    //console.log(event.target['email'].value)
    //console.log(event.target['password'].value)
  }

  return (
    <div className="Login">
      <Form onSubmit={handleSubmit}>
        <Form.Group size="lg" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>
        <Form.Group size="lg" controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>
        <Button block size="lg" type="submit" disabled={!validateForm()}>
          Login
        </Button>
      </Form>
    </div>
  );
}