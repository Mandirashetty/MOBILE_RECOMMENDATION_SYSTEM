# 📱 Mobile Recommendation System (Machine Learning)

A smart mobile recommendation system built using **Machine Learning** and **Flask** that suggests similar smartphones using **content-based filtering** and **cosine similarity**.

---

## 🚀 Features

- 🔍 Search for a mobile phone  
- 🤖 Get similar phone recommendations  
- ⚡ Fast and simple ML model  
- 🌐 Web interface using Flask  

---

## 🎯 Problem Statement

Choosing the right smartphone is difficult due to the large number of available options. This project recommends similar phones based on user input.

---

## 🧠 Machine Learning Approach

- **Algorithm:** Content-Based Filtering  
- **Technique:** Cosine Similarity  
- **Vectorization:** CountVectorizer (Scikit-learn)  
- **Features Used:** Mobile phone dataset  

---

## ⚙️ How It Works

1. User enters a phone name  
2. Data is converted into vectors  
3. Cosine similarity is calculated  
4. Similar phones are recommended  

---

## 📂 Project Structure

```
MOBILE_ML_PROJECT/
│── app.py
│── mobile_recommendation_dataset.csv
│── templates/
│     └── index.html
│── README.md
```


---

## ⚙️ Installation

```bash
pip install flask pandas scikit-learn
```

## ▶️ Run the Application

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000/
```

## 📸 Screenshots

### 🔹 Home Page
<img width="1885" height="896" alt="Screenshot 2026-03-29 103154" src="https://github.com/user-attachments/assets/53204776-330a-413c-ad8c-0b1ee495d025" />

### 🔹 Recommendation Result
<img width="1863" height="845" alt="Screenshot 2026-03-29 103216" src="https://github.com/user-attachments/assets/e1a7bc7c-384a-4900-974b-6f048bb64426" />

## 📊 Dataset

The dataset contains mobile phone details used for generating recommendations.

| Phone Name  | Brand   | Features            |
| ----------- | ------- | ------------------- |
| iPhone 13   | Apple   | iOS, 5G, Camera     |
| Samsung S21 | Samsung | Android, 5G, Camera |

## 🛠️ Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- HTML/CSS  
