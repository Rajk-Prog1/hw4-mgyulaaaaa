def minion_game(s: str) -> str:
    kevin=0
    stuart=0
    hossz=len(s)
    vowels='AEIOUY'
    for i in range(hossz):
        if s[i] in vowels:
            kevin = kevin+hossz-i      #geci ez 10 ev volt mire rajottem hogy csak ennyit kell osszeadni
        else:
            stuart=stuart+hossz-i
    if stuart==kevin:
        return 'Draw'
    if stuart<kevin:
        return(f'Kevin {kevin}')
    if kevin<stuart:
        return(f'Stuart {stuart}')
        

    return(stuart)
    pass


print(minion_game('FASZASEGG'))