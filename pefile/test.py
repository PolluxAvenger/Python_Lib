# coding=utf-8

import pefile

PEfile_Path = "RegexTester.exe"
pe = pefile.PE(PEfile_Path)


if __name__ == "__main__":
    # PE 文件全解析
    print(pe)
    # 入口点
    print(hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
    # 每个节表
    for section in pe.sections:
        print(str(section.Name), hex(section.VirtualAddress), hex(section.Misc_VirtualSize), section.SizeOfRawData)
    # 改写数据
    pe.OPTIONAL_HEADER.AddressOfEntryPoint = 0x5555
    pe.write(filename='handler.exe')
