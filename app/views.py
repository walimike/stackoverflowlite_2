from flask import jsonify, request, make_response
from app.data import questions, answers
from app import create_app

app = create_app (config_name='development')


# This code fetches all questions
@app.route('/stackoverlow/api/v1/questions', methods=['GET'])
def get_all_questions():
    pass


# This code fetches specific question
@app.route('/stackoverlow/api/v1/questions/<int:qn_id>', methods=['GET'])
def get_one_question(qn_id):
    for one_question in questions:
        if one_question['qn_id'] == qn_id:
            return jsonify({'question': one_question})


# This is to post/add a question
@app.route('/stackoverlow/api/v1/questions', methods=['POST'])
def ask_question():
    # {"question": text}
    pass


# This is to add an answer
@app.route('/stackoverlow/api/v1/questions/<int:qn_id>/answer', methods={'POST'})
def answer_to_question(qn_id):
    pass


def valid_question(question_received):
    if question_received and isinstance(question_received, dict) and 'question' in question_received:
        return True
    return False


def valid_answer(answer_received):
    if answer_received and isinstance(answer_received, dict) and 'answer' in answer_received:
        return True
    return False


def custom_response(status_code, status_message, friendly_message):
    response = make_response(
        jsonify({'status_code': str(status_code) + ': ' + status_message + ', ' + friendly_message}),
        status_code)
    response.headers['Status-Code'] = str(status_code) + ': ' + status_message + ', ' + friendly_message
    return response