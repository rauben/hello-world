import  time,os,sys

zugriffszeit = os.path.getatime(sys.argv[1])
aktuelleZeit = time.time()
ausgabe = """Die Datei ist seit{}Stunden nicht mehr gelesen worden""".format(int(aktuelleZeit-zugriffszeit)/3600)
print(ausgabe)

print("Hello World!")
