# 🚗 Clean Alternative Fuel Vehicle (CAFV) Eligibility Predictor

This project is a **Machine Learning-powered web app** that predicts whether an electric vehicle is **eligible for Clean Alternative Fuel Vehicle (CAFV) incentives** based on its specifications.

Built using:
- `scikit-learn` (modeling + pipeline)
- `Streamlit` (frontend app)
- Real-world data from the [U.S. Government Open Data Catalog](https://catalog.data.gov/dataset/electric-vehicle-population-data)

---

## 📊 Demo

👉 **Live App:** [Link](https://cafv-eligibility-predictor-2025.streamlit.app/)

![app-screenshot](demo.png)

---

## 🔍 Features

- Predicts **CAFV eligibility** based on:
  - Vehicle age
  - Electric range
  - MSRP
  - Make, model, price category
  - Electric vehicle type (BEV or PHEV)
- Real-time predictions with Streamlit UI
- Preprocessing + model pipeline with scikit-learn
- Interactive form-based input
- Easy to deploy and scale

---

## 🧠 Machine Learning Pipeline

- **Target Variable:**  
  `Clean Alternative Fuel Vehicle (CAFV) Eligibility`  
  Encoded as 1 (Eligible) or 0 (Not Eligible)

- **Features Used:**  
  - Vehicle Age  
  - Electric Range  
  - Base MSRP  
  - Make (Top 10 + "Other")  
  - Model  
  - Price Category (Low/Mid/High/Luxury)  
  - EV Type (BEV / PHEV)

- **Model:**  
  `RandomForestClassifier` with a preprocessing pipeline

---

## 🛠 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ev-cafv-streamlit.git
cd ev-cafv-streamlit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Launch the App

```bash
streamlit run app.py
```
---

## 📁 File Structure

```
├── app.py                     ← Streamlit frontend
├── model/
│   └── cafv_eligibility_model.pkl  ← Trained ML pipeline
├── requirements.txt           ← Dependencies
└── README.md
```
---

## 📚 Data Source

- Washington State Electric Vehicle Population
[Data Catalog Link](https://catalog.data.gov/dataset/electric-vehicle-population-data)

---

## 🙌 Acknowledgements

- Data from WA State Department of Licensing
- Streamlit for quick deployment
- scikit-learn for powerful pipelines

---

## 👩‍💻 Author

**Jahnavi P**  
📍 Bangalore, India  
🔗 [LinkedIn](https://www.linkedin.com/in/jahnavi-p-a68788233) 

---



