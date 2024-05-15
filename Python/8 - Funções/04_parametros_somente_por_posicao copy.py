# Define uma função chamada criar_carro que recebe os parâmetros modelo, ano e placa como argumentos posicionais obrigatórios,
# e marca, motor e combustivel como argumentos nomeados.
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # Imprime os detalhes do carro formatados.
    print(modelo, ano, placa, marca, motor, combustivel)

# Chama a função criar_carro com argumentos posicionais seguidos por argumentos nomeados.
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Tenta chamar a função criar_carro passando todos os argumentos como nomeados,
# o que resulta em um erro porque modelo, ano e placa devem ser argumentos posicionais.
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# Resumo:
# O código define uma função criar_carro que recebe seis parâmetros:
# - modelo, ano, placa: Devem ser passados como argumentos posicionais obrigatórios devido ao uso da barra (/) na assinatura da função.
# - marca, motor, combustivel: Devem ser passados como argumentos nomeados.
# A função imprime os detalhes do carro formatados.
# A primeira chamada da função é válida, pois respeita a exigência de argumentos posicionais e nomeados.
# A segunda chamada da função é inválida e resultará em um erro, pois tenta passar todos os argumentos como nomeados,
# o que não é permitido para os três primeiros parâmetros.
