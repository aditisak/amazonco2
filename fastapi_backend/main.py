from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Allow requests from all origins (including Chrome extensions)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Replace this with your real API key from Carbon Interface
CARBON_INTERFACE_API_KEY = "your_api_key_here"

@app.get("/")
def root():
    return {"message": "Amazon Carbon API is running."}

@app.get("/emissions")
async def get_emissions(asin: str = Query(None), title: str = Query(None)):
    """
    Estimates carbon footprint based on product title or ASIN.
    This version uses simple keyword matching and stubs Carbon Interface integration.
    """
    try:
        if not title:
            return {"error": "Missing product title"}

        # Use a keyword-based estimate
        estimate = estimate_by_title(title)

        # Optional: Make a real call to Carbon Interface here
        # This is just a placeholder. Carbon Interface does NOT support product-level estimates.
        headers = {
            "Authorization": f"Bearer {CARBON_INTERFACE_API_KEY}",
            "Content-Type": "application/json",
        }

        # Example stub for future Carbon Interface integration
        # response = await httpx.get("https://www.carboninterface.com/api/v1/...", headers=headers)

        return {
            "carbon_kg": estimate,
            "source": "Category-based estimate (fallback)"
        }

    except Exception as e:
        return {"error": str(e)}

def estimate_by_title(title: str) -> float:
    """
    Estimate carbon footprint (kg CO₂e) by keyword matching.
    """
    title = title.lower()
    if "laptop" in title or "macbook" in title:
        return 120
    if "iphone" in title or "smartphone" in title or "samsung" in title:
        return 65
    if "tv" in title or "oled" in title or "television" in title:
        return 200
    if "headphones" in title or "earbuds" in title:
        return 15
    if "monitor" in title:
        return 70
    return 80  # default fallback
