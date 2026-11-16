
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load environment variables
load_dotenv()

# Check LangSmith tracing configuration
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompts = [
    "What is artificial intelligence? Explain briefly.",
    "Explain how RAG works in LangChain.",
    "Explain the complete architecture of a RAG application with examples."
]

for i, prompt in enumerate(prompts, start=1):
    print(f"\n--- Run {i} ---")
    response = llm.invoke(prompt)
    print("Answer:", response.content)
