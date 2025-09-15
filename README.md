# 🌱 AI-Powered Crop Recommendation System

This project is an **AI-based Crop Recommendation System** built with **Python** and **Streamlit**.  
It suggests the most suitable crop to grow based on soil nutrients and climate conditions.  

---

## 🚀 Features
- User-friendly **Streamlit web interface**  
- Input parameters:  
  - Nitrogen (N), Phosphorus (P), Potassium (K)  
  - Temperature (°C), Humidity (%), pH, Rainfall (mm)  
- Predicts the **best crop to cultivate** using a Machine Learning model  
- Self-contained single-file application (no external `.pkl` files needed)  

---

## ⚙️ Tech Stack
- **Python 3.11+**  
- **Streamlit** (frontend)  
- **Scikit-learn** (ML model)  
- **NumPy, Pandas** (data handling)  

---

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install streamlit scikit-learn numpy pandas
2. Run the streamlit app:
   ```bash
   streamlit run app.py
  ## 📊 Workflow
1. Collect soil and climate data (Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall).  
2. Preprocess the dataset using **StandardScaler** for feature scaling.  
3. Train a **Random Forest Classifier** on the dataset.  
4. Save the trained model and scaler (or embed them in the app for single-file submission).  
5. Build a **Streamlit web app** to take user inputs.  
6. Scale the input values and pass them to the trained model.  
7. Display the **recommended crop** as output to the user.  

