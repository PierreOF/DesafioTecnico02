import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

class DesafioTecnico:

    def variavel_soma():
        indice = 13
        soma = 0
        aux = 0

        while aux < indice:
            aux += 1
            soma += aux

        return soma
        

    def fibonacci(num):
        a, b = 0, 1

        while a <= num:
            if a == num:
                return f"O número {num} pertence à sequência de Fibonacci."
            a, b = b, a + b
        return f"O número {num} não pertence à sequência de Fibonacci."
    
    def faturamento(dados):

        faturamento_geral = [d['valor'] for d in dados]
        faturamento_dias_validos = [d['valor'] for d in dados if d['valor'] > 0]

        # não consegui entender bem se para verificar o min e max de venda precisava considerar somente os dias validos, então considerei todos , inclusive os dias que não tiveram vendas.
        menor_faturamento = min(faturamento_geral)
        maior_faturamento = max(faturamento_geral)
        media_mensal = sum(faturamento_dias_validos) / len(faturamento_dias_validos)

        dias_acima_media = sum(1 for valor in faturamento_dias_validos if valor > media_mensal)

        return {
            "Menor Faturamento": round(menor_faturamento,2),
            "Maior Faturamento": round(maior_faturamento,2),
            "Dias acima da media": dias_acima_media
        }       

    def faturamento_estado():
        
        faturamento_estados_porcentagem = {}
        faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
        }

        total_faturamento = sum(faturamento_estados.values())

        for estado, valor in faturamento_estados.items():
            percentual = (valor / total_faturamento) * 100
            faturamento_estados_porcentagem[f'{estado}'] = f"{round(percentual,2)}" + "%"

        return faturamento_estados_porcentagem

    def inverter(palavra):
        palavra_invertida = ""
        
        for letra in palavra:
            palavra_invertida = letra + palavra_invertida
        
        return palavra_invertida


main = DesafioTecnico

# PRIMEIRA QUESTÃO
print(main.fibonacci(5))
# SEGUNDA QUESTÃO
print(main.variavel_soma())
# TERCEIRA QUESTÃO
print(main.faturamento(dados))
# QUARTA QUESTÃO
print(main.faturamento_estado())
# QUINTA QUESTÃO
print(main.inverter("): dlroW olleH"))