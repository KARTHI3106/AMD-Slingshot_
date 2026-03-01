# SkillGraph Setup Guide

Complete installation and configuration guide for SkillGraph.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)
4. [Neo4j Configuration](#neo4j-configuration)
5. [LLM Configuration](#llm-configuration)
6. [Database Initialization](#database-initialization)
7. [Verification](#verification)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software

**Python 3.11 or higher**
```bash
python --version
# Should output: Python 3.11.x or higher
```

**Node.js 18 or higher**
```bash
node --version
# Should output: v18.x.x or higher
```

**Git**
```bash
git --version
```

### Required Accounts

**Neo4j Aura (Free Tier)**
1. Visit https://neo4j.com/cloud/aura/
2. Sign up for a free account
3. Create a new AuraDB Free instance
4. Save the connection URI, username, and password

**Google Gemini API (Optional)**
1. Visit https://aistudio.google.com/apikey
2. Create a new API key
3. Save the key for later use

**Ollama (Optional, for local LLM)**
1. Visit https://ollama.ai
2. Download and install Ollama for your platform
3. Pull the Llama 3.2 8B model:
```bash
ollama pull llama3.2:8b
```

## Backend Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/skillgraph.git
cd skillgraph
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected packages:
- fastapi==0.115.6
- uvicorn==0.32.1
- neo4j==5.27.0
- langgraph==0.2.60
- google-generativeai==0.8.4
- aiosqlite==0.20.0
- httpx==0.28.1
- pydantic==2.10.5
- pydantic-settings==2.7.1
- python-dotenv==1.0.1
- mcp==1.3.0

### Step 4: Configure Environment Variables

Create a `.env` file in the `backend` directory:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Neo4j Configuration
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password

# Gemini Configuration (Optional)
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-3.1-pro

# LLM Provider (ollama or gemini)
LLM_PROVIDER=ollama

# Ollama Configuration (if using Ollama)
OLLAMA_BASE_URL=http://localhost:11434

# Database
SQLITE_DB_PATH=data/skillgraph.db
```

### Step 5: Verify Backend Installation

```bash
python -c "import fastapi, neo4j, langgraph; print('All imports successful')"
```

## Frontend Setup

### Step 1: Navigate to Frontend Directory

```bash
cd frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

Expected packages:
- react@18.3.1
- react-dom@18.3.1
- react-router-dom@6.28.0
- d3@7.9.0
- motion@12.34.3
- lucide-react@0.460.0
- vite@6.0.3

### Step 3: Verify Frontend Installation

```bash
npm list --depth=0
```

## Neo4j Configuration

### Step 1: Access Neo4j Aura Console

1. Log in to https://console.neo4j.io
2. Select your database instance
3. Click "Open with Neo4j Browser"

### Step 2: Verify Connection

The backend will automatically seed the database on first run. To manually verify:

```cypher
MATCH (n:Concept) RETURN count(n) as concept_count;
```

Expected result: 50+ concepts

```cypher
MATCH ()-[r:REQUIRES]->() RETURN count(r) as prerequisite_count;
```

Expected result: 120+ prerequisite relationships

### Step 3: View Sample Data

```cypher
MATCH (c:Concept {concept_id: 'ml_neural_networks'})
RETURN c;
```

```cypher
MATCH (c:Concept {concept_id: 'ml_neural_networks'})-[:REQUIRES*]->(prereq)
RETURN c, prereq;
```

## LLM Configuration

### Option 1: Ollama (Recommended for Development)

**Install Ollama:**

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download from https://ollama.ai/download

**Start Ollama Service:**
```bash
ollama serve
```

**Pull Llama 3.2 8B Model:**
```bash
ollama pull llama3.2:8b
```

**Verify Installation:**
```bash
ollama list
```

**Test Model:**
```bash
ollama run llama3.2:8b "Hello, how are you?"
```

**Configure Backend:**
Set in `.env`:
```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
```

### Option 2: Google Gemini (Cloud-based)

**Get API Key:**
1. Visit https://aistudio.google.com/apikey
2. Click "Create API Key"
3. Copy the generated key

**Configure Backend:**
Set in `.env`:
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-api-key-here
GEMINI_MODEL=gemini-3.1-pro
```

### Option 3: Hybrid (Recommended for Production)

Use Ollama as primary with Gemini as fallback:

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
GEMINI_API_KEY=your-api-key-here
GEMINI_MODEL=gemini-3.1-pro
```

The system will automatically fall back to Gemini if Ollama is unavailable.

## Database Initialization

### SQLite Database

The SQLite database is automatically created on first run. To manually initialize:

```bash
cd backend
python -c "from services import student_service; import asyncio; asyncio.run(student_service.init_db())"
```

### Neo4j Graph Database

The graph database is automatically seeded on first run. To manually seed:

```bash
cd backend
python -c "from services.neo4j_service import Neo4jService, seed_from_files; import asyncio; async def seed(): svc = Neo4jService(); await svc.connect(); await seed_from_files(svc); await svc.close(); asyncio.run(seed())"
```

## Running the Application

### Start Backend Server

```bash
cd backend
# Activate virtual environment if not already active
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

uvicorn main:app --reload --port 8000
```

Backend will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/v1/health

### Start Frontend Development Server

Open a new terminal:

```bash
cd frontend
npm run dev
```

Frontend will be available at:
- Application: http://localhost:5173

## Verification

### Backend Health Check

```bash
curl http://localhost:8000/api/v1/health
```

Expected response:
```json
{
  "status": "ok",
  "neo4j": "connected",
  "agents": [
    {
      "name": "Diagnostic Agent",
      "description": "...",
      "capabilities": ["diagnose_gaps", "classify_errors", "generate_quiz"]
    },
    {
      "name": "Pathway Agent",
      "description": "...",
      "capabilities": ["plan_remediation", "exam_triage"]
    },
    {
      "name": "Content Agent",
      "description": "...",
      "capabilities": ["generate_content", "generate_lesson"]
    }
  ]
}
```

### Test Quiz Generation

```bash
curl http://localhost:8000/api/v1/quiz/machine_learning
```

Expected: JSON array with 10 quiz questions

### Test Frontend

1. Open http://localhost:5173
2. Click "Demo Mode" toggle
3. Select "Priya Sharma" from dropdown
4. Navigate to "Knowledge Graph"
5. Verify graph visualization loads

### Test Complete Flow

1. Navigate to "Find My Gaps"
2. Take a quiz on "Machine Learning"
3. Submit answers
4. Verify results show:
   - Concept scores
   - Identified gaps
   - Root cause chains
   - Agent activity log
5. Navigate to "Remediation"
6. Verify remediation plan shows:
   - Day-by-day schedule
   - Micro-lessons for each gap
   - Estimated study hours

## Troubleshooting

### Backend Issues

**Import Error: No module named 'fastapi'**
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

**Neo4j Connection Failed**
- Verify Neo4j URI, username, and password in `.env`
- Check Neo4j Aura instance is running
- Ensure URI starts with `neo4j+s://` for secure connection
- Test connection in Neo4j Browser

**Ollama Connection Failed**
- Verify Ollama is running: `ollama list`
- Check OLLAMA_BASE_URL in `.env`
- Ensure Llama 3.2 8B model is pulled: `ollama pull llama3.2:8b`
- System will automatically fall back to Gemini if configured

**SQLite Database Error**
- Ensure `data` directory exists in `backend`
- Check file permissions
- Delete `data/skillgraph.db` and restart to recreate

### Frontend Issues

**npm install fails**
```bash
# Clear npm cache
npm cache clean --force
# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json
# Reinstall
npm install
```

**Port 5173 already in use**
```bash
# Kill process using port 5173
# Windows: netstat -ano | findstr :5173
# macOS/Linux: lsof -ti:5173 | xargs kill -9
# Or change port in vite.config.js
```

**API requests fail (CORS error)**
- Verify backend is running on port 8000
- Check browser console for error details
- Ensure CORS middleware is enabled in backend

### LLM Issues

**Ollama not responding**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama service
# macOS/Linux: ollama serve
# Windows: Restart Ollama application
```

**Gemini API quota exceeded**
- Check API usage at https://aistudio.google.com
- Wait for quota reset (daily limit)
- Consider upgrading to paid tier

**Lesson generation fails**
- Check LLM_PROVIDER in `.env`
- Verify API keys are correct
- Check backend logs for detailed error messages
- Ensure at least one LLM provider is configured

### Graph Visualization Issues

**Graph not rendering**
- Check browser console for JavaScript errors
- Verify D3.js is loaded: check Network tab
- Ensure student has taken a quiz (graph needs data)
- Try refreshing the page

**Nodes not colored correctly**
- Verify quiz results are stored in database
- Check API response from `/api/v1/graph/{student_id}`
- Ensure concept scores are calculated

## Production Deployment

### Backend

```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
# Build for production
npm run build

# Preview production build
npm run preview

# Serve with static file server
npx serve -s dist -p 5173
```

### Environment Variables for Production

```env
# Use production Neo4j instance
NEO4J_URI=neo4j+s://production-instance.databases.neo4j.io

# Use Gemini for production (more reliable)
LLM_PROVIDER=gemini
GEMINI_API_KEY=production-api-key

# Disable debug mode
DEBUG=false
```

## Next Steps

After successful setup:

1. Explore the demo profiles to understand the system
2. Take quizzes on different subjects
3. Review the generated remediation plans
4. Experiment with the knowledge graph visualization
5. Try the exam triage feature
6. Review the API documentation at http://localhost:8000/docs
7. Check the agent activity logs to understand A2A protocol

For additional help, refer to the main [README.md](README.md) or open an issue on GitHub.
