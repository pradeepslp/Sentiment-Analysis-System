# 💬 Sentiment Analysis System

A clean and lightweight Sentiment Analysis web application built using **Python**, **Streamlit**, and **TextBlob**.

---

## 🚀 Features

- **Text Input**: Enter any sentence or paragraph to analyze.
- **Sentiment Classification**: Categorizes text into **Positive**, **Negative**, or **Neutral**.
- **Polarity Score**: Calculates sentiment polarity ranging from `-1.0` (most negative) to `+1.0` (most positive).
- **Subjectivity Score**: Measures factual vs opinion-based language (`0.0` to `1.0`).
- **Clean UI**: Visual badge, polarity gauge, and sample sentences for quick testing.
- **Input Validation**: Gracefully handles empty or whitespace-only inputs.
- **100% Free & Local**: No external paid APIs or API keys required.

---

## 🛠️ Prerequisites

- **Python 3.9 or newer** installed on Windows.
- **VS Code** (or any preferred terminal / IDE).

---

## 📦 Installation & Setup

### 1. Open the Project in VS Code
Open the project directory in VS Code:
```powershell
code "Sentiment Analysis System"
```

### 2. (Optional but Recommended) Create a Virtual Environment
Open the integrated terminal in VS Code (`Ctrl + ` ` ` or **Terminal > New Terminal**) and run:
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install the required packages using `requirements.txt`:
```powershell
py -m pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit app with the following command:

```powershell
py -m streamlit run app.py
```
*(If `python` is added to your system PATH, you can also use `streamlit run app.py` or `python -m streamlit run app.py`)*

Once started, Streamlit will automatically open the web app in your default browser at:
```
http://localhost:8501
```

---

## 📊 How Sentiment Classification Works

| Sentiment | Polarity Condition | Description |
| :--- | :--- | :--- |
| **Positive 😊** | `Polarity > 0.0` | Indicates favorable, happy, or constructive sentiment. |
| **Neutral 😐** | `Polarity == 0.0` | Indicates factual or objective text with no clear emotion. |
| **Negative 😞** | `Polarity < 0.0` | Indicates critical, unhappy, or unfavorable sentiment. |

---

## 📁 Project Structure

```
Sentiment Analysis System/
├── app.py              # Main Streamlit web application
├── requirements.txt    # Project dependencies
└── README.md           # Instructions and documentation
```
