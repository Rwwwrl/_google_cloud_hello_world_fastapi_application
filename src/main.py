from fastapi import FastAPI, Response, status

from src.routes import api_router

app = FastAPI()


@app.get("/liveness_check")
def liveness_check():
    return Response(status_code=status.HTTP_200_OK)


@app.get("/readiness_check")
def readiness_check():
    return Response(status_code=status.HTTP_200_OK)


app.include_router(router=api_router)
