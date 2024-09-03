import json
import numpy as np
import math
#Disclaimer: utilizou-se numpy porque as operacoes de media, maximo e minimo sao relativamente triviais e sua abstracao torna o codigo mais
#limpo e simpes
###########  Questão 1  ###########
INDICE = 13
SOMA = 0 
K = 0
while K < INDICE : 
    K = K + 1; SOMA = SOMA + K; 
print(SOMA) 

#Resposta : 91

###########  Questão 2  ###########

#utilizaremos um arquivo json ficticio para obter os dados
with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = np.array([dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0])

menor_valor = np.min(faturamento)
maior_valor = np.max(faturamento)
media_mensal = np.mean(faturamento)
dias_acima_da_media = np.sum(faturamento > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

###########  Questão 3 ###########

####Apesar de podermos fazer pelo método iterativo, seria mais custoso e trabalhoso fazer dessa forma. Podemos usar a propriedade que diz que
# se 5n²±4 for quadrado perfeito, n faz parte da sequencia de fibonacci:
def eh_fibonacci(x):
    def eh_quadrado_perfeito(num):
        raiz = int(math.sqrt(num))
        return raiz * raiz == num

    return eh_quadrado_perfeito(5 * x * x + 4) or eh_quadrado_perfeito(5 * x * x - 4)


###########  Questão 4 ###########

import numpy as np

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

estados = np.array(list(faturamento.keys()))
valores = np.array(list(faturamento.values()))

total_mensal = np.sum(valores)
percentuais = (valores / total_mensal) * 100

print("Percentual de representação por estado:")
for estado, percentual in zip(estados, percentuais):
    print(f"{estado}: {percentual:.2f}%")

###########  Questão 5 ###########
## Nessa funcao, pegamos uma entrada, determinamos o comprimento dela, 
def inverter(entrada):
    tam = len(entrada)
    #copia = [''] * tam
    
    for a in range(tam):
        copia[a] = entrada[tam - a - 1]
    
    copia = ''.join(copia)
    print(copia)
    
    return copia

entrada = "exemplo"
resultado = inverter(entrada)
