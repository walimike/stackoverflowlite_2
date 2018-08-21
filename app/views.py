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
    pass


# This is to post/add a question
@app.route('/stackoverlow/api/v1/questions', methods=['POST'])
def ask_question():
    # {"question": text}
    asked_question = request.get_json()
    first_question = questions[0]
    if valid_question(asked_question) and first_question['question'] == '':
        new_question = {'qn_id': 1, 'question': asked_question["question"]}
        questions[0] = new_question
        response = jsonify({'questions': questions})
    elif valid_question(asked_question) and first_question['question']:
        new_question = {'qn_id': (len(questions) + 1), 'question': asked_question["question"]}
        questions.append(new_question)
        response = jsonify({'questions': questions})
    else:
        response = custom_response(400, 'Bad Request', "Request must contain 'question' data")
    return response


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