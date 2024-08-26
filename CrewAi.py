from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task
from langchain_ollama import OllamaLLM
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama

load_dotenv()

#os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
#os.environ['OPENAI_MODEL_NAME']=os.getenv('OPENAI_MODEL_NAME')
#os.environ['OPENAI_API_BASE']=os.getenv('OPENAI_API_BASE')

#OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
#OPENAI_API_BASE=os.getenv("OPENAI_API_BASE")
#llm=ChatOllama(model='llama2',base_url=OPENAI_API_BASE)

os.environ["OPENAI_API_KEY"] = "NA"
llm = ChatOllama(
    model = "llama2",
    base_url = "http://localhost:11434")


Crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    llm=llm
)

## start the task execution process with enhanced feedback
result=Crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})

