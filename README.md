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

2. Set up your environment variables using a `.env` file:

```
OPENAI_API_KEY=your-openai-api-key
```

3. Build the docker image.

```bash
docker build -t llm_eval .
```

4. Run the docker image.

```bash
docker run --rm -p 8081:8081 llm_eval
```

5. Invoke application

```bash
curl --location 'http://0.0.0.0:8081/api/grade' \
--header 'Content-Type: application/json' \
--data '{
    "question": "",
    "rubric_params": "",
    "answer": "",
    "name": ""
    }'
```
