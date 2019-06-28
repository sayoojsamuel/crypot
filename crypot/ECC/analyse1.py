#!/usr/bin/env sage
from smarts.smart import smarts_attack

class ECCanalyse(object):
    def __init__(self, P, Q=None):
        self.P = P
        self.Q = Q
    
    def analyse(self):
        if self.P and self.Q:
            if self.P.curve()==self.Q.curve():
                print "[+] The Curve of the points are ",self.P.curve()
                if self.P.order() == self.P.curve().base_field().cardinality():
                    print "Vulnerable to Smarts Attack..."
                    print "The ECDLP is solved, the secret is:" ,smarts_attack(self.P.curve(),self.P,self.Q)
                    return
                else:
                    print "Trying to solve DLP..."
                    print "The ECDLP is solved, the secret is:" ,self.P.discrete_log(self.Q)
                    return

            else:
                print "P and Q are from different curves"
                return 
        else:
            print "[+] The Curve of the point is", self.P.curve()






















