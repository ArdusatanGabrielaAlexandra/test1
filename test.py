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

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from A-Z\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Pick a letter\n").upper()

        if not guess in alphabet: #checking input
            print("Enter a letter from A-Z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '*' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print("  You lost :<! The secret word was",         secretWord)


change()
guessing()

print("Game Over!")

