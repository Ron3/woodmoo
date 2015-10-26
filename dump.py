#coding=utf-8
'''
Created on 2015-10-23

@author: lamter
'''

import zlib
from encrypt import *
from intn import int32Head


def dumpInt32(_json, AES_KEY):
    """
    压缩加密
    :param _json:
    :param AES_KEY:
    :return:
    """

    # 加压
    zipData = zlib.compress(_json, 6)

    # 加密
    encryptData = aes128_encrypt(AES_KEY, zipData)

    # Int32位
    int32Data = int32Head(encryptData) + encryptData

    return int32Data

def foo():
    pass