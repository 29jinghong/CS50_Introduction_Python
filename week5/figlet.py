import pyfiglet
import sys

def main():
    #print(pyfiglet.figlet_format('moo', font = 'slant'))

    #check if the input is exackly 3 value, and there is a fount in it.
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        
        #getting the font from the prevous input.
        ifont = sys.argv[2].strip()
        
        #prints the font
        print("font", ifont)

        #asking the user for input.
        ui = input("Input: ")

        #prints the input
        print("user input", ui)
    else:
        sys.exit("plese follow the following font:'figlet -f [font name]' (font example can be founded in figlet)")

    #prints to the user.
    print("Output:\n", pyfiglet.figlet_format(ui , font = ifont))

main()
