from fastapi import FastAPI
import openoa

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OpenOA Backend Running 🚀"}

@app.get("/health")
def health():
    return {"status": "OpenOA is Live ✅"}
