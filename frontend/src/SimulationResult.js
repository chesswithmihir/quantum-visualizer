// frontend/src/SimulationResult.js
import React from 'react';

const SimulationResult = ({ counts }) => {
  if (!counts) {
    return null;
  }

  return (
    <div>
      <h2>Simulation Result</h2>
      <pre>{JSON.stringify(counts, null, 2)}</pre>
    </div>
  );
};

export default SimulationResult;
