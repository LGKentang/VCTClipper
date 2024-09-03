import React, { useState, useRef, useEffect } from "react";
import Paper from "../root/paper";
import { FaCircle } from "react-icons/fa6";
import ToggleButton from "../button/toggle_button";
import "../../../public/css/components/data/node_details.scss";
import NodeTooltip from "../menu/node_tooltip";
import { useNavigate } from "react-router-dom";

interface NodeDetailsProps {
  worker: Worker;
}

const NodeDetails: React.FC<NodeDetailsProps> = ({ worker }) => {
  const [menuVisible, setMenuVisible] = useState(false);
  const [menuPosition, setMenuPosition] = useState({ x: 100, y: 100 });
  const tooltipRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();

  const handleContextMenu = (e: React.MouseEvent) => {
    e.preventDefault(); 
    setMenuPosition({ x: e.clientX -6, y: e.clientY -6 });
    setMenuVisible(true);
  };

  const handleClick = (e: MouseEvent) => {
    if (tooltipRef.current && !tooltipRef.current.contains(e.target as Node)) {
      setMenuVisible(false); 
    }
  };

  const handleMouseOver = (e: MouseEvent) => {
    if (tooltipRef.current && !tooltipRef.current.contains(e.target as Node)) {
      setMenuVisible(false); 
    }
  };

  useEffect(() => {
    document.addEventListener('mousedown', handleClick);
    document.addEventListener('mouseover', handleMouseOver);

    return () => {
      document.removeEventListener('mousedown', handleClick);
      document.removeEventListener('mouseover', handleMouseOver);
    };
  }, []);

  const handleDelete = () => {
    console.log("Delete action");
    setMenuVisible(false);
  };

  const handleEdit = () => {
    setMenuVisible(false);
    navigate(`/workers/${worker.uuid}`);
  }


  return (
    <div onContextMenu={handleContextMenu} className="worker-ongoing-data">
      <Paper margin={"0"} padding={"0"}>
        <div className="worker-data-card">
          
          <FaCircle
            size={10}
            color={worker.status === "active" ? "green" : "red"}
          />
          <div>
            <h3>{worker.name}</h3>
          </div>
          <div className="worker-data-middle-card">
            <img
              className="worker-data-img"
              src={`./images/${
                worker.mediaType === "Youtube" ? "youtube" : "twitch"
              }.png`}
              alt=""
            />
            <p>{worker.channelHandle}</p>
          </div>
          <ToggleButton onTurnedOn={function (): void {
            throw new Error("Function not implemented.");
          } } onTurnedOff={function (): void {
            throw new Error("Function not implemented.");
          } } />
        </div>
      </Paper>
      <NodeTooltip
        ref={tooltipRef}
        visible={menuVisible}
        position={menuPosition}
        onDelete={handleDelete}
        onEdit={handleEdit}
      />
    </div>
  );
};

export default NodeDetails;
