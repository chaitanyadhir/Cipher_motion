import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
from typing import Tuple

load_dotenv()
openai.api_key = "your_api_key"
app = FastAPI(title="AI-Powered Code Analyzer (OpenAI Version)")


class CodeSnippet(BaseModel):
    code: str

class AnalysisResult(BaseModel):
    bottlenecks: str
    suggestions: str

@app.post("/analyze", response_model=AnalysisResult)
def analyze_code(snippet: CodeSnippet) -> AnalysisResult:
    try:
        prompt = (
            "You are a Python expert specializing in performance optimization. "
            "Analyze the following Python code snippet. Identify potential performance bottlenecks, "
            "such as high time complexity, nested loops, or unnecessary computations. "
            "Provide actionable suggestions to optimize the code and explain your reasoning in detail.\n\n"
            f"```python\n{snippet.code}\n```"
        )

        response = openai.Completion.create(
    engine="gpt-3.5-turbo", 
    prompt=prompt,
    max_tokens=512,
    temperature=0.7,
    n=1,
    stop=None  
)


        analysis = response["choices"][0]["message"]["content"]
        
        bottlenecks, suggestions = parse_analysis(analysis)

        return AnalysisResult(bottlenecks=bottlenecks, suggestions=suggestions)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

def parse_analysis(analysis: str) -> Tuple[str, str]:
    bottlenecks = "Not identified."
    suggestions = "No suggestions."

    try:
        if "Potential Bottlenecks:" in analysis:
            bottlenecks = analysis.split("Potential Bottlenecks:")[1].split("Optimization Suggestions:")[0].strip()
        if "Optimization Suggestions:" in analysis:
            suggestions = analysis.split("Optimization Suggestions:")[1].strip()
    except Exception as e:
        print(f"Error parsing analysis: {e}")

    return bottlenecks, suggestions
