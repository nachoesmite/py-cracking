class Polinomial:
    def __init__(self, *coefficients):
        self.coefficients = coefficients
    def __repr__(self) -> str:
        return f'Polinomial(*{self.coefficients})'
    def __add__(self, other):
        return Polinomial(*(x + y for x, y in zip(self.coefficients, other.coefficients)))