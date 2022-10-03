# # Printovanje

# print(123)
# print("tekst123")
# print('tekst123')
# print("ETS \"Nikola Tesla\"")
# print('Milan\'s PC is called "Milan\'s PC"')

# # Promenljive

# godina_rodjenja = 1994
# trenutna_godina = 2022

# godine_starosti = trenutna_godina - godina_rodjenja

# print("Ove godine punite " + str(godine_starosti) + " godina")
# print("Ove godine punite {0} godina".format(godine_starosti))
# print(f"Ove godine punite {godine_starosti} godina")

# # Cuvanje podataka zadatih od korisnika

# ime = input("Unesite svoje ime: ")
# prezime = input("Unesite svoje prezime: ")

# puno_ime_i_prezime = f"{ime} {prezime}"

# print(puno_ime_i_prezime)

# a = float(input("Unesite bilo koji realan broj: "))
# b = float(input("Unesite bilo koji realan broj: "))

# c = a + b

# print(f"{a:.2f} + {b:.2f} = {c:.2f}")

# # .2f - dva decimalna mesta iza tacke
# # 7.3f - pravi poravnjanje

# # Pisanje programa

# tempC = float(input("Unesite temperaturu u stepenima C°: "))

# tempF = tempC * 1.8 + 32

# print(f"Ta temperatura u F° iznosi {tempF:.2f}")

# :.2f - ostavlja dva broja iza tacke kao i sto :.0f ostavlja nula brojeva iza tacke

# #int - ceo broj

# # Konvertovati decimalni broj u binarni zapis:

# broj = int(input("Unesite ceo broj od 0 do 255: "))

# # 10

# bit_1 = broj % 2    #0 -
# broj = broj // 2    #5

# bit_2 = broj % 2    #1 -
# broj = broj // 2    #2

# bit_3 = broj % 2    #0 -
# broj = broj // 2    #1

# bit_4 = broj % 2    #1 -
# broj = broj // 2    #0

# bit_5 = broj % 2    #0 -
# broj = broj // 2    #0

# bit_6 = broj % 2    #0 -
# broj = broj // 2    #0

# bit_7 = broj % 2    #0 -
# broj = broj // 2    #0

# bit_8 = broj % 2    #0 -
# broj = broj // 2    #0

# print(f"{bit_8}{bit_7}{bit_6}{bit_5}{bit_4}{bit_3}{bit_2}{bit_1}")

# kartica = input("Unesite broj platne kartice: ")

# duzina_teksta = len(kartica)

# print(f"Ovaj tekst ima {duzina_teksta} karaktera.")

# prva_dva_simbola = kartica[0:2]

# # [0, 2] - Poceti od nultog indeksa i ne prikazivati drugi

# print(prva_dva_simbola)

# poslednja_dva_simbola = kartica[-2:]

# # [-2:] - Poceti od pretposlednjeg i racunati sve posle njega

# print(poslednja_dva_simbola)

# sve_od_drugog_pa_nadalje = kartica[1:]

# # [1:] - Od drugog indeksa pa do kraja

# print(sve_od_drugog_pa_nadalje)

# svaki_drugi_karakter = kartica[1::2]

# #[1::2] - prikazati svaki drugi karakter poceti od indeksa 1

# # print(svaki_drugi_karakter)

# # Konkretan zadatak:

# # Maskirati broj platne kartice:

# broj_platne_kartice = input("Unesite broj platne kartice: ")

# vidljivi_brojevi = broj_platne_kartice[-4:]

# print(f"Broj Vase platne kartice je ****-****-****-{vidljivi_brojevi}")

# # Prikazati cifre broja unazad

# broj = int(input("Unesite neki ceo broj: "))

# broj = str(broj)

# cifre_unazad = broj[-1::-1]

# cifre_unazad = int(cifre_unazad)

# print(cifre_unazad)

# # Zadatak sa zabom:

# # Koliko zabi treba da dodje do sigurne pozicije ako je udaljena na odredjeno rastojanje izrazeno u cm od nebezbedne pozicije koja je deli od bezbedne

# # Potrebni su nam sledeci podaci:

# # Koliko je zaba udaljena od ivice puta?
# # Koliko je sirok put?
# # Koliko daleko zaba moze da skoci?
# # Dobija se koliko je najmanje skokova potrebno zabi da predje put i stigne do bezbedne pozicije

# udaljenost_zabe_od_ivice_puta = float(input("Udaljenost zabe od ivice puta je: "))
# sirina_puta = float(input("Sirina puta je: "))
# duzina_skoka_zabe = float(input("Zaba moze da skoci daleko: "))

# puno_rastojanje_od_bezbedne_pozicije = udaljenost_zabe_od_ivice_puta + sirina_puta

# broj_skokova_koji_je_potreban_zabi = puno_rastojanje_od_bezbedne_pozicije / duzina_skoka_zabe

# import math

# bezbedan_broj_skokova = math.ceil(broj_skokova_koji_je_potreban_zabi)

# print(f"Zaba treba da napravi {bezbedan_broj_skokova} skokova da bi se nasla na bezbednoj poziciji.")

# # Nalazenje korena uz pomoc math biblioteke

# import math

# zadati_broj = int(input("Unesite neki ceo broj: "))

# koren_iz_zadatog_broja = math.sqrt(zadati_broj)

# print(f"Koren iz unesenog broja iznosi {koren_iz_zadatog_broja:.0f}")

# # Zadatak sa BRUTOM i NETOM

# # Traziti od korisnika BRUTO kolicinu i uz pomoc nje izracunati NETO kolicinu ako:

# # na zdravstvene ustanove odlazi 30%
# # na socijalne ustanove odlazi 20%
# # na prehrambene ustanove odlazi 5%

# BRUTO = float(input("Unesite vrednost BRUTO kolicine: "))

# zdravstvene_ustanove = BRUTO * .3
# prehrambene_ustanove = BRUTO * .2
# socijalne_ustanove = BRUTO * .05

# NETO = BRUTO - (zdravstvene_ustanove + prehrambene_ustanove + socijalne_ustanove)

# print(f"Vrednost NETO kolicine je {NETO:.0f}")
