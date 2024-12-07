Cipher Motion
AI-powered tool for analyzing Python code and suggesting optimizations.

Features
- Detects bottlenecks like high complexity and inefficiencies.
- Provides actionable optimization suggestions.

Setup
1. Clone Repository: 
   git clone https://github.com/your-repo/cipher_motion.git
2. Create Virtual Environment:
   python -m venv venv
   .\\venv\\Scripts\\activate (Windows) OR source venv/bin/activate (Linux/Mac)
3. Install Requirements:
   pip install -r requirements.txt
4. Add API Key: 
   Create a .env file with:
   OPENAI_API_KEY=your_openai_api_key

Usage
- Start Backend: uvicorn backend:app --reload
- Run Frontend: python frontend.py
- Analyze Python code for bottlenecks and optimizations.

Requirements
- Python 3.8+
- Dependencies: fastapi, uvicorn, openai, python-dotenv, tkinter

Test Backend
curl -X POST http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d '{"code": "your_code_here"}'

