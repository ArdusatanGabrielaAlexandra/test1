import random
import sys



wordList = [
"ICONOGRAFĂ", "FAGOCITUL", "APICOLILOR", "HIPOPLAZII", "PROHODI", "CIOPLEA", "COVÂRȘITELOR", "PÂRGUIRILE",
 "BURGHIERILE", "SAMAVOLNICII", "CĂȘĂIEȘTE", "SISALUL", "CINERARIILE", "DEZAGLOMERĂM", "TETRODĂ"
,  "MÂNJITURII", "DESOFISTICĂRII", "TĂIERI", "GENTILEȚILOR", "NENOROCITUL", "ÎNAINTĂ", "ISTMICUL", "ASCUȚITUNGHICUL",
 "OBNUBILĂRILOR", "BUMBĂCELULUI", "POSTĂVĂRIILE", "CENTROZOMUL", "DEBAVURASE", "VRAMIȚE", "RETORI"    ,  "EPISTOLARELOR", "ÎNCHIABUREAȚI", "LAMINATOAREA", "PLATINEZ", "ȚĂNDĂRELEI", "TEVATURI", "FIDANȚATA", "EXONDĂRILE",
 "DECOMANDATĂ", "OMAGIALI", "STÂLPISEM", "ELFILOR", "DECONCERTANTELE", "GAGICULUI", "APELARĂM", "SPERMATOFITELOR",
  "NECREDINCIOȘILOR", "CINSTEȚUL", "NEOFORMAȚIUNII", "PEGMATITUL", "PLUTUIEȘTE", "CINTEZII", "FOLFĂIESC", "OTORINOLARINGOLOGELOR",
"ESTETIZANTEI", "BALAOACHEȘĂ", "NOTĂRIȚĂ", "DULEȚI", "RICKETTSIOZEI", "CIREȘE", "ZGĂRDAT", "PREȚIOASELOR",
"DIMPREJUR", "BULBUCAT", "ARIERDUNĂ", "FLACIDEI", "CONVENȚIONALI", "CUCONIȚĂ", "NELINIȘTITORULUI", "BIHINDISIRILE",
"ÎMPLINIREA", "INSTIGÂND", "RECENTE", "EMBLEMĂ", "SINGURAȘUL", "SUBSECRETARULUI", "DEVITALIZASERĂM", "SUBAPRECIEZ",
"CLASATULUI", "FARAONICUL", "ÎNROLĂRILOR", "PRIMEZIU", "CRUCIATULUI", "PRODIGATELE", "VINA", "CIFRARĂM",
"ÎNFRUNTASEM", "VIOȘELI", "AMUȘISERĂȚI", "TELEGRAFIARĂ", "CITRONADELE", "BASCHETBALIȘTILOR", "SEPTICUL", "VENENO",
"GUDRONĂM", "CORDENCIULUI", "STROPȘIRE", "FOILETONIST", "PLICISERĂ", "ACHITAT" ]

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
letter_storage = []











def change():

    for character in secretWord:
        guess_word.append("*")

    print("Cuvântul are", length_word, "caractere")

    print("Rețineți că puteți introduce doar o litera din alfabet,de la A-Z\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Introduceti o literă\n").upper()

        if not guess in alphabet:
            print("Introduceti o literă de la A-Z ")
        elif guess in letter_storage:            print("Ai ghicit deja aceasta litera!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("Litera corecta!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '*' in guess_word:
                    print("Ai castigat!")
                    break
