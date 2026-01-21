from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.models import QuestionIn, AnswerOut, SourceOut
from app.indexing import build_index
from app.retrieval import search_docs
from app.generation import generate_answer


app = FastAPI(title="Policy RAG Service")

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # safe for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#frontend
# serve frontend folder
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    """
    Serves the main frontend UI
    """
    frontend_path = os.path.join("frontend", "index.html")
    with open(frontend_path, "r", encoding="utf-8") as f:
        return f.read()


#API
@app.post("/api/index")
def index_data():
    count = build_index()
    return {"message": f"indexed {count} chunks"}


@app.post("/api/query", response_model=AnswerOut)
def query(payload: QuestionIn):
    q = payload.question.strip()

    if not q:
        raise HTTPException(status_code=400, detail="empty question")

    docs = search_docs(q)

    if not docs:
        return AnswerOut(
            answer="Not enough information in the knowledge base.",
            sources=[]
        )

    context = "\n".join(d["content"] for d in docs)
    answer = generate_answer(context, q)

    #Critical rule (no sources if unsupported )
    if answer.strip() == "Not enough information in the knowledge base.":
        return AnswerOut(answer=answer, sources=[])

    sources = [
        SourceOut(
            document=d["source"],
            preview=d["content"][:200]
        )
        for d in docs
    ]

    return AnswerOut(answer=answer, sources=sources)
