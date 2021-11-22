#!/usr/bin/env python
# coding: utf-8

# In[25]:


# import kniznice na generovanie nahodneho cisla
from random import randrange

def main() -> None:
    '''
    1. definujem oddelovac - caru
    2. vypisem uvod
    3. spustim cyklus hry
    '''
    cara = '-' * 60
    print(
        f'Hi there!',
        cara,
        f'I´ve generated a random 4 digit number for you.',
        f'Let´s play a bulls and cows game',
        cara,
        sep='\n'
    )

    cyklus_hry()

def isUnique(string: str) -> bool:
    '''
    overi ci je kazda cislica v cisle unikatna
    1. vytvorit list na ukladanie znakov
    2. for loop na iterovanie cez vsetky znaky
    3. pokial este nie je znak v liste na ukladanie znakov prida ho tam
    4. pokial uz je vrati bool = False
    5. pokial cely loop dobehol az dokonca, vrati bool = True
    '''
    string_set = list()
    for i in range(0,len(string)):
        if string[i] not in string_set:
            string_set.append(string[i])
        else:
            return False
    return True

def vygeneruj_cislo() -> str:
    '''
    1. while cyklus generuje cislo kym cislice nesplnaju unikatnost znakov
    2. vrati premennu number
    '''
    while not isUnique(number := str(randrange(1000, 10000, 4))):
        pass
    print(number)
    return number

def over_spravnost_cisla() -> str:
    '''
    1. definujem oddelovac - caru
    2. over ci je numericke, dlhe 4 cislice, neobsahuje rovnake cislice a nezacina nulou
    3. pokial nespluje cokolvek z bodu 1 zadaj cislo znovu
    '''
    cara = '-' * 60

    while not (guess := input('enter number: ')).isnumeric() or not len(str(guess))==4 or not isUnique(str(guess)) or guess.startswith('0'):
        print(
            f'Enter only numeric characters !!!',
            f'Must contain 4 digits exactly !!!',
            f'Must not contain duplicates   !!!',
            f'Cannot start with 0           !!!',
            cara,
            sep='\n'
        )
        #guess = input('enter number: ')

    return guess

def over_zhody_znakov(guess: str, number: str) -> list:
    '''
    1. vytvor list na ukladanie cislic a indexu cislic zaroven, a list iba na zhodu cislic
    2. for cyklus na iterovanie cez vsetky znaky v hadanom cisle
        3. for cyklus na iterovanie cez vsetky znaky v generovanom cisle
            4. podmienky na urcenie zhody cislice a indexu cislic
            5. ukladanie do pripravenych listov
    6. return listy
    '''

    chars_in_place = list()
    chars_not_in_place = list()

    for index_in_guess in range(0,len(guess)):

        for index_in_number in range(0,len(number)):

            if number[index_in_number] == guess[index_in_guess] and index_in_number == index_in_guess:
                chars_in_place.append(number[index_in_number])

            elif number[index_in_number] == guess[index_in_guess] and index_in_number != index_in_guess:
                chars_not_in_place.append(number[index_in_number])

    return chars_in_place, chars_not_in_place

def urci_tvar_slova(slovo : str, chars : int) -> str:
    '''
    1. urci ci sa bude pouzivat slovicko cow/cows, bull/bulls, guess/guesses
    '''
    if slovo == 'guess' and chars == 1:
        slovo = slovo
    elif slovo == 'guess' and chars != 1:
        slovo += 'es'
    elif slovo != 'guess' and chars == 1:
        slovo = slovo
    elif slovo != 'guess' and chars != 1:
        slovo += 's'

    return slovo

def vypis_bilanciu(chars_in_place: list, chars_not_in_place: list) -> None:
    '''
    1. definujem oddelovac - caru
    2. vypis bilanciu bulls/cows
    '''
    cara = '-' * 60 
    print(
        f'{len(chars_in_place)} {urci_tvar_slova("bull", len(chars_in_place))}',
        f'{len(chars_not_in_place)} {urci_tvar_slova("cow", len(chars_not_in_place))}',                
        f'{cara}',
        sep='\n'
    )

def vypis_vysledky(counter: int) -> None:
    '''
    vypise vysledky
    '''
    print(
        f'Correct, you have guessed the right number ',
        f'in {counter} {urci_tvar_slova("guess", counter)} !',
        sep='\n'
    )

def cyklus_hry() -> None:
    '''
    1. funkcia - vygeneruj_cislo
    2. nastavim pocitadlo cyklov na 0
    3. spustim while cyklus - cyklus samotnej hry
        4. navysim pocitadlo cyklov o 1
        5. funkcia - over_spravnost_cisla
        6. podmienka na kontrolu ci sa guess rovna number
            7. funkcia - over_zhody_znakov
            8. funkcia - vypis bilanciu
    9. funkcia - vypis_vysledky
    '''

    number = vygeneruj_cislo()

    # nastavim pocitadlo cyklov
    counter = 0

    # while cyklus sa bude opakovat az kym sa hadane cislo nebude zhodovat s vygenerovanym
    while True: 

        # zakazdym novym spustenim cyklu sa pocitadlo navysi o 1
        counter += 1

        guess = over_spravnost_cisla()

        print(guess)

        # pokial sa generovane a hadane cislo zhoduju, ukoncim while cyklus 
        if guess == number:
            break

        # podmienka pokial sa hadane cislo nezhoduje s generovanym - vypocitam a vypisem bulls/cows
        elif guess != number:
 
            chars_in_place, chars_not_in_place = over_zhody_znakov(guess, number)

            vypis_bilanciu(chars_in_place, chars_not_in_place)

    vypis_vysledky(counter)

main()

