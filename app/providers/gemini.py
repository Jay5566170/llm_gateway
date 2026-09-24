import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)



model = genai.GenerativeModel("gemini-3.6-flash")

def generate_with_gemini(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text


    except Exception as e:

        print("Gemini Error:", e)

        return "Gemini service failed"