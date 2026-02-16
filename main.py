from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://openoa-1-b9wy.onrender.com",   # your frontend
    "*"   # optional (allow all — easiest for assignment)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 🔥 simplest fix
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "OpenOA Backend Running 🚀"}

@app.get("/health")
def health():
    return {"status": "OpenOA is Live ✅"}
