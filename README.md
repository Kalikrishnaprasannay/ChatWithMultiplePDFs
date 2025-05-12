# ChatWithMultiplePDFs
Here's a **GitHub-friendly README.md** for your project:

---

# Chat with Multiple PDFs (Offline & Free Version)

This project provides a local solution for interacting with multiple PDFs by answering questions based on their content. Built with **Streamlit**, **FAISS**, **Sentence-Transformers**, and **Flan-T5**, this app enables offline document-based Q\&A. It does not require any external APIs or internet connection once the model is downloaded.

---

## 🚀 Features

* **Upload Multiple PDFs**: Upload multiple PDF files for interaction.
* **Question-Answering**: Ask questions and get answers based on the content of the uploaded PDFs.
* **Offline Operation**: Entire system works offline once the model is downloaded.
* **Fast Search**: Uses **FAISS** for fast retrieval of relevant content from uploaded PDFs.
* **Lightweight**: Uses the CPU-friendly **Flan-T5** model, ideal for machines with **16 GB RAM**.

---

## 🛠️ Requirements

* **Python 3.x** (preferably 3.7 or higher)
* **16 GB RAM** or higher (CPU-only)
* **Libraries**:

  * `streamlit`
  * `sentence-transformers`
  * `faiss-cpu`
  * `PyPDF2`
  * `transformers`
  * `torch`

---

## 📥 Installation

### 1. Clone the Repository

You can clone this repository by running:

```bash
git clone https://github.com/Kalikrishnaprasannay/ChatWithMultiplePDFs.git
cd ChatWithMultiplePDFs
```

Alternatively, download the ZIP file and extract it.

### 2. Install Dependencies

Navigate to the project folder and install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the App

After installing dependencies, start the Streamlit app:

```bash
streamlit run app.py
```

This will launch the app in your default browser. You will be able to upload PDF files, ask questions, and get answers based on the content of the PDFs.

---

## 📝 How It Works

### 1. Upload PDFs

Upload multiple PDFs via the Streamlit interface. The app will read and extract text from these PDFs using **PyPDF2**.

### 2. Text Chunking & Embedding

The extracted text is split into smaller chunks and converted into embeddings using **Sentence-Transformers** (`all-MiniLM-L6-v2`).

### 3. FAISS Vector Index

A **FAISS** index is created from the text embeddings for fast, similarity-based search.

### 4. Question Answering

When a user submits a question, the relevant document chunks are retrieved, and the **Flan-T5-Base** model is used to generate an answer based on the selected content.

### 5. Answer Display

The generated answer is displayed in the app interface.

---

## 🛠️ Contributing

Feel free to fork the repository and submit pull requests. If you find bugs or have feature requests, please open an issue.

---

![Screenshot (181)](https://github.com/user-attachments/assets/0ec7d54b-46a5-48c3-9155-ac8d67772197)

Let me know if you want to adjust any sections or add more details!
