// frontend/src/App.js
import React, { useState } from 'react';
import CircuitDesigner from './CircuitDesigner';
import SimulationResult from './SimulationResult';
import { simulateCircuit } from './api';

const App = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSimulate = async (options) => {
    setLoading(true);
    try {
      const data = await simulateCircuit(options);
      setResult(data.counts);
    } catch (error) {
      alert('Simulation failed. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Interactive Quantum Circuit Visualizer</h1>
      <CircuitDesigner onSimulate={handleSimulate} />
      {loading && <p>Simulating...</p>}
      <SimulationResult counts={result} />
    </div>
  );
};

export default App;
