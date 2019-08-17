from src.tools.exceptions.base import GunicornFlaskBaseException


class PredictException(GunicornFlaskBaseException):
    def __init__(self, tag=None):
        self.tag = tag
        super().__init__(tag=tag)
