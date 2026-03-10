import { createBrowserRouter, Navigate } from "react-router-dom";
import App from "../App";
import TestPage from "../pages/TestPage";
import NotFoundPage from "../pages/NotFoundPage";
import MainLayout from "../components/layout/MainLayout";
import HomePage from "../pages/HomePage";
import SearchPage from "../pages/SearchPage";
import ProfilePage from "../pages/ProfilePage";
import SettingsPage from "../pages/SettingsPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/test",
    element: <TestPage />,
  },
  {
    element: <MainLayout />,
    children: [
      {
        path: "/home",
        element: <HomePage />,
      },
      {
        path: "/search",
        element: <SearchPage />,
      },
      {
        path: "/profile",
        element: <ProfilePage />,
      },
      {
        path: "/settings",
        element: <SettingsPage />,
      },
    ],
  },
  {
    path: "/mobile",
    element: <Navigate to="/home" replace />,
  },
  {
    path: "*",
    element: <NotFoundPage />,
  },
]);

export default router;
