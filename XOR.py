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
    global mode
    mode = sys.argv[1]
    keyfile = sys.argv[2]
    inpfile = sys.argv[3]

    global key, inp
    key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
    inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
    debug = False
    if(debug):
        print("mode:"+mode)
        print("key: "+key)
        print("inp: "+inp)

#part 1: human readable mode
def human():
    return_string = ''
    counter = 0
    for i in inp:
        inp_ord = ord(i)
        key_ord = ord(key[counter])
        return_string += chr(inp_ord^key_ord)
        counter = (counter + 1) % len(key)
    return return_string

#part 2: number output mode
def numOut():
    return_string = ''
    counter = 0
    for i in inp:
        inp_ord = ord(i)
        key_ord = ord(key[counter])
        return_string += hex(inp_ord^key_ord)
        return_string += ' '
        counter = (counter + 1) % len(key)
    return return_string

if __name__ == '__main__':
    process_inputs()
    if mode == 'human':
        print(human())
    else:
        print(numOut())
