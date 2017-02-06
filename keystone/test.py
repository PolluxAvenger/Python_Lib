# encoding: utf-8

import keystone

if __name__ == "__main__":
    CODE = b'INC ecx; DEC edx'

    try:
        # Initialize engine in X86-32bit mode
        ks = keystone.Ks(keystone.KS_ARCH_X86, keystone.KS_MODE_32)
        encoding, count = ks.asm(CODE)
        print("%s = %s (number of statements: %u)" % (CODE, encoding, count))
    except keystone.KsError as e:
        print("ERROR: %s" % e)
