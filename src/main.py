import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from fastapi import FastAPI
from src.orchestrator import router

app = FastAPI()
app.include_router(router, prefix='/orchestrator')

@app.get('/')
def read_root():
    return {'message': 'Welcome to the Council of Elrond!'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
from src.logger import logger
