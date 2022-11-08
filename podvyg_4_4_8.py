class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def _verify_str_value(value):
        if not isinstance(value, str):
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def _verify_numb_value(value):
        if 0 >= value:
            raise TypeError('неверный тип аргумента')

    def __setattr__(self, key, value):
        if key == '_model':
            self._verify_str_value(value)
        if key in ('_mass', '_speed', '_top'):
            self._verify_numb_value(value)

        object.__setattr__(self, key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key == '_chairs':
            if not isinstance(value, int) or value <= 0:
                raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        if key == '_weapons':
            if not isinstance(value, dict):
                raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]