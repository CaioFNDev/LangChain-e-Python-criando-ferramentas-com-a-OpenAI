from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_crianças = 2
atividade = "música"

prompt = f"Crie um roteiro de viagem de {numero_dias}, para uma família com {numero_crianças} crianças, que gosta de {atividade}"

cliente = OpenAI(api_key = api_key)

resposta = cliente.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "system",
            "content": "Você é um assistente de roteiros de viagens."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

resposta_em_texto = resposta.choices[0].message.content
print(resposta_em_texto)