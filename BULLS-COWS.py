#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randrange


def hlavna() -> None:
    '''
    1. spustim cyklus hry
    '''
    cyklus_hry()


def je_unikatna(string: str) -> bool:
    '''
    overi ci je kazda cislica v cisle unikatna
    1. vytvorit list na ukladanie znakov
    2. for loop na iterovanie cez vsetky znaky
    3. pokial este nie je znak v liste na ukladanie znakov prida ho tam
    4. pokial uz je vrati bool = False
    5. pokial cely loop dobehol az dokonca, vrati bool = True
    '''
    string_set = list()
    for i in range(0, len(string)):
        if string[i] not in string_set:
            string_set.append(string[i])
        else:
            return False
    return True


def vygeneruj_cislo() -> str:
    '''
    1. while cyklus generuje cislo kym cislice nesplnaju unikatnost znakov
    2. vrati premennu cislo
    '''
    while not je_unikatna(cislo := str(randrange(1000, 10000, 4))):
        pass
    print(cislo)
    return cislo


def over_spravnost_cisla() -> str:
    '''
    1. over ci je numericke, dlhe 4 cislice, neobsahuje rovnake cislice a nezacina nulou
    2. pokial nespluje cokolvek z bodu 1 zadaj cislo znovu
    '''
    cara = '-' * 60
    while not (hadane := input('enter number: ')).isnumeric() or not len(str(hadane))==4 or len(set(hadane)) != 4 or hadane.startswith('0'):
        print(
            '''
            Enter only numeric characters !!!\n
            Must contain 4 digits exactly !!!\n
            Must not contain duplicates   !!!\n
            Cannnot start with 0          !!!\n
            ''',
            cara,
        )
        
    return hadane


def over_zhody_znakov(hadane: str, cislo: str) -> list:
    '''
    1. vytvor premenne na pocitanie znakov na mieste a ynakov mimo miesto
    2. for cyklus na iterovanie cez vsetky znaky v generovanom cisle
    3. podmienky na rozlisenie ci sa zhoduje cislica aj index alebo iba cislica
    6. vrat premenne
    '''

    znaky_na_mieste: int = 0
    znaky_mimo: int = 0

    for index, cislica in enumerate(cislo):
        if hadane[index] == cislica:
            znaky_na_mieste += 1
        elif hadane[index] in cislo:
            znaky_mimo += 1

    return znaky_na_mieste, znaky_mimo


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


def vypis_bilanciu(znaky_na_mieste: list, znaky_mimo: list) -> None:
    '''
    1. vypis bilanciu bulls/cows
    '''
    cara = '-' * 60
    print(
        f'{znaky_na_mieste} {urci_tvar_slova("bull", znaky_na_mieste)}',
        f'{znaky_mimo} {urci_tvar_slova("cow", znaky_mimo)}',                
        f'{cara}',
        sep='\n'
    )


def vypis_vysledky(pocitadlo: int) -> None:
    '''
    vypise vysledky
    '''
    print(
        f'Correct, you have guessed the right number ',
        f'in {pocitadlo} {urci_tvar_slova("guess", pocitadlo)} !',
        sep='\n'
    )


def cyklus_hry() -> None:
    '''
    1. definujem oddelovac - caru
    2. vypisem uvod
    3. funkcia - vygeneruj_cislo
    4. nastavim pocitadlo cyklov na 0
    5. spustim while cyklus - cyklus samotnej hry
        6. navysim pocitadlo cyklov o 1
        7. funkcia - over_spravnost_cisla
        8. podmienka na kontrolu ci sa guess rovna number
            9. funkcia - over_zhody_znakov
            10. funkcia - vypis bilanciu
    11. funkcia - vypis_vysledky
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

    cislo = vygeneruj_cislo()
    
    hadane = over_spravnost_cisla()
    
    # nastavim pocitadlo cyklov
    pocitadlo = 1

    # while cyklus sa bude opakovat az kym sa hadane cislo nebude zhodovat s vygenerovanym
    while hadane != cislo:
        
        znaky_na_mieste, znaky_mimo = over_zhody_znakov(hadane, cislo)

        vypis_bilanciu(znaky_na_mieste, znaky_mimo)


        # zakazdym novym spustenim cyklu sa pocitadlo navysi o 1
        pocitadlo += 1

        hadane = over_spravnost_cisla()

 
            
    vypis_vysledky(pocitadlo)

hlavna()

