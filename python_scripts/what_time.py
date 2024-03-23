

txt = "12:34"

def what_time(t):
    arr = t.split(':')
    x = arr[0]
    y = arr[1]

    return "Jest godzina " + x + " i " + y + " minut"


wynik = what_time(txt)
    



print(wynik)
