def find_a_string(original_str: str, substr: str) -> int:
    hossz=len(substr)
    if hossz==0:
        return 0 
    else:
        teljeshossz=len(original_str)
        valasz=0
        for i in range(teljeshossz-hossz+1):
            if substr==original_str[i:i+hossz]:
                valasz+=1
        return valasz
    


nagy = "abab"
kicsi = "a"
print(find_a_string(nagy,kicsi))
