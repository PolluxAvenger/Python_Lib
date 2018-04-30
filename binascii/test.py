import binascii

text = 'Test'

# 得到十六进制
hex_text = hexlify(text)
print hex_text

# 十六进制反向转换为二进制数据
unhex_text = unhexlify(hex_text)
print unhex_text
