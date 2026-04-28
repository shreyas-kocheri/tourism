from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import ollama

from models import TravelRequest

app = FastAPI(title="TRINETRA AI – Tourism Intelligence")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# AI DESTINATION SUGGESTION
# -----------------------------
@app.post("/trinetra/suggest-destination")
def suggest_destination(req: TravelRequest):
    """
    Used ONLY when destination_known = False
    """

    prompt = f"""
You are an Indian tourism expert.

START LOCATION:
{req.start_location}

GROUP DETAILS:
{req.people}

BUDGET:
{req.budget} ({req.budget_style})

MOOD / ENERGY:
{req.mood}

INTEREST TYPE:
{req.interests}

SPECIAL EXPERIENCE:
{req.experiences}

TASK:
Suggest exactly 3 Indian destinations.

For each destination:
- Why it fits the budget
- Why it matches the mood & interests
- Crowd level (Low / Medium / High)

Rules:
- Keep responses concise
- No hallucinated facts
- No markdown headings
"""

    response = ollama.generate(
        model="qwen2:7b",
        prompt=prompt
    )

    return {
        "ai_suggestions": response["response"],
        "next_step": "Ask user to confirm or change destination"
    }

# -----------------------------
# FINAL TRAVEL PLAN
# -----------------------------
@app.post("/trinetra/travel-plan")
def generate_travel_plan(req: TravelRequest):

    if not req.destination:
        raise HTTPException(
            status_code=400,
            detail="Destination is required to generate final plan"
        )

    prompt = f"""
You are TRINETRA AI – a responsible, safety-aware tourism assistant for India.

====================
PERSONA MODE
====================
{req.persona}

Rules:
- guide → informative, cultural, structured
- friend → friendly, simple, casual
- emergency → short, urgent, safety-first

====================
LANGUAGE
====================
{req.language}

Rules:
- If Tamil → respond fully in simple Tamil
- If Hindi → respond fully in simple Hindi
- Else → English

====================
TRIP INPUT
====================

START LOCATION:
{req.start_location}

DESTINATION(S):
{req.destination}

PEOPLE DETAILS:
{req.people}

BUDGET:
{req.budget} ({req.budget_style})

MOOD / ENERGY:
{req.mood}

INTEREST TYPE:
{req.interests}

SPECIAL EXPERIENCE:
{req.experiences}

USER PREFERENCES:
{req.suggestions}

WALKING TOLERANCE:
{req.walking_tolerance}

CROWD PREFERENCE:
{req.crowd_preference}

TRAVEL TIME:
{req.travel_time}

====================
IMPORTANT RULES
====================
- STRICT DAY-WISE itinerary
- ALL section headings in **BOLD**
- Avoid unrelated nearby locations
- Consider children & senior safety
- Do NOT mention AI limitations
- Do NOT reveal chain-of-thought

====================
TASKS
====================

1. **DAY-WISE TRAVEL PLAN**
2. **CULTURAL / SPIRITUAL IMPORTANCE**
3. **CROWD PREDICTION & BACKUP PLANS**
4. **ROUTE & SAFETY TIPS**
5. **TRAVEL ESSENTIALS**
6. **ECO-FRIENDLY & PLASTIC-FREE ADVICE**
7. **WHY THIS PLAN WAS CHOSEN**
   - Group & age logic
   - Budget logic
   - Mood & interest logic
   - Timing logic

End with this exact line:
Even when the path ends, the journey does not.
"""

    response = ollama.generate(
        model="qwen2:7b",
        prompt=prompt
    )

    return {
        "final_plan": response["response"],
        "note": "Crowd & weather insights are simulated for demo purposes"
    }
