# ==========================================
# Sistema de Gestión de Préstamos Biblioteca
# ==========================================

# Variables iniciales
STOCK_MAXIMO = 120
stock_libros = STOCK_MAXIMO
prestamos_activos = 0

print("Bienvenido")
print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

# Ciclo principal del programa
while True:

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        # Opción 1: Mostrar libros disponibles
        if opcion == 1:
            print(f"\nLibros disponibles actualmente: {stock_libros}")

        # Opción 2: Realizar préstamo
        elif opcion == 2:

            try:
                cantidad = int(input("Ingrese cantidad de libros a prestar: "))

                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor a 0.")

                elif cantidad > stock_libros:
                    print("Error: No hay suficientes libros disponibles.")

                else:
                    stock_libros -= cantidad
                    prestamos_activos += cantidad

                    print("\nPréstamo realizado exitosamente.")
                    print(f"Libros prestados: {cantidad}")
                    print(f"Stock disponible: {stock_libros}")

            except ValueError:
                print("Error: Debe ingresar un número válido.")

        # Opción 3: Devolver préstamo
        elif opcion == 3:

            if prestamos_activos == 0:
                print("No existen préstamos registrados para devolver.")

            else:
                try:
                    cantidad = int(input("Ingrese cantidad de libros a devolver: "))

                    if cantidad <= 0:
                        print("Error: La cantidad debe ser mayor a 0.")

                    elif cantidad > prestamos_activos:
                        print("Error: No puede devolver más libros de los prestados.")

                    elif stock_libros + cantidad > STOCK_MAXIMO:
                        print("Error: Se supera la capacidad máxima de la biblioteca.")

                    else:
                        stock_libros += cantidad
                        prestamos_activos -= cantidad

                        print("\nDevolución realizada exitosamente.")
                        print(f"Libros devueltos: {cantidad}")
                        print(f"Stock disponible: {stock_libros}")

                except ValueError:
                    print("Error: Debe ingresar un número válido.")

        # Opción 4: Historial de préstamos
        elif opcion == 4:
            print("\n===== HISTORIAL DE PRÉSTAMOS =====")
            print(f"Total de préstamos activos durante la sesión: {prestamos_activos}")

        # Opción 5: Salir
        elif opcion == 5:
            print("\nGracias por utilizar nuestro software, hasta la próxima.")
            break

        # Opción inválida
        else:
            print("Error: Debe seleccionar una opción entre 1 y 5.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")