import os
import json
import yaml
from crewai import Agent, Task, Crew, LLM, Process
from dotenv import load_dotenv,find_dotenv
from os import environ as env
from typing import List
from pydantic import BaseModel, Field

import markdown
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv('config/.env')

print('GOOGLE_API_KEY:  {}'.format(env['GOOGLE_API_KEY']))

GEMINI_API_KEY = env['GOOGLE_API_KEY']

env["GEMINI_API_KEY"] = env['GOOGLE_API_KEY']
MODEL_NAME = "models/text-embedding-004"
env["SERPER_API_KEY"] = env['SERPER_KEY']

MODEL_NAME_LLM = "gemini/gemini-1.5-pro-latest"
MODEL_NAME_LLM = "gemini/gemini-2.0-flash-exp"

llm = LLM(
    model = MODEL_NAME_LLM,
    temperature = 0.7
)



# Define file paths for YAML configurations
files = {
    'agents': 'config/agents.yaml',
    'tasks': 'config/tasks.yaml'
}
