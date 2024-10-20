def swap_case(s: str) -> int:
    kicsik='qwertzuiopasdfghjklyxcvbnm'
    nagyok='QWERTZUIOPASDFGHJKLYXCVBNM'
    hossz=len(s)
    valasz=list(range(hossz))
    for i in range(hossz):
        if s[i].isupper():
            valasz[i]=s[i].lower()
        elif s[i].islower():
            valasz[i]=s[i].upper()
        else:
            valasz[i]=s[i]
    valasz="".join(valasz)

    return(valasz)
    pass


print(swap_case("akki"))