from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
import os


os.environ["OPENAI_API_KEY"] = ''

def get_embeddings():
    return OpenAIEmbeddings(model='text-embedding-ada-002')


def get_model():
    return OpenAI(model_name='text-ada-001')


def get_chat_model():
    return ChatOpenAI()

