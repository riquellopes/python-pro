from functools import wraps

"""
    Create a decorator to control access of users.
"""

ROUTER = {}
ADMIN = 'ADMIN'
MANAGER = 'MANAGER'
_BD = {ADMIN: ['renzo', 'luis'], MANAGER: ['diego', 'henrique']}


def login(group):
    def decorator(function):
        @wraps(function)
        def decorated(usuario, *args, **kwargs):
            if usuario in _BD[group]:
                return function(usuario, *args, **kwargs)
            return 'Usuario {} nao pode acessar funcao {}'. \
                format(usuario, function.__name__)
        return decorated

    if isinstance(group, str):
        return decorator
    return login(ADMIN)(group)


def route(path):
    def wrap(function, *args, **kwargs):
        ROUTER[path] = function
        return function
    return wrap


@route("/")
@login
def home(usuario):
    print("Home")


if __name__ == "__main__":
    for path in "/".split(","):
        function = ROUTER[path]
        print(function.__closure__[0])
        function("henrique")
