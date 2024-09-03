import { useState, useRef, useEffect } from "react";
import "../../../public/css/components/button/modal_button.scss";

const ModalButton = ({ button_content, content }: any) => {
  const [isOpen, setIsOpen] = useState(false);
  const modalRef = useRef<HTMLDivElement>(null);

  const toggleModal = () => {
    setIsOpen(!isOpen);
  };

  const handleClickOutside = (event: MouseEvent) => {
    if (modalRef.current && !modalRef.current.contains(event.target as Node)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    if (isOpen) {
      document.addEventListener("mousedown", handleClickOutside);
    } else {
      document.removeEventListener("mousedown", handleClickOutside);
    }

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isOpen]);

  return (
    <>
      <button onClick={toggleModal}>{button_content}</button>

      {isOpen && (
        <div className="modal">
          <div className="modal-content" ref={modalRef}>{content}</div>
        </div>
      )}
    </>
  );
};

export default ModalButton;
