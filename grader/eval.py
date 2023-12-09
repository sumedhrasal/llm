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
You need to act as a Grader. You will be provided with a question: {question}. Your task is to 
evaluate the student's answer by going through the rubric params {rubric_params} and provide the total score.
Whenever a student doesn't achieve a perfect score for a specific section, kindly provide a 
list of opportunities for improving the response, including any grammar and spelling errors.
In cases where the student's answer does earn a perfect score, a simple confirmation suffices; 
no additional details are necessary.

Your response structure should be as follows:
- Student's name: {name}
- Total marks:
- Evaluation justification: 
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
        name, question, rubric_params, answer, 
        question_params=None, template_answer=None):
    grader_prompt = SystemMessagePromptTemplate.from_template(
        grader_template, input_variables = ["question", "rubric_params", "name"])
    answer_prompt = HumanMessagePromptTemplate.from_template(
        answer_template, input_variables = ["name", "answer"])

    chat_prompt = ChatPromptTemplate.from_messages(
        [grader_prompt, answer_prompt]
    )
    chain = LLMChain(llm=get_chat_model(), prompt=chat_prompt)

    return chain.run(question=question, name=name, answer=answer, rubric_params=rubric_params)

