from flask import request, json, jsonify
from flask_restful import Resource

from app.models import Text
from app.controllers import TextController


class ReadBook(Resource):
    def get(self):
        control = TextController(Text)
        query = control.get_text()
        print(query)
        return jsonify(query or {'message': 'Book is empty'})


class ReadText(Resource):
    def get(self, title):
        control = TextController(Text)
        query = control.get_text(title=title)
        print('\n'*20)
        print(query)
        print('\n'*20)
        return jsonify(query or {'message': 'Title is not exist'})       


class WriteText(Resource):
    def post(self):
        data = json.loads(request.data)
        control = TextController(Text)
        check_exist = control.is_not_exist(data)

        if 'error' in check_exist:
            return jsonify(error=check_exist[0], message=check_exist[1])

        if 'success' in check_exist:
            check_added = control.add_to_db(data)
            if 'error' in check_added:
                print(check_added)
                print('\n'*20)
                return jsonify(error=check_added[0], message=check_added[1])
            else:
                jsonify(message='Text was add')
        else:
            return jsonify(message='Text is already exist')

class ReadSound(Resource):
    pass
