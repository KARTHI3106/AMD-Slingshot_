# SkillGraph

AI-powered diagnostic learning platform that identifies and fixes prerequisite knowledge gaps using graph-based root cause analysis.

## Overview

SkillGraph helps engineering students identify the root causes of their learning gaps by tracing prerequisite chains through a knowledge graph. Instead of showing "you got this wrong," the platform pinpoints exactly which foundational concepts are missing and generates personalized remediation plans.

## Key Features

- Diagnostic quiz system with 10 questions per subject
- Neo4j graph traversal to trace prerequisite chains up to 5 levels deep
- 4 cognitive error type classification (procedural, conceptual, transfer, prerequisite absence)
- Three LangGraph agents coordinating via A2A protocol
- Personalized remediation plans with day-by-day schedules
- AI-generated micro-lessons in English and Hindi
- Exam triage planner with ROI-based topic prioritization
- Memory decay tracking with forgetting curve calculations
- Interactive D3.js knowledge graph visualization

## Technology Stack

**Backend:**
- FastAPI 0.115.6 with Python 3.11
- LangGraph 0.2.60 for multi-agent orchestration
- Neo4j 5.27.0 graph database
- SQLite with aiosqlite 0.20.0
- Ollama with Llama 3.2 8B (primary LLM)
- Google Gemini 3.1 Pro (fallback LLM)

**Frontend:**
- React 18.3.1 with Vite 6.0.3
- D3.js 7.9.0 for graph visualization
- React Router DOM 6.28.0
- Motion 12.34.3 for animations

**Data:**
- 50+ concept nodes with 120+ prerequisite edges
- Quiz question bank with multiple subjects
- Student profiles and progress tracking

## Getting Started

See [SETUP.md](SETUP.md) for detailed installation and configuration instructions.

### Quick Start

**Prerequisites:**
- Python 3.11 or higher
- Node.js 18 or higher
- Neo4j Aura account (free tier available)
- Google Gemini API key (optional, for fallback LLM)

**Backend:**
```bash
cd backend
cp .env.example .env
# Edit .env with your credentials
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Access the application at http://localhost:5173

## API Documentation

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/health | Health check and agent status |
| GET | /api/v1/quiz/{subject} | Generate diagnostic quiz |
| POST | /api/v1/quiz/submit | Submit quiz and get results |
| GET | /api/v1/graph/{student_id} | Get knowledge graph data |
| POST | /api/v1/remediate | Generate remediation plan |
| POST | /api/v1/triage | Generate exam triage plan |
| GET | /api/v1/agents/activity | View A2A agent activity log |

### Demo Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/demo/profiles | List available demo profiles |
| POST | /api/v1/demo/activate | Activate a demo profile |

Full API documentation available at http://localhost:8000/docs when the backend is running.

## Project Structure

```
skillgraph/
├── backend/
│   ├── agents/              # LangGraph agent implementations
│   │   ├── diagnostic_agent.py
│   │   ├── pathway_agent.py
│   │   ├── content_agent.py
│   │   └── agent_registry.py
│   ├── data/                # Static data files
│   │   ├── concepts.json
│   │   ├── quiz_questions.json
│   │   ├── syllabus.json
│   │   └── skillgraph.db
│   ├── models/              # Pydantic data models
│   ├── routers/             # FastAPI route handlers
│   ├── services/            # Business logic services
│   ├── config.py            # Configuration management
│   ├── main.py              # FastAPI application entry
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── utils/           # Utility functions
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Usage

### Demo Mode

1. Click the "Demo Mode" toggle in the header
2. Select a demo profile (e.g., "Priya Sharma")
3. Navigate to "Knowledge Graph" to see existing gaps
4. Take a quiz to see the diagnostic process
5. View the generated remediation plan

### Taking a Quiz

1. Navigate to "Find My Gaps"
2. Select a subject (e.g., Machine Learning)
3. Answer 10 multiple-choice questions
4. View your concept scores and identified gaps
5. See root cause analysis with prerequisite chains

### Viewing the Knowledge Graph

1. Navigate to "See My Learning Map"
2. Interact with the force-directed graph
3. Color-coded nodes show your status:
   - Red: Gaps (score below 60%)
   - Red with glow: Root causes
   - Green: Mastered (score above 80%)
   - Amber: At-risk (retention below 70%)
   - Gray: Unassessed
4. Use search to find specific concepts
5. Filter by semester

### Getting a Remediation Plan

1. After taking a quiz, navigate to "Remediation"
2. View day-by-day study schedule
3. Concepts are ordered by prerequisite depth
4. Expand each day to see micro-lessons
5. Each lesson includes:
   - Summary of the concept
   - Where you went wrong
   - Correct understanding
   - Real-world analogy
   - Practice question

### Exam Triage

1. Navigate to "Prioritize for Exams"
2. Enter exam date and available study hours per day
3. System calculates ROI for each gap
4. View optimized study schedule
5. See which topics to skip if time is limited

## Configuration

### Environment Variables

Create a `.env` file in the `backend` directory:

```env
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password
GEMINI_API_KEY=your-api-key
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
GEMINI_MODEL=gemini-3.1-pro
SQLITE_DB_PATH=data/skillgraph.db
```

### LLM Configuration

The system supports two LLM providers:

**Ollama (Primary):**
- Self-hosted, free, and private
- Uses Llama 3.2 8B model
- Requires Ollama installation
- Automatically falls back to Gemini if unavailable

**Gemini (Fallback):**
- Cloud-based Google API
- Requires API key
- Used when Ollama is not available
- Free tier available

## Development

### Running Tests

```bash
cd backend
pytest
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

### Building for Production

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run build
npm run preview
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

## Acknowledgments

- Neo4j for graph database technology
- LangGraph for multi-agent orchestration
- Ollama for local LLM inference
- D3.js for graph visualization
