nome = (input('Digite o seu nome'))
salario = int(input('Salario'))
vendas = int(input('Vendas'))

porcentagem = vendas * 0.15
soma = salario + porcentagem

print(nome, 'o seu salario fixo é ', salario, 'o seu salario no final do mes é ', soma)