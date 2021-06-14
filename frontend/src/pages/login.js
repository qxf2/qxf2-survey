import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "../Login.css";
import admin_password from "../AdminCredentials"

const bcrypt=require("bcryptjs")

export default function Login({Login}) {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function compareCredentials({entered_password},{entered_email}){
    const isemailMatch = await bcrypt.compare(entered_email, admin_password.REACT_APP_ADMIN_EMAIL);
    const isPasswordMatch = await bcrypt.compare(entered_password, admin_password.REACT_APP_ADMIN_PASS);
    if(isemailMatch){
      if(isPasswordMatch){
        const login_status = true
        alert("Login Success")
        Login(login_status);
      }
      else{
        alert("Incorrect password")
      }
    }
    else{
      alert("Unauthorized")
    }

  }

  function validateForm() {
    return email.length > 0 && password.length > 0;
  }

  function handleSubmit(event) {
    event.preventDefault();
    const entered_password=event.target['password'].value
    const entered_email=event.target['email'].value
    compareCredentials({entered_password}, {entered_email})
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