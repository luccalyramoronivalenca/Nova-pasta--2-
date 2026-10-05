def notas (n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

print (notas(7, 8, 9))