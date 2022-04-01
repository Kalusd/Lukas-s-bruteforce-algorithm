import itertools
import hashlib as hl
import time
import locale

locale.setlocale(locale.LC_ALL, '') #SET COUNTRY TO USER DEFAULT

def convert(seconds):               #CONVERT ELAPSED SECONDS IN MINUTES AND HOURS
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def bruteforce():                   #BRUTEFORCE FUNCTION FOR ALGORITHMS WITH DEFINED LENGTH
    characterDict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN : " + selectedAlgorithm)
    hashMdp = input("Enter hashed password : ")
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(characterDict) + 1):
        for result in itertools.product(characterDict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essais += 1
            hashEssai = getattr(hl, selectedAlgorithm)(bytes(essai, 'utf-8')).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    exit(0)
                else:
                    print("Found : "+ str(essai) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    exit(0)
            else:
                print("'" + str(essai) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")

def bruteforceLength():                   #BRUTEFORCE FUNCTION FOR ALGORITHMS WITH UNDEFINED LENGTH
    characterDict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN : " + selectedAlgorithm)
    hashMdp = input("Enter hashed password : ")
    longueur = int(input("Enter hash length in bytes : "))
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(characterDict) + 1):
        for result in itertools.product(characterDict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essais += 1
            hashEssai = getattr(hl, selectedAlgorithm)(bytes(essai, 'utf-8')).hexdigest(longueur)
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    exit(0)
                else:
                    print("Found : "+ str(essai) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    exit(0)
            else:
                print("'" + str(essai) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")




###################### MAIN MENU ######################

print("""
  _           _               _       _                _        __                           _                  _ _   _               
 | |         | |             ( )     | |              | |      / _|                         | |                (_| | | |              
 | |    _   _| | ____ _ ___  |/ ___  | |__  _ __ _   _| |_ ___| |_ ___  _ __ ___ ___    __ _| | __ _  ___  _ __ _| |_| |__  _ __ ___  
 | |   | | | | |/ / _` / __|   / __| | '_ \| '__| | | | __/ _ |  _/ _ \| '__/ __/ _ \  / _` | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \ 
 | |___| |_| |   | (_| \__ \   \__ \ | |_) | |  | |_| | ||  __| || (_) | | | (_|  __/ | (_| | | (_| | (_) | |  | | |_| | | | | | | | |
 |______\__,_|_|\_\__,_|___/   |___/ |_.__/|_|   \__,_|\__\___|_| \___/|_|  \___\___|  \__,_|_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|
                                                                                                __/ |                                 
                                                                                               |___/                                  

-----------------------------------------------------------------------------------------------------------------------------------------""")
print("/!\ NEEDS TO BE OPENED IN COMMAND PROMPT OR TERMINAL /!\ ")
print("©Lukas (https://github.com/Kalusd)")
print("""Version 1.1 : Currently Supporting SHA1, SHA224, SHA256, SHA384, SHA512, MD5, SHAKE_128, SHAKE_256, BLAKE2B, BLAKE2S, SHA3_224, SHA3_256, SHA3_384 and SHA3_512
              NOT SUPPORTING (will be in future versions) : Salted hashes, Rainbow Tables and characterDict
    tionnary attacks""")
choixMenu = int(input("\nPlease choose an option from the following ones : \n 1 - Unsalted Hashes \n 2 - Salted Hashes \n 3 - Rainbow Tables Attacks \n 4 - characterDitionnaty Attacks \nEnter a number : "))
if choixMenu == 1:
    choixAlgo = int(input("Please choose an algorithm from the following ones : \n 1 - SHA1 \n 2 - SHA224 \n 3 - SHA256 \n 4 - SHA384 \n 5 - SHA512 \n 6 - MD5 \n 7 - SHAKE_128 \n 8 - SHAKE_256 \n 9 - BLAKE2B \n 10 - BLAKE2S \n 11 - SHA3_224 \n 12 - SHA3_256 \n 13 - SHA3_384 \n 14 - SHA3_512 \nEnter a number : "))
    if choixAlgo == 1:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha1"
        bruteforce()
    elif choixAlgo == 2:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha224"
        bruteforce()
    elif choixAlgo == 3:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha256"
        bruteforce()
    elif choixAlgo == 4:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha384"
        bruteforce()
    elif choixAlgo == 5:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha512"
        bruteforce()
    elif choixAlgo == 6:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "md5"
        bruteforce()
    elif choixAlgo == 7:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "shake_128"
        bruteforceLength()
    elif choixAlgo == 8:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "shake_256"
        bruteforceLength()
    elif choixAlgo == 9:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "blake2b"
        bruteforce()
    elif choixAlgo == 10:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "blake2s"
        bruteforce()
    elif choixAlgo == 11:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha3_224"
        bruteforce()
    elif choixAlgo == 12:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha3_256"
        bruteforce()
    elif choixAlgo == 13:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha3_384"
        bruteforce()
    elif choixAlgo == 14:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        selectedAlgorithm = "sha3_512"
        bruteforce()
    else:
        print("Unrecognised number, please try again")
