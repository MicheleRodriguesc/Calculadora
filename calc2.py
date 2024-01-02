
def calculadora(n1, n2, operacao):
  "
  Calculadora de dois n�meros

  Args:
    n1: O primeiro n�mero
    n2: O segundo n�mero
    operacao: O n�mero da opera��o a ser executada

  Returns:
    O resultado da opera��o
  "

  # Validar a opera��o
  if operacao not in [1, 2, 3, 4]:
    return 0

  # Executar a opera��o
  if operacao == 1:
    return n1 + n2
  elif operacao == 2:
    return n1 - n2
  elif operacao == 3:
    return n1 * n2
  else:
    return n1 / n2