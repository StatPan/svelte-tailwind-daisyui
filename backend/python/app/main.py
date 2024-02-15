from typing import Union
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
import numpy as np
import subprocess

model_path = "/home/statpan/project/js-project/svelte-tailwind-daisyui/backend/python/models/kf-deberta-multitask"
vector_model = SentenceTransformer(model_path)

app = FastAPI()

class VectorRequest(BaseModel):
    sentence: str
    
class VectorResponse(BaseModel):
    vector: list[float]

def is_over_maxlength(sentence):
    if len(sentence) == 0:
        return True
    
    length = vector_model.tokenize([sentence])["input_ids"][0].__len__()
    return True if length > 512 else False


@app.post("/vector")
async def return_vector(request:VectorRequest) -> JSONResponse:
    sentence = request.sentence
    if not is_over_maxlength(sentence):
        vector_list = vector_model.encode(request.sentence).tolist()
        return JSONResponse(content=vector_list)
    
if __name__ == "__main__":
    subprocess.check_call(["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"])