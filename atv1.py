def decorator_imprimir(func):
    def imprimir(capital, taxa, tempo):
        print(f'CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}')
        resultado = func(capital, taxa, tempo)
        print(f"RESULTADO: {resultado}")
        return resultado
    return imprimir

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_simples(1000 , 5 , 6)