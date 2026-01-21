import os
from openai import OpenAI


def generate_answer(context, question):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Not enough information in the knowledge base."

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are answering questions using ONLY the information provided below.

Context:
{context}

Rules:
- Do not use any outside knowledge.
- If the answer is not clearly present in the context, say:
  "Not enough information in the knowledge base."

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content.strip()
