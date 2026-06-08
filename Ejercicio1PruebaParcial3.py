# Hospital Central Metropolitano     
# Registro de Médicos Recién Llegados

# Contadores automáticos
especialistas = 0
residentes = 0

# Validar cantidad de médicos a registrar
while True:
    try:
        cantidad_medicos = int(input("¿Cuántos médicos desea registrar?: "))

        if cantidad_medicos > 0:
            break
        else:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

# ------------------------------------------
# Registro de médicos
# ------------------------------------------
for i in range(1, cantidad_medicos + 1):

    print(f"\n===== MÉDICO {i} =====")

    # --------------------------------------
    # Validar nombre profesional
    # --------------------------------------
    while True:
        nombre = input("Nombre profesional: ")

        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

    # --------------------------------------
    # Validar experiencia clínica
    # --------------------------------------
    while True:
        try:
            experiencia = int(input("Años de experiencia clínica: "))

            if experiencia > 0:
                break
            else:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    # --------------------------------------
    # Clasificación del médico
    # --------------------------------------
    if experiencia > 5:
        clasificacion = "Especialista Senior"
        especialistas += 1
    else:
        clasificacion = "Residente Junior"
        residentes += 1

    # --------------------------------------
    # Mostrar resultado individual
    # --------------------------------------
    print("\n--- Registro completado ---")
    print(f"Médico: {nombre}")
    print(f"Experiencia: {experiencia} años")
    print(f"Clasificación: {clasificacion}")

# ------------------------------------------
# Resumen final
# ------------------------------------------
print("\n===================================")
print("RESUMEN FINAL DEL HOSPITAL")
print("===================================")

print(f"Total de médicos registrados: {cantidad_medicos}")
print(f"Especialistas Senior: {especialistas}")
print(f"Residentes Junior: {residentes}")

print(f'\n"¡El hospital cuenta con {especialistas} Especialistas Senior ')
print(f'y {residentes} Residentes Junior! ')
print(f'¡Sistema listo para operar!"')