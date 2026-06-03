from fastapi import FastAPI
from routers import auth


app = FastAPI()


app.include_router(auth.router)

@app.get("/health-check", tags=["health_check"])
def health_check():
    return {"status": "healthy and running"}
