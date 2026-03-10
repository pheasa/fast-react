import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import TestPage from "../pages/TestPage";
import NotFoundPage from "../pages/NotFoundPage";

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
    path: "*",
    element: <NotFoundPage />,
  },
]);

export default router;
