batteri = 50                    # Lager en variabel som skal forestille et batteri med en kapasitet på 50
fil = open("forbruk", "r")      # åpner fila forbruk i modus read som variabelen fil.
for rad in fil:                 # leser rad for rad fra fila
    batteri -= float(rad[:-1])  # gjør om alt per rad untatt "newline" tegnet, om til et desimaltal og oppdaterer batteriet
    print(batteri, " kw/t")     # printer ut batteristatus
fil.close()                     # lukker fila forsvarlig
