import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

import App from "./App";
import Home from "./pages/Home";
import Ingredients from "./pages/Ingredients";
import Drinks from "./pages/Drinks";
import AllDrinks from "./pages/AllDrinks";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      {
        path: "/ingredients",
        element: <Ingredients />,
      },
      {
        path: "/drinks",
        element: <Drinks />,
      },
      {
        path: "/alldrinks",
        element: <AllDrinks />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);