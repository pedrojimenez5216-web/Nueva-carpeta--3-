def mostrar_menu():
    """Muestra las opciones disponibles en el menú principal."""
    print("\n=== GESTOR DE GASTOS ===")
    print("1. Registrar gasto")
    print("2. Ver todos los gastos")
    print("3. Filtrar por categoría")
    print("4. Ver resumen total")
    print("5. Salir")


def agregar_gasto(gastos):
    """Solicita los datos de un gasto, los valida y los guarda en la lista."""
    descripcion = input("Descripción del gasto: ").strip()
    while not descripcion:
        print("-> La descripción no puede estar vacía.")
        descripcion = input("Descripción del gasto: ").strip()

    while True:
        try:
            monto = float(input("Monto ($): "))
            if monto <= 0:
                print("-> El monto debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("-> Entrada inválida. Por favor, ingresa un número válido.")

    categoria = input("Categoría (Comida/Transporte/Ocio/Otros): ").strip()
    if not categoria:
        categoria = "Otros"

    gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria.capitalize(),
    }
    gastos.append(gasto)
    print("-> Gasto registrado con éxito.")


def mostrar_gastos(gastos):
    """Muestra todos los gastos registrados de forma numerada y legible."""
    if not gastos:
        print("\nNo hay gastos registrados todavía.")
        return

    print("\n--- LISTA DE GASTOS ---")
    for indice, gasto in enumerate(gastos, start=1):
        print(
            f"{indice}. {gasto['descripcion']} | "
            f"Categoría: {gasto['categoria']} | "
            f"Monto: ${gasto['monto']:.2f}"
        )


def filtrar_por_categoria(gastos):
    """Filtra y muestra los gastos que coinciden con la categoría indicada."""
    if not gastos:
        print("\nNo hay gastos registrados para filtrar.")
        return

    categoria_buscada = input("Ingresa la categoría a filtrar: ").strip().lower()
    coincidencias = [
        gasto for gasto in gastos if gasto["categoria"].lower() == categoria_buscada
    ]

    if not coincidencias:
        print(f"\nNo se encontraron gastos en la categoría '{categoria_buscada.capitalize()}'.")
        return

    print(f"\n--- GASTOS EN CATEGORÍA: {categoria_buscada.capitalize()} ---")
    for indice, gasto in enumerate(coincidencias, start=1):
        print(f"{indice}. {gasto['descripcion']} - ${gasto['monto']:.2f}")


def calcular_resumen(gastos):
    """Calcula y muestra el total general y el desglose por categoría."""
    print("\n--- RESUMEN DE GASTOS ---")
    if not gastos:
        print("Total general: $0.00")
        print("No hay gastos registrados para desglosar.")
        return

    total_general = 0.0
    totales_por_categoria = {}

    for gasto in gastos:
        monto = gasto["monto"]
        categoria = gasto["categoria"]
        total_general += monto
        totales_por_categoria[categoria] = totales_por_categoria.get(categoria, 0.0) + monto

    print(f"Total general: ${total_general:.2f}")
    for categoria, subtotal in totales_por_categoria.items():
        print(f"- {categoria}: ${subtotal:.2f}")


def main():
    """Función principal que controla el ciclo del programa."""
    gastos = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            filtrar_por_categoria(gastos)
        elif opcion == "4":
            calcular_resumen(gastos)
        elif opcion == "5":
            print("¡Hasta luego! Gracias por usar el Gestor de Gastos.")
            break
        else:
            print("-> Opción no válida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    main()