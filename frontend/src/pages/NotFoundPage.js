import React from 'react';

const NotFoundPage = () => {
  return (
    <div
      style={{
        backgroundColor: "white",
        position: "absolute",
        top: 0,
        bottom: 0,
        left: 0,
        right: 0
      }}
    >
      <div
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          height: "150px",
          width: "500px",
          margin: "-75px 0 0 -250px",
          padding: "20px",
          fontFamily: "Arial",
          fontSize: "75px",
          textAlign: "center",
          textTransform: "uppercase",
          textShadow: "0 0 80px red, 0 0 30px FireBrick, 0 0 6px DarkRed",
          color: "red"
        }}
      >
        <p
          style={{
            color: "#fff",
            textShadow: "0 0 80px #ffffff, 0 0 30px #008000, 0 0 6px #0000ff"
          }}
        >
          error
        </p>
        <p id="code">404</p>
      </div>
    </div>
  );
};


export default NotFoundPage;