def agregar_notas(listas):
    try:
        nota = 0
        while nota <= 0:
            nota = float(input("ingrese la notas:\n"))
        listas.append(nota)
        print("la nota fue agregada con exito")
    except:
        print("la nota debe ser un valor numerico decimal entero")