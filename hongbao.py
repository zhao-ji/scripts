#!/usr/bin/env python
#-*- coding: utf8 -*-

from sha import sha
from bcrypt import checkpw

PSW = "81662ff03de49cd3058f6fe95556951ad9a6f152"
SUFFIX = "twitter"
BCRYPT_PSW = "$2a$16$deGDy1I0Mf.NesPlzAWLm.aZH0znfMIxd4J65dJ4Jc3cvkYtkkr3i"

if __name__ == "__main__":
    for n in xrange(10000000, 100000000):
        plaintext = "".join([str(n), SUFFIX])
        ciphertext = sha(plaintext).hexdigest()
        if ciphertext == PSW:
            print "the origin number is {}".format(n)
            break
        if n%1000000 == 0:
            print "process {}".format(n)
