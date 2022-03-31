import itertools
import hashlib as hl
import time
import locale

locale.setlocale(locale.LC_ALL, '') #SET COUNTRY TO USER DEFAULT

def convert(seconds):               #CONVERT ELAPSED SECONDS IN MINUTES AND HOURS
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

###################### BRUTEFORCE WITH DIFFERENT ALGORITHMS ######################
##### SHA256
def bruteforceSHA256():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA256")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
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
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
##### SHA512
def bruteforceSHA512():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA512")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
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
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
##### SHA384
def bruteforceSHA384():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA384")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
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
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
##### MD5
def bruteforceMD5():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN MD5")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
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
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHAKE_256
def bruteforceSHAKE_256():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHAKE_256")
    hashMdp = input("Enter hashed password : ")
    longueur = int(input("Enter hash length in bytes : "))
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.shake_256(essai).hexdigest(longueur)
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHAKE_128
def bruteforceSHAKE_128():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHAKE_128")
    hashMdp = input("Enter hashed password : ")
    longueur = int(input("Enter hash length in bytes : "))
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.shake_128(essai).hexdigest(longueur)
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHA1
def bruteforceSHA1():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA1")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha1(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHA224
def bruteforceSHA224():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA224")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha224(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####BLAKE2B
def bruteforceBLAKE2B():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN BLAKE2B")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.blake2b(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####BLAKE2S
def bruteforceBLAKE2S():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN BLAKE2S")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.blake2s(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHA3_224
def bruteforceSHA3_224():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA3_224")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha3_224(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHA3_256
def bruteforceSHA3_256():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA3_256")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha3_256(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHA3_384
def bruteforceSHA3_384():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA3_384")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha3_384(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
#####SHA3_512
def bruteforceSHA3_512():
    dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "$", "ù", "*", "!", ":", ";", ",", "?", ".", "/", "§", "%", "µ", "£", "¨", "^", "+", "²", "~", "#", "{", "[", "|", "`", "@", "]", "¤", "€", " "]
    print("HASH IN SHA3_512")
    hashMdp = input("Enter hashed password : ")
    trouvé = False
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(dict) + 1):
        for result in itertools.product(dict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essai = essai.encode('utf-8')
            essais += 1
            hashEssai = hl.sha3_512(essai).hexdigest()
            if str(hashEssai) == str(hashMdp):
                if essais == 1:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " try" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) + ' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
                else:
                    print("Found : "+ str(essai.decode('utf-8')) + ", in "+ str(essais) + " tries" + ", (hash : " + str(hashEssai) + " )")
                    endTime = time.time()
                    rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                    elapsedTime = endTime - startTime
                    rElapsedTime = convert(elapsedTime)
                    print('Execution time : ' + str(rElapsedTime) +' [H:M:S] (' + str(elapsedTime) +' s)' + " | Start : "+ str(rStartTime) + " | End : " + str(rEndTime))
                    trouvé = True
                    exit(0)
            else:
                print("'" + str(essai.decode('utf-8')) + "'" + " (" + str(hashEssai) + ")" + " doesn't match with current hashed password, trying next...")
    input("Press a key to exit...")
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
print("/!\ NEEDS TO BE OPENED IN COMMAND PROMPT / TERMINAL /!\ ")
print("©Lukas (https://github.com/Kalusd)")
print("""Version 1.1 : Currently Supporting SHA1, SHA224, SHA256, SHA384, SHA512, MD5, SHAKE_128, SHAKE_256, BLAKE2B, BLAKE2S, SHA3_224, SHA3_256, SHA3_384 and SHA3_512
              NOT SUPPORTING (will be in future versions) : Salted hashes, Rainbow Tables, Dictionnary attacks""")
choixAlgo = int(input("Please choose an algorithm from the following ones : \n 1 - SHA1 \n 2 - SHA224 \n 3 - SHA256 \n 4 - SHA384 \n 5 - SHA512 \n 6 - MD5 \n 7 - SHAKE_128 \n 8 - SHAKE_256 \n 9 - BLAKE2B \n 10 - BLAKE2S \n 11 - SHA3_224 \n 12 - SHA3_256 \n 13 - SHA3_384 \n 14 - SHA3_512 \nEnter a number : "))
if choixAlgo == 1:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA1()
elif choixAlgo == 2:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA224()
elif choixAlgo == 3:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA256()
elif choixAlgo == 4:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA384()
elif choixAlgo == 5:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA512()
elif choixAlgo == 6:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceMD5()
elif choixAlgo == 7:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHAKE_128()
elif choixAlgo == 8:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHAKE_256()
elif choixAlgo == 9:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceBLAKE2B()
elif choixAlgo == 10:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceBLAKE2S()
elif choixAlgo == 11:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA3_224()
elif choixAlgo == 12:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA3_256()
elif choixAlgo == 13:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA3_384()
elif choixAlgo == 14:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    bruteforceSHA3_512()
else:
    print("Unrecognised number, please try again")
