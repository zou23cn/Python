import os
import json
import hashlib
import requests

# 定义变量
channeld = '201905001'   # 
appKey = '0000015ce3d1aa6f00c7962580000012'
appOrderNo = 'DD1907080002'
couponType = 'jxs002'
orderId ='2222222222'
timeStamp = '1467640240476'
count = '1'
mobile = '18601380755' #手机号

#签名
def create_sign(channeld, appKey, orderId, count, couponType, appOrderNo, timeStamp):
    sign_data = {
                'channeld': channeld,
                'appKey':appKey,
                'orderId':orderId,
                'count':count,
                'couponType':couponType,
                'appOrderNo':appOrderNo,
                'timeStamp':timeStamp
            }
    raw_str=json.dumps(sign_data, separators=(',', ':'),sort_keys=True)
    m2=hashlib.md5()
    m2.update(raw_str.encode())
    sign = m2.hexdigest()
    return sign

def outfile(out_date):
    out_file = open(r"d:\slist.txt", 'a')
    out_file.write('\n'+ out_date)


api_date = {
                'channeld': channeld,
                'orderId':orderId,
                'couponType':couponType,
                'appOrderNo':appOrderNo,
                'count':count,
                'mobile':mobile,
                'timeStamp':timeStamp, 
                'sign':create_sign(channeld, appKey, orderId, count, couponType, appOrderNo, timeStamp),
            }
api_str = json.dumps(api_date, separators=(',', ':'),sort_keys=True)

api_url = 'http://106.15.131.225/hgdz_distributor_web/couponApiService?serviceMethod=requestCodeSnForMc&&channeld=' + channeld + '&orderId=' + orderId + '&count=' + count + '&appOrderNo=' + appOrderNo + '&couponType=' + couponType + '&timeStamp=' + timeStamp + '&sign=' + create_sign(channeld, appKey, orderId, count, couponType, appOrderNo, timeStamp) + '&mobile' + mobile
r = requests.get(api_url)
print(api_url)
print(api_str)
print(r.json())
print(r.url)
outfile(api_str)



