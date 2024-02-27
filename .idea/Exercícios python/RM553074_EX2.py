segunda =int(input("Digite a quantidade de votos para Segunda-Feira: "))
terca =int(input("Digite a quantidade de votos para Terça-Feira: "))
quarta =int(input("Digite a quantidade de votos para Quarta-Feira: "))
quinta =int(input("Digite a quantidade de votos para Quinta-Feira: "))
sexta =int(input("Digite a quantidade de votos para Sexta-Feira: "))


if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda-Feira venceu")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça-Feira venceu")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta-Feira venceu")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta-Feira venceu")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Sexta-Feira venceu")
else:
    print("Houve um empate")

print("Os votos foram:\nSegunda: {}\nTerÇa: {}\nQuarta: {}\nQuinta: {}\nSexta: {}".format(segunda, terca, quarta, quinta, sexta))

#ELABORADO POR: BRUNA MENDES DA CUNHA PASSOS RM:553074