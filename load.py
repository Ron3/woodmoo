#coding=utf-8
'''
Created on 2015-10-23

@author: lamter
'''

import zlib
from encrypt import *
from intn import getDataLength

# 块长度
BLOCK_SIZE = 1024

def loadInt32(AES_KEY, _socket):
    """
    以 int32 来解包数据
    :return: json
    """
    # 获取长度
    d = _socket.recv(4)

    # 获得数据长度
    length = getDataLength(d)

    if length == 0:
        return ''

    # 接受完数据
    cryptData = ''
    while length > 0:
        if length >= BLOCK_SIZE:
            s = BLOCK_SIZE
        else:
            s = length

        buff = _socket.recv(s)
        cryptData += buff
        length -= len(buff)

    # 解密
    decryptData = aes128_decrypt(AES_KEY, cryptData)
    # 解压
    unzipData = zlib.decompress(decryptData)

    return unzipData

