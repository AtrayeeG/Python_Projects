try:   
    d={}
    d['a']
    int("a")
except KeyError:
    print("a key error happened")
except ValueError:
    print("an exception happened.")
print("End of the program")