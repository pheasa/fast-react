import React from "react";
import { Outlet } from "react-router-dom";
import BottomNav from "./BottomNav";
import "./MainLayout.css";

const MainLayout: React.FC = () => {
  return (
    <div className="main-layout">
      <main className="layout-content">
        <Outlet />
      </main>
      <BottomNav />
    </div>
  );
};

export default MainLayout;
