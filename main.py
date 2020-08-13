"""
Sample Endpoint for Qxf2 Survey Application
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    "Returns the Message for Mock Data"
    return {"msg": "Mock Data for the Survey"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        access_log=False,
        port=5000,
        debug=True,
        reload=True
    )