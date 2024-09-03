import React, { CSSProperties, ReactNode } from 'react';

interface PaperProps {
  children: ReactNode;
  className?: string;
  style? : CSSProperties
  isCenter?: boolean;
  margin?: string;
  padding?: string | number;
  backgroundColor?: string;
}

const Paper: React.FC<PaperProps> = ({
  children,
  className,
  isCenter = false,
  style,
  margin,
  padding = 10,
  backgroundColor = '#b8c3ce4b',
}) => {
  return (
    <div
      className={className}
      style={{
        padding,
        borderRadius: 5,
        backgroundColor,
        marginBottom: 20,
        width: '100%',
        maxWidth: 800,
        margin: margin ? margin : 'auto',
        display: 'flex',
        justifyContent: isCenter ? 'center' : 'flex-start',
        alignItems: isCenter ? 'center' : 'flex-start',
        flexDirection: isCenter ? 'column' : 'row',
        ...style
      }}
    >
      {children}
    </div>
  );
};

export default Paper;
