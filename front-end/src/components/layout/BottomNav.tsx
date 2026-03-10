import React from "react";
import { NavLink } from "react-router-dom";
import { Home, Search, User, Settings } from "lucide-react";
import "./BottomNav.css";

const BottomNav: React.FC = () => {
  return (
    <nav className="bottom-nav">
      <NavLink
        to="/home"
        className={({ isActive }) => (isActive ? "nav-item active" : "nav-item")}
      >
        <Home size={24} />
        <span>Home</span>
      </NavLink>
      <NavLink
        to="/search"
        className={({ isActive }) => (isActive ? "nav-item active" : "nav-item")}
      >
        <Search size={24} />
        <span>Search</span>
      </NavLink>
      <NavLink
        to="/profile"
        className={({ isActive }) => (isActive ? "nav-item active" : "nav-item")}
      >
        <User size={24} />
        <span>Profile</span>
      </NavLink>
      <NavLink
        to="/settings"
        className={({ isActive }) => (isActive ? "nav-item active" : "nav-item")}
      >
        <Settings size={24} />
        <span>Settings</span>
      </NavLink>
    </nav>
  );
};

export default BottomNav;
