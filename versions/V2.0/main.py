import itertools
import hashlib as hl
import time
import locale

locale.setlocale(locale.LC_ALL, "")  # SET COUNTRY TO USER DEFAULT


def convert(seconds):
    """CONVERT ELAPSED SECONDS IN MINUTES AND HOURS"""
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def bruteforce(selectedAlgorithm):
    """BRUTEFORCE FUNCTION FOR ALGORITHMS WITH DEFINED LENGTH"""
    characterDict = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é"'(-è_çà)=$ù*!:;,?./§%µ£¨^+²~#{[|`@]¤ €"""
    print("HASH IN : " + selectedAlgorithm)
    hashMdp = input("Enter hashed password : ").strip("'\" \n").lower()
    essais = 0
    startTime = time.time()
    rStartTime = time.strftime("%A %d %B %Y %H:%M:%S")
    for n in range(0, len(characterDict) + 1):
        for result in itertools.product(characterDict, repeat=n):
            essai = ""
            for item in result:
                essai += str(item[0])
            essais += 1
            hashEssai = getattr(hl, selectedAlgorithm)(
                bytes(essai, "utf-8")
            ).hexdigest()
            if str(hashEssai) == str(hashMdp):
                print()
                print(
                    f"Found : {essai}, in {essais} tr{'y' if essais == 1 else 'ies'}, (hash : {hashEssai} )"
                    + " " * 10
                )
                endTime = time.time()
                rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                elapsedTime = endTime - startTime
                rElapsedTime = convert(elapsedTime)
                print(
                    f"Execution time : {rElapsedTime} [H:M:S] ({elapsedTime}s) | Start : {rStartTime} | End : {rEndTime}"
                )
                exit(0)
            else:
                print(
                    f"'{essai}' ({hashEssai}) doesn't match with current hashed password, trying next...",
                    end="\r",
                )


def bruteforceLength(selectedAlgorithm):
    """BRUTEFORCE FUNCTION FOR ALGORITHMS WITH UNDEFINED LENGTH"""
    characterDict = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é"'(-è_çà)=$ù*!:;,?./§%µ£¨^+²~#{[|`@]¤ €"""
    print("HASH IN : " + selectedAlgorithm)
    hashMdp = input("Enter hashed password : ").strip("'\" \n").lower()
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
            hashEssai = getattr(hl, selectedAlgorithm)(bytes(essai, "utf-8")).hexdigest(
                longueur
            )
            if str(hashEssai) == str(hashMdp):
                print(
                    f"Found : {essai}, in {essais} tr{'y' if essais == 1 else 'ies'}, (hash : {hashEssai} )"
                    + " " * 10
                )
                endTime = time.time()
                rEndTime = time.strftime("%A %d %B %Y %H:%M:%S")
                elapsedTime = endTime - startTime
                rElapsedTime = convert(elapsedTime)
                print(
                    f"Execution time : {rElapsedTime} [H:M:S] ({elapsedTime}s) | Start : {rStartTime} | End : {rEndTime}"
                )
                exit(0)
            else:
                print(
                    f"'{essai}' ({hashEssai}) doesn't match with current hashed password, trying next...",
                    end="\r",
                )


###################### MAIN MENU ######################
def main():
    print(
        """
     _           _               _       _                _        __                           _                  _ _   _               
    | |         | |             ( )     | |              | |      / _|                         | |                (_| | | |              
    | |    _   _| | ____ _ ___  |/ ___  | |__  _ __ _   _| |_ ___| |_ ___  _ __ ___ ___    __ _| | __ _  ___  _ __ _| |_| |__  _ __ ___  
    | |   | | | | |/ / _` / __|   / __| | '_ \| '__| | | | __/ _ |  _/ _ \| '__/ __/ _ \  / _` | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \ 
    | |___| |_| |   | (_| \__ \   \__ \ | |_) | |  | |_| | ||  __| || (_) | | | (_|  __/ | (_| | | (_| | (_) | |  | | |_| | | | | | | | |
    |______\__,_|_|\_\__,_|___/   |___/ |_.__/|_|   \__,_|\__\___|_| \___/|_|  \___\___|  \__,_|_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|
                                                                                                   __/ |                                 
                                                                                                  |___/                                  

    -----------------------------------------------------------------------------------------------------------------------------------------"""
    )
    print("/!\ NEEDS TO BE OPENED IN COMMAND PROMPT OR TERMINAL /!\ ")
    print("©Lukas (https://github.com/Kalusd)")
    print(
        """Version 2.0 : Currently Supporting SHA1, SHA224, SHA256, SHA384, SHA512, MD5, SHAKE_128, SHAKE_256, BLAKE2B, BLAKE2S, SHA3_224, SHA3_256, SHA3_384 and SHA3_512
                NOT SUPPORTING (will be in future versions) : Salted hashes, Rainbow Tables and Dictionnary attacks"""
    )
    choixMenu = 0
    while choixMenu not in [1]:
        try:
            choixMenu = int(
                input(
                    "\nPlease choose an option from the following ones : \n 1 - Unsalted Hashes \n 2 - Salted Hashes \n 3 - Rainbow Tables Attacks \n 4 - Dictionnary Attacks \nEnter a number : "
                )
            )
        except ValueError:
            print("This is not a valid option")
    if choixMenu == 1:
        available_algorithms_undeflen = [
            "sha1",
            "sha224",
            "sha256",
            "sha384",
            "sha512",
            "md5",
            "blake2b",
            "blake2s",
            "sha3_224",
            "sha3_256",
            "sha3_384",
            "sha3_512",
        ]
        available_algorithms_deflen = [
            "shake_128",
            "shake_256",
        ]

        choixAlgo = 0
        while (
            0
            < choixAlgo
            < len(available_algorithms_deflen) + len(available_algorithms_undeflen) + 1
        ):
            try:
                choixAlgo = int(
                    input(
                        f"Please choose an algorithm from the following ones : \n - "
                        + "\n - ".join(
                            [
                                str(i + 1) + " : " + e.upper()
                                for i, e in enumerate(
                                    available_algorithms_undeflen
                                    + available_algorithms_deflen
                                )
                            ]
                        )
                        + " \nEnter a number : "
                    )
                )
            except ValueError:
                print("This is not a valid option")

        print("-" * 137)
        if choixAlgo - 1 < len(available_algorithms_undeflen):
            bruteforce(available_algorithms_undeflen[choixAlgo - 1])
        else:
            bruteforceLength(
                available_algorithms_deflen[
                    choixAlgo - 1 - len(available_algorithms_undeflen)
                ]
            )


if __name__ == "__main__":
    main()
