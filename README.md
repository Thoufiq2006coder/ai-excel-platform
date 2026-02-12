# 📊 AI-Powered Smart Spreadsheet (Hackathon Project)

An intelligent data analysis platform that combines the familiarity of a spreadsheet interface with the power of Google Gemini AI. Users can upload datasets, ask questions in plain English, and receive instant insights, charts, and formulas.

## 🚀 Features

* **📂 Drag & Drop Upload:** Instantly parses CSV and Excel files.
* **🤖 AI Analyst:** Integrated with **Google Gemini 1.5 Flash** to answer questions like "Summarize this data" or "Find the trend."
* **⚡ Real-Time Calculation:** Python Backend (FastAPI) processes data in milliseconds.
* **⬇️ Export:** Download your analyzed and modified datasets.
* **🔐 Architecture:** Separation of concerns with a RESTful API (Backend) and Responsive UI (Frontend).

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript.
* **Backend:** Python 3.10, FastAPI, Uvicorn.
* **AI Engine:** LangChain + Google Gemini API.
* **Data Processing:** Pandas, OpenPyXL.

## ⚙️ How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AI-Smart-Spreadsheet.git](https://github.com/YOUR_USERNAME/AI-Smart-Spreadsheet.git)
    cd AI-Smart-Spreadsheet
    ```

2.  **Start the Backend**
    ```bash
    cd backend
    pip install -r requirements.txt
    python main.py
    ```

3.  **Start the Frontend**
    ```bash
    cd ../frontend
    python -m http.server 3000
    ```

4.  **Access the App**
    Open `http://localhost:3000` in your browser.

## 🏆 Hackathon Compliance

This project meets the requirements for **Level 2 Open Innovation**:
* ✅ **Complex Data Relationships:** Handles structured datasets (Rows/Columns) and maps them to AI contexts.
* ✅ **Real-time API:** FastAPI backend serving live data analysis.
* ✅ **User-Centric UI:** Clean, intuitive interface for non-technical users.

---
*Built with ❤️ for the Hackathon.*
