import datetime

def calcular_idade(data_nascimento):
  """Calcula a idade em anos e meses completos a partir da data de nascimento.

  Args:
    data_nascimento: Uma string no formato 'DD/MM/AAAA'.

  Returns:
    Uma tupla (anos, meses) representando a idade.
  """

  # Converte a data de nascimento para um objeto datetime
  data_nasc = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')

  # Obtém a data atual
  hoje = datetime.datetime.now()

  # Calcula a diferença em dias
  diferenca = hoje - data_nasc

  # Calcula a idade em anos e meses
  anos = diferenca.days // 365
  meses = (diferenca.days % 365) // 30

  return anos, meses
#print(converted_date)  # Output: 25/11/2023

## Solicita a data de nascimento ao usuário
#data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
#
## Chama a função para calcular a idade
#anos, meses = calcular_idade(data_nascimento)
#
## Exibe o resultado
#print(f"Você tem {anos} anos e {meses} meses.")



def convert_date_format(date_str):
  """Converts a date string from YYYY-MM-DD to DD/MM/YYYY format.

  Args:
    date_str: The date string in YYYY-MM-DD format.

  Returns:
    The converted date string in DD/MM/YYYY format.
  """

  date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
  return date_obj.strftime('%d/%m/%Y')

# Example usage:
#date_string = "2023-11-25"
#converted_date = convert_date_format(date_string)