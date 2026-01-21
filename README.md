# 📘 University Policy RAG System

**An End-to-End Retrieval-Augmented Generation (RAG) Application**
**Built for Internship Technical Evaluation**

---

## 🌟 Overview

This project is a **Retrieval-Augmented Generation (RAG) system** designed to answer questions about **university policies** using a document-based knowledge base.

The system follows a strict RAG workflow:

* Documents are indexed and embedded
* Relevant context is retrieved for each question
* Answers are generated **only from retrieved content**
* Sources are explicitly shown
* If information is unavailable, the system clearly says so

This project demonstrates **end-to-end RAG architecture**, clean backend design, frontend integration, and practical deployment decision-making.

---

## 🧠 What the System Does

The system:

* Reads policy documents from a custom knowledge base
* Splits documents into small, meaningful chunks
* Creates semantic embeddings
* Stores embeddings in a local index
* Retrieves the most relevant chunks for a user question
* Uses an LLM (OpenAI) to generate a **grounded answer**
* Returns both the **answer** and its **sources**

If the required information is not present, the system responds with:

> **Not enough information in the knowledge base.**

---

## 🗂 Folder Structure

```
Policy-Rag-System/
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
├── storage/
│   ├── documents.pkl
│   └── embeddings.npy
│
├── requirements.txt
└── README.md
```

---

## 🎯 Key Features

### 🔹 1. Knowledge Base & Indexing

* Loads all policy documents from the `data/` directory
* Splits documents into readable chunks
* Generates sentence embeddings using **Sentence Transformers**
* Stores embeddings in a persistent local index
* Indexing can be triggered via the backend API or UI

---

### 🔹 2. Retrieval & Generation Pipeline

This is the core RAG workflow:

1. User enters a question
2. Question is converted into an embedding
3. Top-K most similar document chunks are retrieved
4. Only retrieved chunks are passed to the LLM
5. LLM generates a grounded answer
6. The system returns:

   * Final answer
   * Source documents with previews

If retrieval confidence is insufficient, the system **does not hallucinate**.

---

### 🔹 3. Frontend UI

* Clean, minimal, evaluator-friendly interface
* Two main actions:

  * **Build Index**
  * **Ask Question**
* Displays answers and clearly labeled sources
* Designed to demonstrate system behavior, not visual complexity

---

## 🌍 Live Evaluation Access

The system is demonstrated via a **live public URL** during evaluation to allow direct testing of:

* Indexing
* Retrieval quality
* Grounded answer generation
* Fallback behavior

> **Note:**
> Multiple deployment strategies were evaluated. Due to free-tier memory constraints on some cloud platforms when running ML workloads, the final live demonstration is provided via a secure local tunnel to ensure stable and reliable evaluation.

This ensures evaluators can test the **complete RAG pipeline without platform-induced failures**.

---

## 🛠 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Maryam-Nisar-Ahmad/Policy-Rag-System.git
cd Policy-Rag-System
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set OpenAI API key

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

### 5️⃣ Run the backend

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

### 6️⃣ Open the application

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔍 API Overview

### **POST /api/index**

Builds the document index.

**Response**

```json
{
  "message": "indexed 45 chunks"
}
```

---

### **POST /api/query**

Ask a question to the RAG system.

**Request**

```json
{
  "question": "What happens if a student commits plagiarism?"
}
```

**Response**

```json
{
  "answer": "...",
  "sources": [
    {
      "document": "plagiarism_policy.txt",
      "preview": "..."
    }
  ]
}
```

---

## 🖥 Frontend UI

<img width="1020" height="450" alt="image" src="https://github.com/user-attachments/assets/e2949575-833d-4c08-939f-312b85c853fa" />

---

## 📚 Knowledge Base & Indexing

<img width="1025" height="439" alt="image" src="https://github.com/user-attachments/assets/a53b676c-b334-496a-bf24-3924038a62ed" />

---

## 🔄 Retrieval & Generation Pipeline

<img width="1011" height="914" alt="image" src="https://github.com/user-attachments/assets/87f9c27d-2f4e-41df-846b-3e7338642e65" />

---

## 🧪 Suggested Evaluation Questions

### Supported (should answer):

* What happens if a student commits plagiarism?
* What is the attendance requirement for undergraduate students?
* What items are banned in the examination hall?
* What happens if fees are unpaid?
* What does a grade of D represent?

### Unsupported (should return fallback):

* What is the hostel curfew time?
* When does the sports festival start?
* How many buses does the university have?

---

## ⚠️ Edge Cases Handled

✔ Empty question validation
✔ Indexing required before querying
✔ Low-relevance fallback handling
✔ Strict grounding (no hallucination)
✔ Source transparency
✔ Clear user feedback during indexing

---

## 🧩 Technologies Used

* Python
* FastAPI
* Sentence Transformers
* NumPy
* OpenAI API
* HTML / CSS / JavaScript
* ngrok (evaluation-time deployment)
