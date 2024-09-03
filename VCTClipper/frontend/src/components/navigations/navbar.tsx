import React, { useState } from 'react';
import { MdArrowForward } from 'react-icons/md';
import { useNavigate } from 'react-router-dom'; 
import '../../../public/css/components/navigations/navbar.scss';
import '../../index.css';

type NavItem = {
  label: string;
  icon: React.ReactElement; 
  path: string;
};

interface NavbarProps {
  navs: NavItem[];
}

const Navbar: React.FC<NavbarProps> = ({ navs }) => {
  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate();

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };




  return (
    <div className={`sidebar ${isOpen ? 'open' : ''}`}>
      {isOpen && (
        <div className="sidebar-content">
          <div className="sidebar-header">
            <img src="../../../public/images/vct.png" alt="VCT-Clipper" />
            VCT-Clipper
          </div>

          {navs.map(nav => (
            <div
              key={nav.label}
              className='sidebar-nav-button'
              onClick={()=>{navigate(nav.path)}} // Handle click
            >
              {nav.icon}
              {/* <div className="nav-icon"></div> */}
              <p>{nav.label}</p>
            </div>
          ))}
        </div>
      )}
      <div
        className={`arrow ${isOpen ? 'rotated' : ''}`}
        onClick={toggleSidebar}
      >
        <MdArrowForward />
      </div>
    </div>
  );
};

export default Navbar;
