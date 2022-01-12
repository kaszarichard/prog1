import sys
try:
    file_to_test = sys.argv[1]
    source = open(file_to_test, 'r').read() + '\n'
    res = compile(source, file_to_test, 'exec')

    print("Nincs szintaktikai hiba!")
except:
    print("SyntaxError")