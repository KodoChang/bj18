import requests
import time
import random
import hashlib
import json
import sys
import os


# key = input("请输入要翻译的内容")
key = sys.argv[1]

def get_salt(ts):  # 需要ts参数(r)
    """获取salt，js中salt：i"""
    # salt = ts + parseInt(10*Math.random(),10)
    salt = ts + str(random.randint(0, 10))
    return salt

def get_sign(key, salt):
    """获取sign"""
    # var n = e("./jquery-1.7");
    # sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
    sign = "fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
    return sign

def get_ts():
    # r = "" + (new Date).getTime()
    # ts:r
    ts = int(time.time()*1000)
    return str(ts)

# 请求url地址
post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

ts = get_ts()
salt = get_salt(ts)
sign = get_sign(key, salt)

# 构造参数
data = {
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': '53539dde41bde18f4a71bb075fcf2e66',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

# 构造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": str(len(data)),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "P_INFO=joyofs@163.com|1563967015|0|other|00&99|CN&1562044200&mail_client#CN&null#10#0#0|&0||joyofs@163.com; OUTFOX_SEARCH_USER_ID=219194725@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=538717569.5545719; JSESSIONID=aaapjRLwFIQta-h3qM7Ww; YOUDAO_MOBILE_ACCESS_TYPE=0; ___rl__test__cookies=1564388487325",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com",
    "X-Requested-With": "XMLHttpRequest"
}

r = requests.post(post_url, headers=headers, data=data)
# print(r.status_code)
data_dict = json.loads(r.content.decode())
ret = data_dict["translateResult"][0][0]["tgt"]
print(key,"翻译的结果是:", os.linesep, ret)
