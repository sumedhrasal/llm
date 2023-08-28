from flask import Flask, request, jsonify
from grader import perform_evaluation

import logging


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/api/grade', methods=['POST'])
def grade_answer():
    data = request.json
    if data.get('question') is None or data.get('rubric_params') is None or data.get('answer') is None:
        logging.info(data)
        return jsonify({"error": "Invalid input request", "details": "question, rubric_params and answer are mandatory"}), 400

    output = perform_evaluation("John", data['question'], data['rubric_params'], data['answer'])
    result = {"message": "Evaluation complete", "data": output}
    
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port="8081")
