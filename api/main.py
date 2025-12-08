from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"]
                   ,allow_methods=["GET", "POST"]
                   ,allow_headers=["*"]
                   ,allow_credentials=True)


@app.get("/predict")
async def predict():
    pass


@app.get("/")
async def root():
    return JSONResponse({"message": "ASGI Server running on Port 8000"}, status_code=200)

