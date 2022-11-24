class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def __call__(self, string):
        return self.is_valid(string)

    def is_valid(self, string):
        if not self.min_length <= len(string) <= self.max_length:
            raise ValueError('недопустимая строка')
        if self.chars:
            if set(string).isdisjoint(set(self.chars)):
                raise ValueError('недопустимая строка')

        return True


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        if 'login' not in request.keys() or 'password' not in request.keys():
            raise TypeError('в запросе отсутствует логин или пароль')

        if self.login_validator(request['login']):
            self._login = request['login']

        if self.password_validator(request['password']):
            self._password = request['password']


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)



