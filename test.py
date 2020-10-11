import random
import sys


# lets set some variables
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
secretWord = random.choice(wordList) # lets randomize single word from the list
length_word = len(secretWord)
alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
letter_storage = []











def change():

    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("*")

    print("Cuvântul are", length_word, "caractere")

    print("Rețineți că puteți introduce doar o litera din alfabet,de la A-Z\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Introduceti o literă\n").upper()

        if not guess in alphabet: #checking input
            print("Introduceti o litera de la A-Z ")
        elif guess in letter_storage: #checking if letter has been already used
            print("Ai ghicit deja aceasta litera!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("Litera corecta!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '*' in guess_word:
                    print("Ai castigat!")
                    break
            else:
                print("Litera nu este in cuvant. Incearca din nou!")
                guess_taken += 1
                if guess_taken == 10:
                    print("  Ai pierdut! Cuvantul a fost",         secretWord)


change()
guessing()

print("Joc incheiat!")

