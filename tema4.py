import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# 3. Afișarea șablonului inițial
print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit: ", " ".join(progres))

# 4. Buclă principală de joc
while incercari_ramase > 0 and "_" in progres:
	# a. Cererea unei litere
	litera = input("Introdu o literă: ").lower()

	# b. Verificarea validității
	if len(litera) != 1 or not litera.isalpha():
		print("Te rog să introduci o literă validă.")
		continue
	if litera in litere_incercate:
		print("Ai încercat deja această literă!")
		continue

	litere_incercate.append(litera)

	# c. Verificarea literei în cuvânt
	if litera in cuvant_de_ghicit:
		for i in range(len(cuvant_de_ghicit)):
			if cuvant_de_ghicit[i] == litera:
				progres[i] = litera
		print("Corect! Progresul tău:", " ".join(progres))
	else:
		incercari_ramase -= 1
		print(f"Litere incorectă! Îți mai rămân {incercari_ramase} încercări.")

	# 5. Afișarea progresului și încercărilor rămase
	print("Progresul tău:", " ".join(progres))
	print("Litere încercate:", ", ".join(litere_incercate))

# 6. Încheierea jocului
if "_" not in progres:
	print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
	print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
