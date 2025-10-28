# ⚛️ QNN-Lite: A Hybrid Quantum-Classical Neural Network

This project is a deep-dive into Quantum AI, building a hybrid neural network from scratch using Python (PyTorch, Qiskit) and a React.js dashboard.

The goal is to replace a layer of a classical AI model with a Variational Quantum Circuit (VQC) and compare its performance on the MNIST dataset.

## Tech Stack
* **AI (Classical):** Python, PyTorch
* **AI (Quantum):** Qiskit, Qiskit Machine Learning
* **Backend API:** Python, Flask
* **Frontend:** React.js, Matplotlib (for saving charts)
* **Database:** MongoDB
* **Automation:** Bash Scripting

## Project Architecture
This is a full-stack, hybrid computation project.

1.  **`client-react`:** A web dashboard to start training runs and visualize results.
2.  **`backend-python`:** A Flask API that serves the React app and runs the AI models.
3.  **`QNN_Model`:** The core AI, a hybrid PyTorch/Qiskit model.

## Project Status (MVP Goals)
- [ ] **Phase 1:** Build and train the baseline classical model (PyTorch).
- [ ] **Phase 2:** Implement the hybrid QNN model (PyTorch + Qiskit).
- [ ] **Phase 3:** Build the Flask API and React client to run training from a webpage.
- [ ] **Phase 4:** Integrate MongoDB to store results and a Bash script to automate the dev server.
