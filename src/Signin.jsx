import React, { useState } from "react";

import "./Signin.css";

function Signin() {
  let [email, setemail] = useState();
  let [password, setpassword] = useState();
  return (
    <div class="signin">
      <div class="signin-text">
        <h1>Hello, Friend!</h1>
        <p>Enter your personal details and start journey with us</p>
        <button>SIGN IN</button>
      </div>
      <div class="signin-form">
        <h1>SIGN IN</h1>
        <input
          type="text"
          value={email}
          onChange={(e) => {
            setemail(e.target.value);
          }}
          placeholder="Email"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => {
            setpassword(e.target.value);
          }}
          placeholder="Password"
        />
        <a href="/">Forgot your password?</a>
        <input type="button" value="SIGN UP" />
      </div>
    </div>
  );
}

export default Signin;
