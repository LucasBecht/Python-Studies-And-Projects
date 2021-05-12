# Calculadora de área
print("Bem Vindo a calculadora de área, Para utilizar, insira as medidas da residência em m²")

# Entrada 
sala_area = float(input("Área da Sala: "))
cozinha_area = float(input("Área da Cozinha: "))
banheiro_area = float(input("Área do Banheiro Social: "))
quarto1_area = float(input("Área do primeiro quarto: "))
quarto2_area = float(input("Área do segundo quarto: "))

# Processamento
area_total = sala_area + cozinha_area + banheiro_area + quarto1_area + quarto2_area

if area_total>=100 :
 valor_total = area_total * 1200
else :
 valor_total =  area_total * 1000

# Saida de Dados
print("A área total da residência é %.2f M², e o valor total é R$%.2f" %(area_total, valor_total))
