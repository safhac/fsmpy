from contextlib import AbstractContextManager


class Listen(AbstractContextManager):

    def __enter__(self):
        print(f'enter listen')
        return (self, None)
        print('listen complete')

    def __exit__(self, *exc):

        print(f'exit listen {exc=}')
        if not exc or ConnectionRefusedError in exc:
            print('in')
            return True
        return False

