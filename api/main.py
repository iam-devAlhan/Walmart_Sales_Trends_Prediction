from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

cors = CORSMiddleware(app=app,
                      allow_origins=["*"]
                      ,allow_methods=["GET", "POST"]
                      ,allow_headers=["*"]
                      ,allow_credentials=True)

@app.post("/predict")
async def predict():
    pass

