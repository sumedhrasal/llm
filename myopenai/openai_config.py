from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import boto3


# Load environment variables from .env file
load_dotenv()


def set_key():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    environment = os.environ.get('FLASK_ENV', 'dev')
    aws_parameter_store = os.environ.get('PARAMETER_STORE')
    if environment == "dev":
        return openai_api_key
    else:
        ssm = boto3.client('ssm', region_name='us-east-1')
        response = ssm.get_parameter(Name=aws_parameter_store, WithDecryption=True)
        return response['Parameter']['Value']


key = set_key()


def does_api_key_exist():
    return key and key != ''


def get_embeddings():
    return OpenAIEmbeddings(model='text-embedding-ada-002', openai_api_key=key)


def get_model():
    return OpenAI(model_name='text-ada-001', openai_api_key=key, temperature=0.0)


def get_chat_model():
    return ChatOpenAI(openai_api_key=key, temperature=0.0)
