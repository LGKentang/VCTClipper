import React, { forwardRef } from "react";
import "../../../public/css/components/menu/node_tooltip.scss";
import { RiDeleteBin5Fill } from "react-icons/ri";
import { FaGear } from "react-icons/fa6";

const NodeTooltip = forwardRef<
  HTMLDivElement,
  {
    visible: boolean;
    position: { x: number; y: number };
    onDelete: () => void;
    onEdit: () => void;
  }
>(({ visible, position, onDelete, onEdit}, ref) => {
  if (!visible) return null;

  return (
    <div
      className="custom-context-menu visible"
      style={{ top: position.y, left: position.x }}
      ref={ref}
    >
      <button
        className="edit-button"
        onClick={(e) => {
          e.stopPropagation();
          onEdit();
        }}
      >
        <FaGear size={24} />
      </button>
      <button
        className="delete-button"
        onClick={(e) => {
          e.stopPropagation();
          onDelete();
        }}
      >
        <RiDeleteBin5Fill size={24} />
      </button>
    </div>
  );
});

export default NodeTooltip;
