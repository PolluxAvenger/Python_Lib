import sys
import colorama


while True:
    sys.stdout.write("%s\t\t\t%s %s%s\n" % (getattr(colorama.Fore, 'GREEN'), "Color Output", getattr(colorama.Fore, 'YELLOW'), "test"))
    sys.stdout.write("\n")
    sys.stdout.write("--- %s%s ------------------------------------ %s%s ---------\n" % (
        getattr(colorama.Fore, 'GREEN'), "Test 1", getattr(colorama.Fore, 'GREEN'), "Test 2"))
    sys.stdout.write("|\t%s%s : \t\t\t\t | Test 3 : \t\t |\n" % (getattr(colorama.Fore, 'CYAN'), "Test 4"))
    sys.stdout.write("-------------------------------------------------\t\t [cpu: %s%s]   |\n" % (
        getattr(colorama.Fore, 'WHITE'), "23.33%"))
    sys.stdout.flush()
