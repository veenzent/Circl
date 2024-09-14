from fastapi import FastAPI


app = FastAPI(
    title="Circl API",
    description="A real-time messaging API that enables users to communicate instantly.",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}