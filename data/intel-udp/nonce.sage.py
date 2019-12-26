
# This file was *autogenerated* from the file nonce.sage
from sage.all_cmdline import *   # import sage library

_sage_const_12982511241385771099689470326654774263894697667703711753598098427526832214082 = Integer(12982511241385771099689470326654774263894697667703711753598098427526832214082); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_85034076815184974961739170239653072089442086308599627559489680731885713194115 = Integer(85034076815184974961739170239653072089442086308599627559489680731885713194115); _sage_const_257 = Integer(257); _sage_const_4 = Integer(4); _sage_const_256 = Integer(256); _sage_const_8 = Integer(8); _sage_const_0xb39eaeb437e33087132f01c2abc60c6a16904ee3771cd7b0d622d01061b40729 = Integer(0xb39eaeb437e33087132f01c2abc60c6a16904ee3771cd7b0d622d01061b40729); _sage_const_12 = Integer(12); _sage_const_16 = Integer(16); _sage_const_106058005610142779690166437300572023785265939629722543453418132696315520505889 = Integer(106058005610142779690166437300572023785265939629722543453418132696315520505889); _sage_const_50 = Integer(50)
noisy_local_key = _sage_const_12982511241385771099689470326654774263894697667703711753598098427526832214082 
modulo = Integer(115792089210356248762697446949407573529996955224135760342422259061068512044369L)
digest = Integer(_sage_const_0xb39eaeb437e33087132f01c2abc60c6a16904ee3771cd7b0d622d01061b40729 )
inf_real_key = _sage_const_85034076815184974961739170239653072089442086308599627559489680731885713194115 
remoteUDP_key = _sage_const_106058005610142779690166437300572023785265939629722543453418132696315520505889 


key = Integer(remoteUDP_key)


def load_samples(l=_sage_const_4 ):
    ocounter = _sage_const_0 
    lines=_sage_const_0 

    with open("sigpairs%d.txt" % l, "r") as f:
        for line in f:
            a = line.split()
            t = tuple([int(x,_sage_const_16 ) for x in a])
            r,s = t
            nonce = lift(mod((digest+key*Integer(r))*inverse_mod(s,modulo), modulo))
            #twelve = (lift(nonce)-lift(mod(nonce,2^(256-12))))//2^(256-12)
            #eight = (lift(nonce)-lift(mod(nonce,2^(256-8))))//2^(256-8)
            #four  = (lift(nonce)-lift(mod(nonce,2^(256-4))))//2^(256-4)
            four = nonce//_sage_const_2 **(_sage_const_256 -_sage_const_4 )
            eight = nonce//_sage_const_2 **(_sage_const_256 -_sage_const_8 )
            twelve = nonce//_sage_const_2 **(_sage_const_256 -_sage_const_12 )
            ocounter += nonce//_sage_const_2 **(_sage_const_256 -_sage_const_1 )
            print four, eight, twelve, "0x"+hex(r), " 0x"+hex(s)
            print bin(nonce + _sage_const_2 **_sage_const_257 )[_sage_const_4 :_sage_const_50 ]
            lines = lines + _sage_const_1 
            print ocounter, lines,float(ocounter)/float(lines)


load_samples(_sage_const_12 )
