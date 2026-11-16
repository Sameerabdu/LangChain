
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Verify LangSmith configuration
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))

# Initialize OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Three different prompts
prompts = [
    "What is artificial intelligence? Explain briefly.",
    "Explain how RAG works in LangChain.",
    "Explain the complete architecture of a RAG application with examples."
]

# Execute prompts
for i, prompt in enumerate(prompts, start=1):
    print(f"\n--- Run {i} ---")
    response = llm.invoke(prompt)
    print("Prompt:", prompt)
    print("Answer:", response.content)
