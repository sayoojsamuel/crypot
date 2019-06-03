low d
partial key exposure
pinhole
chosen ciphertext attack
common modulus
blinding attack
related primes
hastad broadcast
copper/wiener/LLL
Redacted
conversions between formats

close primes: https://grocid.net/2017/09/16/finding-close-prime-factorizations/
franklin reiter: f2 = (m*X + r)^e -c2

Padding oracle attacks in RSA
http://secgroup.dais.unive.it/wp-content/uploads/2012/11/Practical-Padding-Oracle-Attacks-on-RSA.html
hellman suggested
same resource for Blakenbeicher attack


Faulty Encryption
Joye and Quisquater showed how to capitalise on the common modulus weakness due to a transient error when transmitting the public key. Consider the situation where an attacker, Malory, has access to the communication channel used by Alice and Bob. In other words, Malory can listen to anything that is transmitted, and can also change what is transmitted. Alice wishes to talk privately to Bob, but does not know his public key. She requests by sending an email, to which Bob replies. But during transmission, Malory is able to see the public key and decides to flip a single bit in the public exponent of Bob, changing (e,n) to (e',n).

When Alice receives the faulty key, she encrypts the prepared message and sends it to Bob (Malory also gets it). But of course, Bob cannot decrypt it because the wrong key was used. So he lets Alice know and they agree to try again, starting with Bob re-sending his public key. This time Malory does not interfere. Alice sends the message again, this time encrypted with the correct public key.

Malory now has two ciphertexts, one encrypted with the faulty exponent and one with the correct one. She also knows both these exponents and the public modulus. Therefore she can now apply the common modulus attack to retrieve Alice's message, assuming that Alice was foolish enough to encrypt exactly the same message the second time.

A demonstation of the Common Modulus attack and the Faulty Encryption attack can be found in this Mathematica notebook.
http://www.members.tripod.com/irish_ronan/rsa/attacks.html



