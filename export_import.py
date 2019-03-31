print("Upišite potrebne podatke za izračun uvećanja plaće: ")
placa = int(input("\t- plaća: "))
staz = int(input("\t- godine staža: "))

if staz >= 10:
    ukupna_placa = placa * (1+(staz/100))
    print("Vaša plaća se uvećava za " + str(staz) + "% i iznosi " + str(ukupna_placa))
else:
    print("Nemate pravo na povećanje plaće.")