from lista_enlazada import ListaEnlazada
def menu_cola():
    cola_impresion = ListaEnlazada()
    while True:
        print("\n--- Sistema de Gestión de Cola de Impresión ---")
        print("1. Añadir trabajo a la cola")
        print("2. Procesar el siguiente trabajo")
        print("3. Mostrar cola de impresión")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            trabajo = input("Ingrese el nombre del trabajo: ")
            cola_impresion.agregar(trabajo)
            print(f"Trabajo '{trabajo}' añadido a la cola.")
        elif opcion == "2":
            if cola_impresion.cabeza:
                print(f"Procesando trabajo: {cola_impresion.cabeza.valor}")
                cola_impresion.eliminar(cola_impresion.cabeza.valor)
            else:
                print("La cola de impresión está vacía.")
        elif opcion == "3":
            print("\nCola de impresión actual:")
            cola_impresion.mostrar()
        elif opcion == "4":
            print("Saliendo del sistema de cola de impresión. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_cola()