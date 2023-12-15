from flask import Flask, request, jsonify, abort
from grader import perform_evaluation
from myopenai import does_api_key_exist
import json
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/api/grade', methods=['POST'])
def grade_answer():
    if not does_api_key_exist():
        abort(401, 'Unauthorized: Missing OPENAI_API_KEY in .env file')

    data = request.json
    if data.get('question') is None or data.get('rubric_params') is None or data.get('answer') is None:
        logging.info(data)
        return jsonify({"error": "Invalid input request", "details": "question, rubric_params and answer are mandatory"}), 400

    name = data['name'] if data.get('name') else 'John'
    output = perform_evaluation(name, data['question'], data['rubric_params'], data['answer'])
    result = {"response": json.loads(output)}

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port="8081")
