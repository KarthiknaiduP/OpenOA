import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "OpenOA Backend Running"}

@app.get("/health")
def health():
    return {"status": "OpenOA is Live"}

@app.get("/data")
def get_data():
    return {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "values": [random.randint(50, 150) for _ in range(6)]
    }
