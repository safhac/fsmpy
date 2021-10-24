class Model:
    def __init__(self, filename):
        self._file: str = filename

    @property
    def file(self):
        return self._file
