import { useState } from "react";

interface ToggleButtonProps{
  onTurnedOn : () => void,
  onTurnedOff : () => void,
}

const ToggleButton : React.FC<ToggleButtonProps> = ({}) => {
  const [isOn, setIsOn] = useState(false);

  const handleToggle = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation(); 
    setIsOn(prevState => !prevState);
  };

  return (
    <button
      onClick={handleToggle}
      style={{
        padding: "10px 20px",
        backgroundColor: isOn ? "green" : "red",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
        outline: "none"
      }}
    >
      {isOn ? "On" : "Off"}
    </button>
  );
};

export default ToggleButton;
