// frontend/src/api.js
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const simulateCircuit = async (options) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/simulate`, options);
    return response.data;
  } catch (error) {
    console.error("API error:", error);
    throw error;
  }
};
