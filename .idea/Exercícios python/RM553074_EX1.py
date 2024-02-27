tipo_assinatura = input("Por favor, o número correspondente a sua assinatura:\n 1-BASIC\n "
                        "2-SILVER\n 3-GOLD\n4-PLATINUM: \n")
fat_anual = float(input("Por favor, digite seu faturamento anual R$: "))
bonus = 0
if tipo_assinatura == "1":
    bonus = fat_anual * 0.3
elif tipo_assinatura == "2":
    bonus = fat_anual * 0.2
elif tipo_assinatura == "3":
    bonus = fat_anual * 0.1
elif tipo_assinatura == "4":
    bonus = fat_anual * 0.05
else:
    print("Plano inexistente ou digitado incorretamente")

print("Com base no seu plano {}, o bônus concedido é de R$: {}".format(tipo_assinatura, bonus))

#ELABORADO POR: BRUNA MENDES DA CUNHA PASSOS RM:553074