#usr/bin/python2.7
import time
import itertools, string

info = """
                   ====================================================================================================
                   ====================================================================================================
                   ===           Name            : Python Wordlist Generator v0.2                                   ===
                   ===           Created By      : AKHADE VAIJINATH KACHRU (Macaish)                                ===
                   ===           Blog            : vaijinathakhade.blogspot.com                                     ===
                   ===           Documentation   : https://github.com/themacaish/Python-Wordlist-Generator/         ===
                   ===           License         : GNU GENERAL PUBLIC LICENSE Version 3, February 2019              ===
                   ===           Thanks to       : SHEETHAL NAAGAR (Macaish2)                                       ===
                   ====================================================================================================
                   ====================================================================================================
                                       ===    __  __    _    ____    _    ___ ____  _   _    ===
                                       ===   |  \/  |  / \  / ___|  / \  |_ _/ ___|| | | |   ===
                                       ===   | |\/| | / _ \| |     / _ \  | |\___ \| |_| |   ===
                                       ===   | |  | |/ ___ \ |___ / ___ \ | | ___) |  _  |   ===
                                       ===   |_|  |_/_/   \_\____/_/   \_\___|____/|_| |_|   ===
                                       =========================================================      
                                       =========================================================            
"""

def _createWordlist(output, chrs, min_length, max_length):
    if min_length > max_length:
        print "[!] Please min_length must smaller or same as with max_length"

    output = open(output, 'w')
    
    print "[+] Creating wordlist at { %s } ..." % str(output).split("'")[1]
    print "[+] Start Time: ", time.strftime('%H:%M:%S')
    
    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            saved = ''.join(xs)
            output.write("%s\n" % saved)
    output.close()
    print "[-] End Time: ", time.strftime('%H:%M:%S')

def _minLength():
    return input("[+] Type your min_length, (ex: 1): ")
                 
def _maxLength():
    return input("[+] Type your max_length, (ex: 3): ")

def _output():
    return raw_input("[+] Type your output for wordlist, (ex: wordlist.txt): ")

def main():
    print info
    inp_usr = raw_input(" 1. Real Complete Characters\n 2. Complete Chars from Input\n[+] Type your choice: ")
    
    if inp_usr == '1':
        output = _output()
        chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
        return _createWordlist(output, chrs, _minLength(), _maxLength())

    elif inp_usr == '2':
        output = _output()
        chrs = raw_input("[+] Type your option characters, (ex: abc): ")
        return _createWordlist(output, chrs, _minLength(), _maxLength())
    else:
        print "[!] WTF U, Please choice correct options!!"

if __name__ == "__main__":
    main()
