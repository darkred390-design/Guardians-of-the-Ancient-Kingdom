
from abc import ABC, abstractmethod


class Personaje(ABC):

    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if type(valor) is not int or not 0 <= valor <= 100:
            raise ValueError("La vida debe ser un entero entre 0 y 100.")
        self.__vida = valor

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, valor):
        if type(valor) is not int or valor <= 0:
            raise ValueError("El ataque debe ser un entero positivo.")
        self.__ataque = valor

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, valor):
        if type(valor) is not int or valor < 0:
            raise ValueError("La defensa debe ser un entero no negativo.")
        self.__defensa = valor

    def recibir_danio(self, cantidad):
        if type(cantidad) is not int or cantidad < 0:
            raise ValueError("El daño debe ser un entero no negativo.")

        danio_real = min(cantidad, self.__vida)
        self.__vida -= danio_real
        return danio_real

    def esta_vivo(self):
        return self.__vida > 0

    def mostrar_estado(self):
        print(
            f"{self.__nombre} | "
            f"Vida: {self.__vida} | "
            f"Ataque: {self.__ataque} | "
            f"Defensa: {self.__defensa}"
        )

    @abstractmethod
    def atacar(self, objetivo):
        pass


class Guerrero(Personaje):

    def atacar(self, objetivo):
        validar_ataque(self, objetivo)

        danio = max(0, int(self.ataque * 1.20) - objetivo.defensa)
        return objetivo.recibir_danio(danio)


class Mago(Personaje):

    def atacar(self, objetivo):
        validar_ataque(self, objetivo)

        danio = self.ataque
        return objetivo.recibir_danio(danio)


class Arquero(Personaje):

    def atacar(self, objetivo):
        validar_ataque(self, objetivo)

        if self.ataque > objetivo.defensa:
            danio_base = self.ataque - objetivo.defensa
            danio = danio_base * 2
        else:
            danio = 0

        return objetivo.recibir_danio(danio)


def validar_ataque(atacante, objetivo):
    if not atacante.esta_vivo():
        raise ValueError("Un personaje derrotado no puede atacar.")

    if not isinstance(objetivo, Personaje):
        raise TypeError("El objetivo debe ser un personaje válido.")

    if not objetivo.esta_vivo():
        raise ValueError("No se puede atacar a un personaje derrotado.")


class Combate:

    def __init__(self, personaje1, personaje2):
        if not isinstance(personaje1, Personaje):
            raise TypeError("El primer participante debe ser un personaje.")

        if not isinstance(personaje2, Personaje):
            raise TypeError("El segundo participante debe ser un personaje.")

        if personaje1 is personaje2:
            raise ValueError("Los participantes deben ser diferentes.")

        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.turno_actual = personaje1
        self.rondas = 0
        self.ganador = None
        self.empate = False

    def cambiar_turno(self):
        if self.turno_actual is self.personaje1:
            self.turno_actual = self.personaje2
        else:
            self.turno_actual = self.personaje1

    def verificar_ganador(self):
        vivo1 = self.personaje1.esta_vivo()
        vivo2 = self.personaje2.esta_vivo()

        if vivo1 and not vivo2:
            self.ganador = self.personaje1
        elif vivo2 and not vivo1:
            self.ganador = self.personaje2
        else:
            self.ganador = None

        return self.ganador

    def mostrar_resultado(self):
        print("\n=== RESULTADO DEL COMBATE ===")

        if self.ganador is not None:
            print(f"¡El ganador es {self.ganador.nombre}!")
        else:
            print("El combate terminó en empate.")

        print("\nEstado final:")
        self.personaje1.mostrar_estado()
        self.personaje2.mostrar_estado()

    def iniciar(self):
        print("\n=== COMIENZA EL COMBATE ===")

        if not self.personaje1.esta_vivo() and not self.personaje2.esta_vivo():
            self.empate = True
            self.mostrar_resultado()
            return None

        if not self.personaje1.esta_vivo() or not self.personaje2.esta_vivo():
            self.verificar_ganador()
            self.mostrar_resultado()
            return self.ganador

        while self.rondas < 50:
            self.rondas += 1
            print(f"\n--- Ronda {self.rondas} ---")

            danio_ronda = 0

            for _ in range(2):
                atacante = self.turno_actual

                objetivo = (
                    self.personaje2
                    if atacante is self.personaje1
                    else self.personaje1
                )

                if atacante.esta_vivo() and objetivo.esta_vivo():
                    danio = atacante.atacar(objetivo)
                    danio_ronda += danio

                    print(
                        f"{atacante.nombre} ataca a {objetivo.nombre} "
                        f"y causa {danio} de daño."
                    )

                    self.personaje1.mostrar_estado()
                    self.personaje2.mostrar_estado()

                ganador = self.verificar_ganador()

                if ganador is not None:
                    self.mostrar_resultado()
                    return ganador

                self.cambiar_turno()

            if danio_ronda == 0:
                self.empate = True
                print("Empate técnico: no se causó daño durante la ronda.")
                self.mostrar_resultado()
                return None

        self.empate = True
        print("Se alcanzó el límite de 50 rondas.")
        self.mostrar_resultado()
        return None
