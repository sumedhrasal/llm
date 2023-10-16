from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from myopenai import get_chat_model
import os
import json


grader_template = """
You need to act as a Grader. You will be provided with a question: {question}.
Your task is to evaluate the student's answer by going through the rubric params {rubric_params} 
and provide the total score.
Please provide detailed justification of your evaluation by using the rubric params.
"""

answer_template = """
Student name: {name}, answer: {answer}
"""


def get_rubrics_from_file():
    parent_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "rubrics_template"))

    # Specify the JSON file path within the parent folder
    json_file_path = os.path.join(parent_folder_path, "file1.json")

    # Read the JSON file
    data = None
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data


def perform_evaluation(
        student_name, question, rubric_params, answer, 
        question_params=None, template_answer=None):
    grader_prompt = SystemMessagePromptTemplate.from_template(
        grader_template, input_variables = ["question", "rubric_params"])
    answer_prompt = HumanMessagePromptTemplate.from_template(
        answer_template, input_variables = ["student_name", "answer"])

    chat_prompt = ChatPromptTemplate.from_messages(
        [grader_prompt, answer_prompt]
    )
    chain = LLMChain(llm=get_chat_model(), prompt=chat_prompt)

    return chain.run(question=question, name=student_name, answer=answer, rubric_params=rubric_params)

