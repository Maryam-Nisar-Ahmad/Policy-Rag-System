import os
from openai import OpenAI


def generate_answer(context, question):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "__UNSUPPORTED__"

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a Retrieval-Augmented Generation (RAG) system.

You must decide whether the context contains enough information
to answer the question.

Rules:
- Use ONLY the context.
- Do NOT use outside knowledge.
- If the context does NOT contain the answer, respond EXACTLY with:
  __UNSUPPORTED__
- If it DOES contain the answer, write a clear answer based only on the context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a strict RAG evaluator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()
