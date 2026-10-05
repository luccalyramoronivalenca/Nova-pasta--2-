def cargahoraria (horas):
    if horas >= 40:
        return "Carga horária completa"
    else:
        return "Carga horária incompleta"

print (cargahoraria(35))