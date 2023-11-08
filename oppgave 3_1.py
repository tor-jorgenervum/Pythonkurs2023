import random

def egen_funksjon(antall_kast):
    for i in range(0, antall_kast):
        print(random.randrange(1,7))
    
egen_funksjon(12)