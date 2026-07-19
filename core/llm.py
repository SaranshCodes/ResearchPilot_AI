from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv('GOOGLE_API_KEY')
)

def ask_gemini(question, context):
    prompt = f'''
    You are a research paper assistant. Answer only using the provided context chunks.
If the answer isn't in the context, say so clearly. Always mention which section of the paper your answer comes from.
    
    Research paper context:
    {context}
    
    Question:
    {question}
    '''
    response =client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt)
    return response.text

# Gemini chatbot