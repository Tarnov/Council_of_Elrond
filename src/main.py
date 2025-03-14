import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from src.logger import logger
from src.orchestrator import router
from src.config import config

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as http_exception:
            logger.error(f"HTTP error: {http_exception.detail}")
            return JSONResponse(status_code=http_exception.status_code, content={"error": http_exception.detail})
        except Exception as e:
            logger.error(f"Unhandled error: {str(e)}")
            return JSONResponse(status_code=500, content={"error": "Internal Server Error"})

app = FastAPI()
app.add_middleware(ExceptionHandlerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix='/orchestrator')

@app.get('/')
def read_root():
    logger.info("Root endpoint accessed")
    return {'message': 'Welcome to the Council of Elrond!'}

if __name__ == '__main__':
    logger.info(f"Starting {config.APP_NAME} on {config.HOST}:{config.PORT} (Debug: {config.DEBUG})")
    uvicorn.run(app, host=config.HOST, port=config.PORT)
