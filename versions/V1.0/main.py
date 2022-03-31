import itertools
import hashlib as hl
import time

###################### BRUTEFORCE WITH DIFFERENT ALGORITHMS ######################
##### SHA256
def bruteforceSHA256():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€"]
    print("HASH IN SHA256")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha256(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")

##### SHA512
def bruteforceSHA512():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€"]
    print("HASH IN SHA512")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha512(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")

##### SHA384
def bruteforceSHA384():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€"]
    print("HASH IN SHA384")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha384(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")

##### MD5
def bruteforceMD5():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€"]
    print("HASH IN MD5")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.md5(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    print(f'Execution time : {elapsedTime:.2}s' + " Start : "+ str(startTime) + ", End : " + str(endTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")



###################### ALGORITHM SELECTION MENU ######################

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
print("©Lukas (https://github.com/Kalusd)")
print("/!\ NEEDS TO BE OPENED IN COMMAND PROMPT / TERMINAL /!\ ")
print("Version 1.0 : Currently Supporting SHA256, SHA384, SHA512 and MD5 | NOT SUPPORTING (will be in future versions) : Salted hashes, Rainbow Tables, Dictionnary attacks")
choixAlgo = int(input("Please choose an algorithm from the following ones : \n 1 - SHA256 \n 2 - SHA384 \n 3 - SHA512 \n 4 - MD5 \nEnter a number : "))
if choixAlgo == 1:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA256()
elif choixAlgo == 2:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA384()
elif choixAlgo == 3:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA512()
elif choixAlgo == 4:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceMD5()
else:
    print("Unrecognised number, please try again")
