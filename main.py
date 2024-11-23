"""
This file is the start file for Fast Api
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware.sessions import SessionMiddleware
from routers import ai_system, user_management, dietitian
from connections.postgres_connection import DBResourceManager

diet_management=DBResourceManager(db_key="diet_management")

load_dotenv()
# os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

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

# app.add_middleware(SessionMiddleware, secret_key=os.getenv("GOOGLE_API_KEY"))
app.include_router(ai_system.router, prefix="/aiSystem", tags=["aiSystem"])
app.include_router(dietitian.router, prefix="/dietitian", tags=["dietitian"])
app.include_router(user_management.router, prefix="/userManagement", tags=["userManagement"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
