import os
import google.generativeai as genai
from IPython.display import display, Markdown
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=gemini_api_key)

print("Gemini client successfully configured.")
print(gemini_api_key[:5])

# # Create model
# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content(
#     "Explain Agentic AI in one line."
# )

# display(Markdown(response.text))
