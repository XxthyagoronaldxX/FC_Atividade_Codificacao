import matplotlib.pyplot as grafico

import matplotlib.pyplot as grafico

def plotar_sinais(sinais, titulos, sequencia):
    grafico.figure(figsize=(12, 6))

    for i in range(len(sinais)):
        grafico.subplot(3, 1, i+1)  
        grafico.step(range(len(sinais[i])), sinais[i], where='mid', color='b') 
        grafico.ylim([-2, 2])  
        grafico.title(f'{titulos[i]} - Sequência: {sequencia}')
        grafico.xlabel('Tempo')  
        grafico.ylabel('Sinal') 
        grafico.grid(True)  

    grafico.tight_layout()  
    grafico.show()  

def codificar_ami(bits):
    ami = []  
    ultimo = 1
    for bit in bits:
        if (bit == '0'):
            ami.append(0)  
        else:
            ultimo = -ultimo  
            ami.append(ultimo)  
    return ami 


def codificar_manchester(bits):
    manchester = []  
    for bit in bits:
        if (bit == '0'):
            manchester.extend([1, -1])  
        else:
            manchester.extend([-1, 1])  
    return manchester  

def bits_para_ternario(bits):
    mapeamento = {
        '0000': [0, 0, 0],
        '0001': [0, 0, 1],
        '0010': [0, 1, 0],
        '0011': [0, 1, 1],
        '0100': [1, 0, 0],
        '0101': [1, 0, 1],
        '0110': [1, 1, 0],
        '0111': [1, 1, 1],
        '1000': [-1, 0, 0],
        '1001': [-1, 0, 1],
        '1010': [-1, 1, 0],
        '1011': [-1, 1, 1],
        '1100': [0, -1, 0],
        '1101': [0, -1, 1],
        '1110': [1, -1, 0],
        '1111': [1, -1, 1]
    }
    
    ternario = []  
    for i in range(0, len(bits), 4):
        bloco = bits[i:i+4]  
        ternario.extend(mapeamento[bloco]) 
    return ternario  



sequencia = '1000000001010011'


ami_codificado = codificar_ami(sequencia)
manchester_codificado = codificar_manchester(sequencia)
ternario_codificado = bits_para_ternario(sequencia)


sinais_codificados = [ami_codificado, manchester_codificado, ternario_codificado]
titulos_codificacoes = ["Codificação AMI", "Codificação Manchester", "Codificação 4B3T"]


plotar_sinais(sinais_codificados, titulos_codificacoes, sequencia)
