from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Request body schema
class StoryRequest(BaseModel):
    user_input: str
    story_context: str

# Story generation route
@app.post("/generate-story/")
async def generate_story(request: StoryRequest):
    try:
        # Use OpenAI API to generate story continuation
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative storyteller for interactive adventures."},
                {"role": "user", "content": f"Context: {request.story_context} \nUser choice: {request.user_input}"}
            ]
        )
        story = response.choices[0].message.content
        return {"story": story}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Story generation failed: {str(e)}")

# Run the server using `uvicorn main:app --reload`
