# coding=utf-8

import capstone

if __name__ == "__main__":
    CODE = b'\x55\x48\x8b\x05\xb8\x13\x00\x00'
    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)

    for item in md.disasm(CODE, 0x1000):
        print("0x%x:\t%s\t%s" % (item.address, item.mnemonic, item.op_str))
