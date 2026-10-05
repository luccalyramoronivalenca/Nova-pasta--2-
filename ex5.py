def aprovacao (a1, a2, a3):
    notas = [a1, a2, a3]
    aprovados = [nota for nota in notas if nota > 7]
    return aprovados

print (aprovacao(8, 6, 9))