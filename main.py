"""
This file is the start file for Fast Api
"""
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import ai_system, user_management, dietitian
from connections.postgres_connection import DBResourceManager

diet_management=DBResourceManager(db_key="diet_management")

load_dotenv()

app = FastAPI(
    title="Diet Planning and Nutrition Management Application",
    version="1.0",
    description="Diet Planning and Nutrition Management Application",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(ai_system.router, prefix="/aiSystem", tags=["aiSystem"])
app.include_router(dietitian.router, prefix="/dietitian", tags=["dietitian"])
app.include_router(user_management.router, prefix="/userManagement", tags=["userManagement"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
