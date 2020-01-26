preco = float(input('Diga qual o valor do salário R$ '))
acrescimo = int(input('Diga o valor do acrescimo em porcentagem: '))
acrescimoAplicado = preco * (acrescimo / 100)
valorFinal = preco + acrescimoAplicado
print('o salário de R${} com um acrescimo de {}% sairá por R${}'.format(preco, acrescimo, valorFinal))
