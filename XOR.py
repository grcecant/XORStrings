#-----------------------
#XOR Strings Assignment
#-----------------------

#imports
import sys

#process command line arguments
def process_inputs():
    if len(sys.argv) < 3:
        sys.exit()

    #args from command line
    global human, text, key
    mode = sys.argv[1]
    if mode == 'human':
        human = True
    else:
        human = False
    text = sys.argv[2].upper()
    key = sys.argv[3].upper()
