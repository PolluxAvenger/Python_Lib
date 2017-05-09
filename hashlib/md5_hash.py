# coding=utf-8

import hashlib
import zlib
# hashlib 提供 RSA，MD5，SHA1，SHA224，SHA256，SHA384，SHA512 等标准哈希算法
# zlib 提供 adler32 和 crc32 哈希

if __name__ == '__main__':
    text = b'Hello World!'
    text_md5 = hashlib.md5(text).hexdigest()
    # 要使用 md5 哈希算法，你必须传递字节串而不是普通的字符串
	print(text_md5)
	
	test_list = []
	list_sha256 = hashlib.sha256()
	list_sha256.update(repr(test_list).encode('utf-8')
    print(list_sha256.hexdigest())
