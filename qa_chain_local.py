from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import faiss
import numpy as np

class LocalPDFQA:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.text_chunks = []
        self.index = None
        self.device = 'cpu'  # Force CPU
        self.model_name = "google/flan-t5-base"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).to(self.device)

    def split_text(self, text, chunk_size=500):
        self.text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    def build_vector_index(self):
        embeddings = self.embedder.encode(self.text_chunks)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def query(self, question: str) -> str:
        question_embedding = self.embedder.encode([question])
        D, I = self.index.search(question_embedding, k=3)
        context = "\n".join([self.text_chunks[i] for i in I[0]])

        prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True).to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=150)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
