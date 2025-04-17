// frontend/src/CircuitDesigner.js
import React, { useState } from 'react';

const CircuitDesigner = ({ onSimulate }) => {
  const [applyError, setApplyError] = useState(false);
  const [useNoise, setUseNoise] = useState(false);

  const handleSimulate = () => {
    onSimulate({ apply_error: applyError, use_noise_model: useNoise });
  };

  return (
    <div>
      <h2>Design Your Quantum Circuit</h2>
      <div>
        <label>
          <input
            type="checkbox"
            checked={applyError}
            onChange={(e) => setApplyError(e.target.checked)}
          />
          Apply Bit-flip Error on Qubit 0
        </label>
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            checked={useNoise}
            onChange={(e) => setUseNoise(e.target.checked)}
          />
          Simulate with Noise Model (Depolarizing)
        </label>
      </div>
      <button onClick={handleSimulate}>Simulate Circuit</button>
    </div>
  );
};

export default CircuitDesigner;
