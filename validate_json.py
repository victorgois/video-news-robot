#!/usr/bin/env python

def main ():
    
    f= open("new_output","w+")
    prog = 'python -m json.tool < output.json' >> 'new_output.json'
    return prog
    f.write(prog)
    f.close
