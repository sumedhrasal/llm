<h1 align="center">
LLM - Answer Grading
</h1>

This project is designed to grade answers given a question and its rubric parameters. 

## Features

- Input a question and an answer to grade using the provided rubric.
- Keep environment and package management organized using Conda environments.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/sumedhrasal/llm.git
cd llm
```

2. Install required packages:

```bash
conda env create -f environment.yml
```

3. After creating the environment, you can activate it:

```bash
conda activate llm_env
```

4. Set up your environment variables using a `.env` file:

```
OPENAI_API_KEY=your-openai-api-key
```

5. Run application

```bash
curl --location 'http://127.0.0.1:8081/api/grade' \
--header 'Content-Type: application/json' \
--data '{
    "question": "",
    "rubric_params": "",
    "answer": ""
    }'
```
