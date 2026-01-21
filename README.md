# 📘 University Policy RAG System

**An End-to-End Retrieval-Augmented Generation Application**
**Built for the Internship Technical Task**

---

## 🌟 Overview

This project is a **fully functional Retrieval-Augmented Generation (RAG) system** that can answer questions about **university policies**.

It:

* Reads documents from a **custom knowledge base**
* Splits them into chunks
* Creates **embeddings**
* Stores them in a local **index**
* Retrieves the most relevant chunks for a question
* Uses an **LLM (OpenAI)** to generate an answer using ONLY the retrieved text

The system includes:

* **Backend (FastAPI)**
* **Frontend (HTML/CSS/JS)**
* **Local indexing**
* **Cosine-similarity based retrieval**
* **LLM-based answer generation**
* **Deployment on Render**
* **Public live URL**

This README explains everything clearly so anyone can:

* Understand the system
* Run it locally
* Review the architecture
* Deploy it again

---

# 🗂 Folder Structure

```
RAG-APP/
│
├── app/
│   ├── api.py
│   ├── generation.py
│   ├── indexing.py
│   ├── retrieval.py
│   ├── models.py
│   └── settings.py
│
├── data/
│   ├── attendance_policy.txt
│   ├── disciplinary_actions.txt
│   ├── examination_rules.txt
│   ├── grading_system.txt
│   ├── plagiarism_policy.txt
│   └── registration_and_fees.txt
│
├── frontend/
│   └── index.html
│
├── storage/        # created at runtime (gitignored)
│   ├── documents.pkl
│   └── embeddings.npy
│
├── requirements.txt
└── README.md

```

---

# 🎯 Key Features

### 🔹 1. **Knowledge Base + Indexing**

* Loads all `.txt` policy documents
* Converts them into small readable chunks
* Creates sentence embeddings using *Sentence Transformers*
* Stores them in a local index file
* Can rebuild index anytime using a button in the UI

---

### 🔹 2. **Retrieval + Generation Pipeline**

This is the heart of the system.

Steps:

1. User enters a question
2. Question is embedded
3. Top-K similar document chunks are retrieved
4. Only those chunks are sent to the LLM
5. LLM generates a grounded answer
6. The system returns:

   * final answer
   * sources (document + snippet)

If the system doesn’t find enough relevant context:

> **Not enough information in the knowledge base.**

---

### 🔹 3. **Frontend UI**

* Fully responsive
* Modern, clean design
* Simple two-button interface:

  * **Build Index**
  * **Ask Question**
* Sources displayed neatly under the answer

---

### 🔹 4. **Deployment**

* Backend deployed on **Render**
* Public API URL
* Frontend also hosted automatically
* Environment variables securely stored

---

# 🌍 Live Demo URL (replace after deployment)

```
https://policy-rag-system-rxn0.onrender.com/
```

---

# 🛠 How to Run Locally

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Maryam-Nisar-Ahmad/Policy-Rag-System.git
cd YOUR-REPO
```

## 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

### Windows:

```bash
venv\Scripts\activate
```

### Mac/Linux:

```bash
source venv/bin/activate
```

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Add your OpenAI API key

Create `.env` file in the root:

```
OPENAI_API_KEY = your_key_here
```

OR set in PowerShell:

```bash
setx OPENAI_API_KEY "your_key_here"
```

## 5️⃣ Run backend

```bash
uvicorn app.api:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

## 6️⃣ Access frontend locally

After starting the backend, open the following URL in your browser:

```
http://127.0.0.1:8000/
```

The frontend is served automatically by the FastAPI backend.

---

# 🚀 Deployment Instructions (Render)

## 1️⃣ Create Render account

(https://render.com/)

## 2️⃣ Create a new Web Service

* Connect your GitHub repo
* Environment: **Python 3.10+**
* Start command:

  ```
  uvicorn app.api:app --host 0.0.0.0 --port 10000
  ```
* Add environment variable:

  ```
  OPENAI_API_KEY = your_key_here
  ```

## 3️⃣ Deploy

Render will automatically:

* Install dependencies
* Start the FastAPI server
* Give you a public URL

## 4️⃣ Visit your frontend

The frontend is served directly by the FastAPI backend at the root URL (`/`).

Once deployed, open the Render service URL in your browser to access the full application.
No separate frontend hosting is required.

---

# 🔍 API Documentation

## **POST /api/index**

Builds embeddings + index

### Response

```json
{
  "message": "indexed 45 chunks"
}
```

---

## **POST /api/query**

Ask a question to the RAG system.

### Body:

```json
{
  "question": "What happens if a student commits plagiarism?"
}
```

### Response:

```json
{
  "answer": "...",
  "sources": [
    {
      "document": "plagiarism_policy.txt",
      "preview": "...."
    }
  ]
}
```

---
# Frontend UI section

<img width="1020" height="450" alt="image" src="https://github.com/user-attachments/assets/e2949575-833d-4c08-939f-312b85c853fa" />

# Knowledge Base + Indexing
<img width="1025" height="439" alt="image" src="https://github.com/user-attachments/assets/a53b676c-b334-496a-bf24-3924038a62ed" />

# Retrieval + Generation Pipeline
<img width="1011" height="914" alt="image" src="https://github.com/user-attachments/assets/87f9c27d-2f4e-41df-846b-3e7338642e65" />

---

# 🧪 Suggested Test Questions

Use these to demonstrate evaluation quality:

### Positive (should answer):

* *What happens if a student commits plagiarism?*
* *What is the attendance requirement for undergraduate students?*
* *What items are banned in the examination hall?*
* *What happens if fees are unpaid?*
* *What does a grade of D represent?*

### Negative (should return “Not enough information…”):

* *What is the hostel curfew time?*
* *When does the sports festival start?*
* *How many buses does the university have?*

---

# ⚠️ Edge Cases Handled

✔ Empty question → returns error
✔ Index not built → user must click “Build Index”
✔ Low relevance → returns fallback message
✔ Strict grounding → no hallucinations
✔ All sources included
✔ Button state handling during indexing

---

# 🧩 Technologies Used

* **Python**
* **FastAPI**
* **Sentence Transformers**
* **NumPy**
* **OpenAI API**
* **HTML + CSS + JavaScript**
* **Render (Deployment)**
