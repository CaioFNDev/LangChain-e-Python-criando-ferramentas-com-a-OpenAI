from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_crianças = 2
atividade = "praia"

modelo_de_prompt = PromptTemplate(
    template= """
    Crie um roteiro de viagem de {dias} dias,
    para uma família com {numero_crianças} crianças,
    que gostam de {atividade}
    """
) # type: ignore

prompt = modelo_de_prompt.format(
    dias = numero_dias,
    numero_crianças = numero_crianças,
    atividade = atividade
)

print("Prompt : \n", prompt)

modelo = ChatOpenAI(
    model= "gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key # type: ignore
)

resposta = modelo.invoke(prompt)
print(resposta.content)