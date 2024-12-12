from lista_enlazada import ListaEnlazada
def menu():
    playlist = ListaEnlazada()
    while True:
        print("\n--- Sistema de Gestión de Playlists ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Buscar canción")
        print("4. Mostrar playlist")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la canción: ")
            playlist.agregar(nombre)
            print(f"Canción '{nombre}' agregada a la playlist.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la canción a eliminar: ")
            if playlist.eliminar(nombre):
                print(f"Canción '{nombre}' eliminada.")
            else:
                print(f"La canción '{nombre}' no se encontró en la playlist.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre de la canción a buscar: ")
            if playlist.buscar(nombre):
                print(f"La canción '{nombre}' está en la playlist.")
            else:
                print(f"La canción '{nombre}' no se encontró en la playlist.")
        elif opcion == "4":
            print("\nPlaylist actual:")
            playlist.mostrar()
        elif opcion == "5":
            print("Saliendo del sistema de playlists. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()