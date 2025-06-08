from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Allow CORS for local dev and extension usage
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CARBON_INTERFACE_API_KEY = "your_api_key_here"  # Replace this with your actual API key

@app.get("/emissions")
async def get_emissions(asin: str = Query(None), title: str = Query(None)):
    try:
        # Temporary fallback logic based on title
        estimate = estimate_by_title(title or "")

        # Optional: Call Carbon Interface (stubbed here for demo)
        headers = {
            "Authorization": f"Bearer {CARBON_INTERFACE_API_KEY}",
            "Content-Type": "application/json",
        }

        # You can integrate actual logic here with their endpoints
        # Example: GET /v1/estimates
        # But they do not support product-level estimation, so we fake it here

        return {
            "carbon_kg": estimate,
            "source": "Category-based estimate (fallback)"
        }

    except Exception as e:
        return {"error": str(e)}

def estimate_by_title(title):
    title = title.lower()
    if "laptop" in title:
        return 120
    if "iphone" in title or "smartphone" in title:
        return 65
    if "tv" in title:
        return 200
    return 80  # default fallback
