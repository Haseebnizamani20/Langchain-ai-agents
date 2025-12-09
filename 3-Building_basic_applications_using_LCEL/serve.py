from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()


groq_api_key=os.getenv("groq_api_key")


model= ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)

                

# prompt template


system_template="translate the following {language} : "

prompt_template =ChatPromptTemplate.from_messages(
    [("system",system_template),("user","{text}")]
    )

parser=StrOutputParser()
chain=prompt_template | model | parser

#APP DEFINITION

app=FastAPI(title="Langchain server",
            version="1.0",
            description="A simple API server using LANGCHAIN runnable interfaces")

add_routes(
    app,
    chain,
    path='/chain123'
)

if __name__=="__main__":
    # import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000) 