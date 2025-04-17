# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from quantum_simulation import simulate_circuit

app = Flask(__name__)
CORS(app)  # Enable CORS to allow the frontend to call the API

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    # Get options from the request
    apply_error = data.get('apply_error', False)
    use_noise_model = data.get('use_noise_model', False)
    
    # Run simulation
    counts = simulate_circuit(apply_error=apply_error, use_noise_model=use_noise_model)
    return jsonify({'counts': counts})

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
