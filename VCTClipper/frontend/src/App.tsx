import Navbar from './components/navigations/navbar';
import { LuLayoutDashboard } from "react-icons/lu";
import { HiWrenchScrewdriver } from "react-icons/hi2";
import { BiMoviePlay } from "react-icons/bi";
import './App.css';
import RouteLayer from './routes/RouteLayer';
import { useState } from 'react';

function App() {


  const navs = [
    { label: 'Dashboard', icon: < LuLayoutDashboard  />, path: '/dashboard' },
    { label: 'Workers', icon: <HiWrenchScrewdriver />, path: '/workers' },
    { label: 'Clips', icon: <BiMoviePlay />, path: '/clips' },
  ];

  

  return (
    <>
      <RouteLayer>
        <Navbar navs={navs} />
      </RouteLayer>
    </>
  );
}

export default App;
