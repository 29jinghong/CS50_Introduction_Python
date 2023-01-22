import inflect

grammar = inflect.engine()

def main():
    #Adieu, adieu, to Liesl, Friedrich, and Louisa
    names = []
    while True:
        print("type quit to exit")
        name = input("enter your name: ").strip().title()
        if name == "Quit":
            break
        names.append(name)
    
    print("Adieu, adieu, to", grammar.join(names))
    
main()
