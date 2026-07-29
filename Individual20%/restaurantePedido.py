from typing import overload


class ItemMenu:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor


class Pedido:
    @overload
    def calcular_valor(self, primer_plato: ItemMenu, bebida: ItemMenu) -> float:
        ...

    @overload
    def calcular_valor(self, primer_plato: ItemMenu, segundo_plato: ItemMenu, bebida: ItemMenu) -> float:
        ...

    @overload
    def calcular_valor(self, primer_plato: ItemMenu, segundo_plato: ItemMenu, bebida: ItemMenu, postre: ItemMenu) -> float:
        ...

    def calcular_valor(self, *args):
        if len(args) == 2:
            primer_plato, bebida = args
            return primer_plato.valor + bebida.valor
        elif len(args) == 3:
            primer_plato, segundo_plato, bebida = args
            return primer_plato.valor + segundo_plato.valor + bebida.valor
        elif len(args) == 4:
            primer_plato, segundo_plato, bebida, postre = args
            return primer_plato.valor + segundo_plato.valor + bebida.valor + postre.valor
        else:
            raise ValueError("La cantidad de elementos del pedido no es válida")


def mostrar_pedido(texto, total):
    print(texto)
    print(f"El costo de {texto.split('El costo de ')[1]} es = ${total}")


def main():
    primer_plato_1 = ItemMenu("Sancocho", 4000)
    bebida_1 = ItemMenu("Gaseosa", 3000)

    primer_plato_2 = ItemMenu("Crema de verduras", 5000)
    segundo_plato_2 = ItemMenu("Churrasco", 6500)
    bebida_2 = ItemMenu("Gaseosa", 1500)

    primer_plato_3 = ItemMenu("Crema de espinacas", 6000)
    segundo_plato_3 = ItemMenu("Salmón", 9000)
    bebida_3 = ItemMenu("Gaseosa", 2000)
    postre_3 = ItemMenu("Tiramisú", 5000)

    pedido = Pedido()

    total_1 = pedido.calcular_valor(primer_plato_1, bebida_1)
    print(f"El costo de {primer_plato_1.nombre} y {bebida_1.nombre} es = ${total_1}")

    total_2 = pedido.calcular_valor(primer_plato_2, segundo_plato_2, bebida_2)
    print(f"El costo de {primer_plato_2.nombre} + {segundo_plato_2.nombre} + {bebida_2.nombre} es = ${total_2}")

    total_3 = pedido.calcular_valor(primer_plato_3, segundo_plato_3, bebida_3, postre_3)
    print(f"El costo de {primer_plato_3.nombre} + {segundo_plato_3.nombre} + {bebida_3.nombre} + {postre_3.nombre} es = ${total_3}")


if __name__ == "__main__":
    main()
