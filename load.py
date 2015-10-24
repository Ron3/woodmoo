#coding=utf-8
'''
Created on 2015-10-23

@author: lamter
'''

from encrypt import *
from zipdata import ZipData


# 块长度
BLOCK_SIZE = 1024

def loadInt32(_socket):
    """
    以 int32 来解包数据
    :return: json
    """
    _json = ''

    ''' 获取长度 '''

    d = _socket.recv(4)

    ''' 获得数据长度 '''
    length = getDataLength(d)

    if length == 0:
        return _json

    ''' 接受完数据 '''
    buffers = ''
    while length > 0:
        if length >= BLOCK_SIZE:
            s = BLOCK_SIZE
        else:
            s = length

        buff = _socket.recv(s)
        buffers += buff
        length -= len(buff)

    ''' 解密 '''
    cryptData = BPAES.aes128_decrypt(buffers)

    unzipData = BPZipData.unzip_data(cryptData)

    ''' 解析json '''
    data = json.loads(unzipData)

    #print "data->", data
    return data


from struct import pack, unpack
STRUCT_FORMAT = "!I"

def getDataLength(d):
    if d:
        length, = unpack(STRUCT_FORMAT, d)
        return length
    else:
        return 0