import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

client = OpenAI()

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

# Usar a chave API carregada do arquivo de ambiente
llm = ChatOpenAI(api_key=openai_api_key, model='gpt-3.5-turbo')

model = ChatOpenAI(model="gpt-3.5-turbo")
result = model.invoke("oi, vc está ai?")
print(result)