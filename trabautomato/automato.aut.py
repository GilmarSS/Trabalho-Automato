import json
import sys
import csv
import time

arquivo1 = "arquivo_automato.aut.json"
arquivo2 = "arquivo_de_testes.in.csv"
arquivo3 = "arquivo_de_saida.out"

if len(sys.argv) > 1:
    arquivo1 = sys.argv[1]
if len(sys.argv) > 2:
    arquivo2 = sys.argv[2]
if len(sys.argv) > 3:
    arquivo3 = sys.argv[3]

with open(arquivo1, 'r', encoding='utf-8') as dados:
    arq_json = json.load(dados)

entradas = []

with open(arquivo2, "r", encoding='utf-8') as csvfile:
    
    arq_csv = csv.reader(csvfile, delimiter=";")

    for linha in arq_csv:
        entradas.append(linha)

initial_state = arq_json["initial"]
final_states = arq_json["final"]
transitions = arq_json["transitions"]

with open(arquivo3, "w", encoding='utf-8') as saida:
    for entrada in entradas:
        tempo_inicial = time.time()

        atual_state = initial_state

        cont = 0
        wrongLetter = False
        for transition in transitions:

            from_state = transition["from"]
            read_symbol = transition["read"]
            to_state = transition["to"]

            if from_state == atual_state:

                if read_symbol == entrada[0][cont]:
                    atual_state = to_state

                    if cont < len(entrada[0]) - 1:
                        cont += 1
                    elif cont == len(entrada[0]) - 1:

                        break
                else:

                    wrongLetter = True
                    break

        valorFinal = 0
        for final in final_states:
            if atual_state == final and not wrongLetter:
                valorFinal = 1
        tempo_final = time.time()

        entrada_str = entrada[0]
        resultado_esperado = entrada[1]

        tempo = f"{tempo_final - tempo_inicial:.5f}"
        saida.write(
            f"{entrada_str};{resultado_esperado};{valorFinal};{tempo}\n")