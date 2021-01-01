# -*- coding: utf-8 -*-
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import sys
import os
import time
import subprocess

from .jd_logger import logger

#-----------默认配置-----------
# accessKey和secretkey是七牛的秘钥
access_key = 'Ocs7PPLPFuf8mJ6CCqugqiE6-BuGEXAU__mZQpBi'
secret_key = 'LvXODUTYGSsyaj9lIZvw1xG_1PlVLKZ08duG9YRA'
# 存储空间
bucket_name = 'jd-login-qr'
# 域名
bucket_url = 'http://qm9ua9rea.hn-bkt.clouddn.com/'

# 格式
img_suffix = ["jpg", "jpeg", "png", "bmp", "gif"]


class QiniuTool(object):
    def __init__(self):
        self.newName = str(int(time.time()*1000)) + ".png"

    #上传文件到七牛, 返回链接地址
    def upload_data(self, localfilePath):
        #logger.info("{}, {}", self.newName, localfilePath)
        q = Auth(access_key, secret_key)
        # 上传到七牛后保存的文件名
        key = self.newName;
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        # 要上传文件的本地路径
        localfile = localfilePath
        ret, info = put_file(token, key, localfile)
        return bucket_url + key


    def crateFile(self, dataList):
        with open(result_file, 'w+') as f:
            for data in dataList:
                # 如果是图片则生成图片的markdown格式引用
                if os.path.splitext(data)[1][1:] in img_suffix:
                    f.write('![]('+data+')'+'\n')

        f.close()


