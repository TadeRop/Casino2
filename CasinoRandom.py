#-*- coding: utf-8 -*-
import random

def main():
    secret = random.randint(0, 10)
    nadaljuj = "da"
    while nadaljuj.lower() == "da":
        guess = int(raw_input("Ugani številko:"))
        if guess == secret:
            print ("Čestitam! Zadel si jackpot!")
        else:
            print ("Več sreče prihodnjič!")
        nadaljuj = raw_input("Želiš nadaljevati igro? (da/ne)")

if __name__ == "__main__":
    main()