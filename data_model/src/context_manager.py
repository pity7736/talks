
class ContextManager:

    def __init__(self):
        self._closed = False

    @property
    def is_closed(self):
        return self._closed
