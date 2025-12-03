from fastapi import FastAPI
from app.api.v1.size_router import router as size_router
from app.api.v1.health_router import router as health_router

app = FastAPI(
    title="SizeFit API",
    version="1.0.0",
    description="API for size recommendation and body measurement prediction"
)

# Register routers
app.include_router(health_router, prefix="/api/v1/health", tags=["Health"])
app.include_router(size_router, prefix="/api/v1/size", tags=["Size Recommendation"])


@app.get("/")
def root():
    return {"message": "Welcome to SizeFit API"}
