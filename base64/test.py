# coding=utf-8

import base64

initial_data = b'This is a test fot base64 encoding.'
encoded_data = base64.b64encode(initial_data)
num_initial = len(initial_data)
padding = {0: 0, 1: 2, 2: 1}[num_initial % 3]
decoded_data = base64.b64decode(encoded_data)

print('编码前为 %d 字节' % num_initial)
print('编码前为 %s' % initial_data)
print('填充了 %d 个字节（不够8bit要自动补0，使二进制序列的长度成为24的倍数(6和8的最小公倍数)）' % padding)
print('编码后为 %d 字节' % len(encoded_data))
print('编码后为:', encoded_data)
print('解码后为:', decoded_data)

print('在 URL 编码中，+ 要由-来代替，_ 要代替/，其他字母表还是相同')
for original in [ b'\xfb\xef', b'\xff\xff' ]:
    print('原始字符串:', repr(original))
    print('标准方式编码后为:', base64.standard_b64encode(original))
    print('URL 编码后为:', base64.urlsafe_b64encode(original))

original_string = b'This is a test fot base32 encoding.'
encoded_string = base64.b32encode(original_string)
decoded_string = base64.b32decode(encoded_string)
print('原始字符串:', original_string)
print('编码后为:', encoded_string)
print('解码后为:', decoded_string)
