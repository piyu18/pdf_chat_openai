from dotenv import load_dotenv
import os
from langchain_community.embeddings import OpenAIEmbeddings
import openai

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
print(key)

embeddings = OpenAIEmbeddings(openai_api_key=key)