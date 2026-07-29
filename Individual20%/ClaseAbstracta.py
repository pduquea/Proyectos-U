from abc import ABC, abstractmethod
from math import gcd


class Numerica(ABC):
    """Clase abstracta base para representar operaciones numéricas."""

    @abstractmethod
    def to_string(self) -> str:
        """Convierte el número a texto."""
        pass

    @abstractmethod
    def equals(self, other) -> bool:
        """Compara este objeto con otro."""
        pass

    @abstractmethod
    def sumar(self, numero: "Numerica") -> "Numerica":
        """Retorna la suma de este número y otro."""
        pass

    @abstractmethod
    def restar(self, numero: "Numerica") -> "Numerica":
        """Retorna la resta de este número y otro."""
        pass

    @abstractmethod
    def multiplicar(self, numero: "Numerica") -> "Numerica":
        """Retorna la multiplicación de este número y otro."""
        pass

    @abstractmethod
    def dividir(self, numero: "Numerica") -> "Numerica":
        """Retorna la división de este número y otro."""
        pass


class Fraccion(Numerica):
    """Representa un número fraccionario con numerador y denominador."""

    def __init__(self, numerador: int, denominador: int = 1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")

        if denominador < 0:
            numerador = -numerador
            denominador = -denominador

        divisor_comun = gcd(abs(numerador), abs(denominador))
        self.numerador = numerador // divisor_comun
        self.denominador = denominador // divisor_comun

    def to_string(self) -> str:
        return f"{self.numerador}/{self.denominador}"

    def __str__(self) -> str:
        return self.to_string()

    def equals(self, other) -> bool:
        if not isinstance(other, Numerica):
            return False
        return isinstance(other, Fraccion) and self.numerador == other.numerador and self.denominador == other.denominador

    def sumar(self, numero: Numerica) -> Numerica:
        if not isinstance(numero, Fraccion):
            raise TypeError("Solo se pueden sumar fracciones")

        nuevo_numerador = self.numerador * numero.denominador + self.denominador * numero.numerador
        nuevo_denominador = self.denominador * numero.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def restar(self, numero: Numerica) -> Numerica:
        if not isinstance(numero, Fraccion):
            raise TypeError("Solo se pueden restar fracciones")

        nuevo_numerador = self.numerador * numero.denominador - self.denominador * numero.numerador
        nuevo_denominador = self.denominador * numero.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def multiplicar(self, numero: Numerica) -> Numerica:
        if not isinstance(numero, Fraccion):
            raise TypeError("Solo se pueden multiplicar fracciones")

        return Fraccion(self.numerador * numero.numerador, self.denominador * numero.denominador)

    def dividir(self, numero: Numerica) -> Numerica:
        if not isinstance(numero, Fraccion):
            raise TypeError("Solo se pueden dividir fracciones")
        if numero.numerador == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")

        return Fraccion(self.numerador * numero.denominador, self.denominador * numero.numerador)


if __name__ == "__main__":
    a = Fraccion(1, 2)
    b = Fraccion(3, 4)

    print("a =", a.to_string())
    print("b =", b.to_string())
    print("igualdad:", a.equals(b))
    print("suma:", a.sumar(b))
    print("resta:", a.restar(b))
    print("multiplicación:", a.multiplicar(b))
    print("división:", a.dividir(b))
