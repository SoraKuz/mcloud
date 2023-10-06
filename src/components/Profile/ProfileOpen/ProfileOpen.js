import css from "./ProfileOpen.module.css"
import { Link } from "react-router-dom";
import Login from "../../../pages/RegistrationLogin/Login";

import { useState } from "react";

export const ProfileOpen = () => {
  return (
    
      <div className={css.links}>
        <Link className={css.link} to="/SignIn">
            <div className={css.content}>SignIn</div>
        </Link>
        <Link className={css.link} to="/SignUp">
            <div className={css.content}>SignUp</div>
        </Link>
      </div>
  );
};