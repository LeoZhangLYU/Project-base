import logo from "./assets/images/logo.svg";
import "./assets/css/App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Home from "./components/Home";
import Pcontent from "./components/Pcontent";

function App() {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Home></Home>}></Route>
        <Route path="/pcontent/:id" element={<Pcontent></Pcontent>}></Route>
      </Routes>
    </div>
  );
}

export default App;
