from google import genai
import os
from dotenv import load_dotenv
import json
import re


# Store Your API Key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

def analyze_job_requirements(requirements_text, experience):

    """
    Use Gemini API to analyze job requirements and extract:
    - Skills required
    """
    # print(requirements_text)
       
    prompt = f"""
    You are an intelligent job analysis assistant.

    Your task is to extract key information from the given job posting text and output it as JSON. 
    You must include the following fields:
    1. Tools: List of tools or software explicitly mentioned
    2. Technical skills: List of data, programming, or analytical skills, each technical skills should have maximum 2 words, maximum 5 technical skills 
    3. Other skills: list of other skills such as management ot administrative skills, each skill should have maximum 2 words, maximum 3 other skills
    4. Job level: categorize the job as Entry Level, Intermediate,  or Expert depending on primarily on the years of experience  and then skills sets required
       so, if 5 years or more experience is needed, it will be expert
       if 3 years or more experience and a lot of skills are needed, it will be expert

    Requirements:
    Jon Posting -{requirements_text}
    Experience - {experience}
    
    Return output in JSON format:
    {{
        "tools": [...],
        "technical skills": [...],
        "other skills": [...],
        "job_level": ...
    }}

    Leave the field blank if no tool/ technical skill/ other skill is found
    Leave the job level blank if the years of experience is not given
    """
    response = ""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
 
    # Extract the JSON text
    raw_text = response.candidates[0].content.parts[0].text.strip()
    
    # Remove code fences if present
    clean_text = re.sub(r"^```json\s*|\s*```$", "", raw_text.strip())
    print(clean_text)
    # Try parsing
    try:
        return json.loads(clean_text)
    except json.JSONDecodeError as e:
        print("❌ Could not parse JSON:", e)
        return {}

   
