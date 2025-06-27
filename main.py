from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from song import router as song_router
from user import router as user_router
import os

app = FastAPI()

# Configure CORS for production
if os.getenv('PRODUCTION') == 'true':
    origins = [
        "https://your-vercel-app.vercel.app",  # Your frontend URL
        # Add other allowed origins
    ]
else:
    origins = [
        "http://localhost:3000",  # Local development
        "http://127.0.0.1:3000",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(song_router, prefix="/songs", tags=["Songs"])
app.include_router(user_router, prefix="/user", tags=["User"])