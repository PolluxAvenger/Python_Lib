# coding=utf-8

import unicorn

if __name__ == "__main__":
    # code to be emulated
	# INC ecx; DEC edx
    X86_CODE32 = b'\x41\x4a' 

    # memory address where emulation starts
    ADDRESS = 0x1000000

    print('Emulate i386 code')

    try:
        # Initialize emulator in X86-32bit mode
        mu = unicorn.Uc(unicorn.UC_ARCH_X86, unicorn.UC_MODE_32)
        # map 2MB memory for this emulation
        mu.mem_map(ADDRESS, 2 * 1024 * 1024)
        # write machine code to be emulated to memory
        mu.mem_write(ADDRESS, X86_CODE32)
        # initialize machine registers
        mu.reg_write(unicorn.x86_const.UC_X86_REG_ECX, 0x1234)
        mu.reg_write(unicorn.x86_const.UC_X86_REG_EDX, 0x7890)
        # emulate code in infinite time & unlimited instructions
        mu.emu_start(ADDRESS, ADDRESS + len(X86_CODE32))
        # now print out some registers
        print('Emulation done.\nBelow is the CPU context:')

        r_ecx = mu.reg_read(unicorn.x86_const.UC_X86_REG_ECX)
        r_edx = mu.reg_read(unicorn.x86_const.UC_X86_REG_EDX)

        print(">>> ECX = 0x%x" % r_ecx)
        print(">>> EDX = 0x%x" % r_edx)
    except unicorn.UcError as e:
        print("ERROR: %s" % e)
