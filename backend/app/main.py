"""
This is the main module which integrates all the other backend related modules
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import api

app = FastAPI(title="Help-Survey", openapi_url="/survey/apis")

# To handle CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://15.207.159.86"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(router=api.app, prefix="/survey")

if __name__ == "__main__":
    uvicorn.run(
                app,
                access_log=False,
                port=5000,
                debug=True,
                reload=True
               )
