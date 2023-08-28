import myopenai
import streamlit as st 

from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


grader_template = """
You need to act as a Grader. A student {name} will submit an essay on any {topic} of his or her choosing. 
You need to use the following rubric to review the essay & award marks out of 10. 
The topic and the essay have to match or else you can simply award  0 points to the student & ignore the rubric details.

Your task is to evaluate the student's essay, go through the rubrics & award appropriate points. 
Please provide detailed justification of your evaluation by using the rubric levels.

Evaluate student answer:
"""

answer_template = """
Name: {name}, Topic: {topic}.
Answer: {answer}
"""


def grader_run():
    with st.form(key='grader_form'):
        st.title('Grading App')
        name = st.text_input('Student Name')
        topic = st.text_input('Topic')
        answer = st.text_area('Answer')
        submit_button = st.form_submit_button(label='Submit')

        grader_prompt = SystemMessagePromptTemplate.from_template(
            grader_template, input_variables = ["topic", "name", "answer"])
        answer_prompt = HumanMessagePromptTemplate.from_template(
            answer_template, input_variables = ["topic", "name", "answer"])

        chat_prompt = ChatPromptTemplate.from_messages(
            [grader_prompt, answer_prompt]
        )
        chain = LLMChain(llm=myopenai.get_chat_model(), prompt=chat_prompt)

        if submit_button:
            grades = chain.run(topic=topic, name=name, answer=answer)
            # grades = chain.run({"topic": topic, "name": name, "answer": answer})

            st.write(grades) 
            # st.write(script) 

            # with st.expander('Grading History'): 
                # st.info(essay_memory.buffer)
