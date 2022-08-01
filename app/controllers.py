from app import db


class ErrorHandler:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwds):
        try:
            return self.func(*args, **kwds)
        except Exception as e:
            return 'error', e


class Controller:
    def __init__(self, obj):
        self.obj = obj
    
    @ErrorHandler
    def is_not_exist(self, data):
        query_text = self.obj.query.filter_by(title=data['title']).one_or_none()
        return 'success', query_text
    
    @ErrorHandler
    def _get_content_one(self, title):
        query_result = self.obj.query.filter_by(title=title).one_or_none()
        result_dict = {'title': query_result.title, 'data': query_result.data}
        return result_dict

    @ErrorHandler
    def _get_content_many(self):
        query_result = self.obj.query.all()
        result_dict = [{'title': q.title, 'data': q.data} for q in query_result]
        return result_dict
    
    @ErrorHandler
    def add_to_db(self, data):
        try:
            text = self.obj(title=data['title'], data=data['text'])
            db.session.add(text)
            db.session.commit()
        except Exception as e:
            return e


class SoundController:
    pass


class TextController(Controller):
    def get_text(self, title=None):
        if title:
            print('\n'*20)
            content = self._get_content_one(title)
        else:
            content = self._get_content_many()
        return content
