my_text = ("Unele caractere nu pot fi incluse direct într-un șir de caractere. "
		   "De exemplu, ghilimelele duble nu pot fi incluse direct într-un șir "
		   "delimitat de ghilimele duble; acest lucru ar cauza terminarea prematură a șirului."
		   "Caracterele de acest tip trebuie „escapate” prin plasarea unui backslash (\"\") înaintea lor. "
		   "Ghilimelele duble trebuie escapate doar în șiruri cu ghilimele duble, și același lucru este valabil și"
		   " pentru șirurile cu ghilimele simple.")

# SLICING
# print(my_text[5:0:-1])

inceput = 0
final = 5
pas = 1
#
# print(my_text[inceput:final:pas])
# print(my_text[::])


# METODE UZUALE
print(my_text)

print(my_text.upper())
print(my_text.lower())
print(my_text.replace("a", "b").replace("A","B"))
print(my_text.strip())
