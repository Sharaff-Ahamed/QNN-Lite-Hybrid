# ⚛️ QNN-Lite: Hybrid Quantum–Classical Neural Network

A practical exploration into **Quantum Machine Learning (QML)** using real quantum circuits — without requiring quantum hardware.

QNN-Lite combines:
- **Classical Deep Learning (PyTorch)**  
- **Quantum Variational Circuits (Qiskit)**  

The goal is to replace one classical neural network layer with a **Variational Quantum Circuit (VQC)** and compare the performance of:

| Model Type | Technology | Expected Outcome |
|------------|------------|------------------|
| Classical Neural Network | PyTorch | Strong accuracy baseline |
| Hybrid Quantum Neural Network | PyTorch + Qiskit | Lower accuracy, but demonstrates quantum learning capability |

---

## 🏁 Project Progress

### ✅ Phase Overview
Each phase represents a major milestone in the project.

| Phase | Description | Status |
|--------|-------------|--------|
| Phase 0 | Setup Python environment + Project structure | ✅ Completed |
| Phase 1 | Store MNIST dataset in MongoDB (visualize in Compass) | ✅ Completed |
| Phase 2 | Train Classical Neural Network (PyTorch baseline model) | 🔄 In Progress |
| Phase 3 | Build Hybrid QNN Model (PyTorch + Qiskit VQC layer) | ⏳ Next |
| Phase 4 | Compare Classical vs Quantum performance & store logs | ⏳ Pending |
| Phase 5 | Build Flask backend to trigger training from API | ⏳ Pending |
| Phase 6 | Build React.js dashboard for visualization | ⏳ Pending |
| Phase 7 | Bash script automation (run training + logs) | ⏳ Pending |

---

### 📊 Progress Bar

---

## 🧠 Tech Stack

### **AI & Quantum**
- Python
- PyTorch (classical model)
- Qiskit + Qiskit Machine Learning (quantum model)

### **Backend**
- Flask (REST API to trigger training and fetch results)
- MongoDB (stores:
  - training logs
  - accuracy results
  - predicted sample images)

### **Frontend**
- React.js dashboard (visualizing charts and results)

### **Automation**
- Bash scripting to automate:
  - training runs
  - logging
  - environment setup

---

## 🏗️ Project Structure

📦 **QNN-Lite**
