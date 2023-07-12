Materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
Aprobadas = []

for materia in Materias:

    puntaje = float(input("¿Qué nota has sacado en " + materia + "?"))

    if puntaje >= 5:

        Aprobadas.append(materia)

for materia in Aprobadas:

    Materias.remove(materia)
    
print("Tienes que repetir " + str(Materias))