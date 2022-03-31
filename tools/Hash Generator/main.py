import hashlib as hl

mdp = input("Enter the password to hash : ").encode('utf-8')
print("Algorithms availables : \n 1 - SHA1 \n 2 - SHA224 \n 3 - SHA256 \n 4 - SHA384 \n 5 - SHA512 \n 6 - MD5 \n 7 - SHAKE_128 \n 8 - SHAKE_256 \n 9 - BLAKE2B \n 10 - BLAKE2S \n 11 - SHA3_224 \n 12 - SHA3_256 \n 13 - SHA3_384 \n 14 - SHA3_512 ")
choix = int(input("Please choose an algorithms from the following ones : "))
if choix == 1:
    print("Hash : " + hl.sha1(mdp).hexdigest())
elif choix == 2:
    print("Hash : " + hl.sha224(mdp).hexdigest())
elif choix == 3:
    print("Hash : " + hl.sha256(mdp).hexdigest())
elif choix == 4:
    print("Hash : " + hl.sha384(mdp).hexdigest())
elif choix == 5:
    print("Hash : " + hl.sha512(mdp).hexdigest())
elif choix == 6:
    print("Hash : " + hl.md5(mdp).hexdigest())
elif choix == 7:
    longueur = int(input("Length of the hash (bytes) : "))
    print("Hash : " + hl.shake_128(mdp).hexdigest(longueur))
elif choix == 8:
    longueur = int(input("Length of the hash (bytes) : "))
    print("Hash : " + hl.shake_256(mdp).hexdigest(longueur))
elif choix == 9:
    print("Hash : " + hl.blake2b(mdp).hexdigest())
elif choix == 10:
    print("Hash : " + hl.blake2s(mdp).hexdigest())
elif choix == 11:
    print("Hash : " + hl.sha3_224(mdp).hexdigest())
elif choix == 12:
    print("Hash : " + hl.sha3_256(mdp).hexdigest())
elif choix == 13:
    print("Hash : " + hl.sha3_384(mdp).hexdigest())
elif choix == 14:
    print("Hash : " + hl.sha3_512(mdp).hexdigest())
else:
    print("Unrecognised number...")
