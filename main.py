from fastapi import FastAPI
from routers import auth_routs


app = FastAPI()


app.include_router(auth_routs.router)

@app.get("/api/health-check", tags=["health_check"])
def health_check():
    return {"status": "healthy and running"}
