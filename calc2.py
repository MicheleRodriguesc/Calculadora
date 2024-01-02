
def calculadora(n1, n2, operacao):
  "
  Calculadora de dois números

  Args:
    n1: O primeiro número
    n2: O segundo número
    operacao: O número da operação a ser executada

  Returns:
    O resultado da operação
  "

  # Validar a operação
  if operacao not in [1, 2, 3, 4]:
    return 0

  # Executar a operação
  if operacao == 1:
    return n1 + n2
  elif operacao == 2:
    return n1 - n2
  elif operacao == 3:
    return n1 * n2
  else:
    return n1 / n2