import inflect

grammar = inflect.engine()

def main():
    #Adieu, adieu, to Liesl, Friedrich, and Louisa
    names = []
    while True:
        print("type control-c to exit")
        try:
            name = input("enter your name: ").strip().title()
        except KeyboardInterrupt:
            print()
            print("Done")
            break
        names.append(name)

    print("Adieu, adieu, to", grammar.join(names))
    
main()
