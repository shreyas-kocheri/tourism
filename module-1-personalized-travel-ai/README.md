# 🔱 TRINETRA AI  
### Personalized • Safety-First • Agentic Travel Planner for India

> **“Even when the path ends, the journey does not.”**

---

## 📌 Project Overview

**Trinetra AI** is an AI-powered travel intelligence platform designed specifically for **real Indian travel conditions**.

It provides **personalized, safety-aware, and culturally intelligent travel plans** by combining structured user inputs with **agentic AI reasoning** and **local LLMs (Ollama)**.

This project focuses on:
- Family & child-safe travel
- Spiritual and cultural tourism
- Low-budget and eco-friendly planning
- Emergency-aware (SOS) travel logic
- Day-wise, human-readable itineraries

---

## 🧠 What Inputs Does Trinetra AI Use?

From the frontend UI, users provide:

- 👥 **Number of people**
- 🎂 **Age & gender of each person**
- 📍 **Starting location**
- 🎯 **Destination**
  - If unknown → AI predicts suitable destinations
- 💭 **Interest / mood**
  - spiritual / adventure / relaxed / mixed
- ⏰ **Travel time**
  - `now` → SOS mode
  - `later` → normal planning
- 📅 **Travel dates (optional)**
- 💰 **Budget**
- 🌐 **Preferred language**

---

## 🚨 SOS MODE (Travel Now Logic)

When **Travel Time = now**, Trinetra AI automatically:

- Prioritizes safety over speed
- Avoids risky or overcrowded routes
- Mentions nearby hospitals & police stations
- Suggests safer transport options
- Adjusts plans for children and families

---

## 🧭 How the System Works (Agentic Flow)

Trinetra AI uses an **agent-based workflow**:

Plan Phase → Identify destinations
Research Phase → Gather location information
Generate Phase → Create travel plan
Reflect Phase → Detect gaps & issues
Improve Phase → Produce final refined plan


This makes the output **more reliable and structured** than a single-step AI response.

---

## 🏙 Output Structure

Each generated plan includes:

### 📆 DAY-WISE TRAVEL PLAN
- Day 1–2, Day 3–4, etc.
- Day / Night awareness

### 🕉 CULTURAL / SPIRITUAL IMPORTANCE
- Temples, heritage sites, rituals
- Local cultural context

### 👥 CROWD PREDICTION & BACKUP PLANS
- Peak vs off-peak guidance
- Alternate routes or places

### 🧳 TRAVEL ESSENTIALS
- Clothing
- Medicines
- Food & water tips

### 🌱 ECO-FRIENDLY & PLASTIC-FREE ADVICE
- Sustainable travel practices
- Responsible tourism guidance

At the end of the plan, the UI displays:

> **“Even when the path ends, the journey does not.”**

---

## 🏗 Technology Stack

### Backend
- Python
- FastAPI
- Ollama (local LLMs)
- Agentic AI workflow

### Frontend
- Next.js (App Router)
- React + TypeScript
- Tailwind CSS

### AI Models
- llama3
- qwen2:7b
- mistral / gemma (if available)

---

## 📂 Project Structure

trinetra-ai-travel-planner/
│
├── backend/
│ ├── api.py # FastAPI endpoints
│ ├── agent.py # Agentic workflow
│ ├── tools.py # Reasoning tools
│ └── app.py # Gradio UI (optional)
│
├── frontend/
│ ├── app/
│ │ ├── page.tsx
│ │ └── layout.tsx
│ ├── globals.css
│ └── tailwind.config.js


---

## ▶️ How to Run

### 1️⃣ Start Ollama
```bash
ollama pull llama3
ollama serve

2️⃣ Start Backend

cd backend
uvicorn api:app --reload

3️⃣ Start Frontend

cd frontend
npm install
npm run dev

🌟 Why Trinetra AI is Different

❌ Not a simple chatbot
❌ Not static travel suggestions

✅ Agentic reasoning
✅ Safety-first logic
✅ Built for Indian tourism realities
✅ Cultural & spiritual awareness
🚀 Future Scope

    Community live updates

    Trust validation (like / dislike)

    Rewards for local contributors

    District-wise RAG tourism knowledge

    Multilingual responses

    Emergency alert integration

👨‍💻 Author

Sakthivel S M
📧 Email: s.m.sakthivelofficial@gmail.com
📜 Philosophy

Travel is not just about destinations —
it is about safety, awareness, culture, and growth.

Trinetra AI plans journeys that think like humans.