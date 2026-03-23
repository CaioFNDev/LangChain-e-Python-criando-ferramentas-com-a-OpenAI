from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


modelo_cidade = PromptTemplate(
    template= """
    Sugira uma cidade dado meu interesse por {interesse}.
    """,
    input_variables=["interesse"]
) # type: ignore


modelo = ChatOpenAI(
    model= "gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key # type: ignore
)

cadeia = modelo_cidade | modelo | StrOutputParser()

resposta = cadeia.invoke(
                         {
                             "interesse": "praias"
                         })
print(resposta)