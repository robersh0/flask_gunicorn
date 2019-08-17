from src.config.general import ERRORS


class GunicornFlaskBaseException(Exception):
    def __init__(self, tag=None, trace=None):
        self.tag = tag
        self.trace = trace

        if self.tag in ERRORS:
            self.__set_properties(ERRORS[tag])
        else:
            self.__set_properties(ERRORS['INTERNAL_ERROR'])

    def __set_properties(self, error):
        if not hasattr(self, 'message') or self.message is None:
            self.message = error['message']
        self.code = error['code']
        self.internal_code = error['internal_code']

    @property
    def serialize(self):
        return {
            'code': self.code,
            'tag': self.tag,
            'message': self.message
        }
