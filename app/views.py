from flask import jsonify, request, make_response
from app.data import questions, answers
from app import create_app

app = create_app(config_name='development')


# This code fetches all questions
@app.route('/stackoverlow/api/v1/questions', methods=['GET'])
def get_all_questions():
    return jsonify({'questions': questions})


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
        response = make_response("Request must contain 'question' data", 404)
    return make_response(response, 201)


# This is to add an answer
@app.route('/stackoverlow/api/v1/questions/<int:qn_id>/answer', methods=['POST'])
def answer_to_question(qn_id):
    particular_question = answers[qn_id - 1]
    all_answers = particular_question['answer']
    first_answer = all_answers[0]
    given_answer = request.get_json()
    if valid_answer(given_answer) and first_answer['answer'] == '':
        new_answer = {'ans_id': 1, 'answer': given_answer["answer"]}
        all_answers[0] = new_answer
        response = jsonify({'answers': answers})
    elif valid_answer(given_answer) and first_answer['answer']:
        new_answer = {'ans_id': (len(all_answers) + 1), 'answer': given_answer["answer"]}
        all_answers.append(new_answer)
        response = jsonify({'answers': answers})
    else:
        response = make_response( "Request must contain 'answers' data", 404)
    return make_response(response, 201)


def valid_question(question_received):
    if question_received and isinstance(question_received, dict) and 'question' in question_received and not question_received.isspace():
        return True
    return False


def valid_answer(answer_received):
    if answer_received and isinstance(answer_received, dict) and 'answer' in answer_received and not answer_received.isspace():
        return True
    return False


