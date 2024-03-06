def inverter_string(string):
  string_invertida = ""
  i = len(string) - 1

  while i >= 0:
    string_invertida += string[i]
    i -= 1

  return string_invertida

string = "Guilherme de Moraes"
string_invertida = inverter_string(string)
print(string_invertida)