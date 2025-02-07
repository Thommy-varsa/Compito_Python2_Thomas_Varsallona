prezzo1=int(input("inserisci il prezzo del primo jeans: "))
prezzo2=int(input("inserisci il prezzo del secondo jeans: "))
prezzo_scontato1=prezzo1-prezzo1*0.20
prezzo_scontato2=prezzo2-prezzo2*0.20
print("il prezzo scontato è: ", prezzo_scontato1)
print("il prezzo scontato è: ", prezzo_scontato2)
contanti=int(input("inserisci i contanti: "))
resto=contanti-prezzo_scontato1-prezzo_scontato2
print("resto: ", resto)