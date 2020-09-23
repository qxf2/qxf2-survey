import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => (
    <nav>
        <ul>
            <li>
                <Link to="/">Survey</Link>
            </li>
            <li>
                <Link to="/dashboard">Dashboard</Link>
            </li>
            <li>
                <Link to="/admin">Admin</Link>
            </li>
        </ul>
    </nav>
);

export default NavBar;