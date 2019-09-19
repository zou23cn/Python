import os
import json
import hashlib



def create_sign(channeld, orderId, count, couponType, appOrderNo, timeStamp):
    sign_data = {
                'channeld': channeld,
                'appKey':'ebuyprovideprivatekey',
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
                'channeld': '1',
                'orderId':'2',
                'couponType':'4',
                'appOrderNo':'5',
                'count':'1',
                'mobile':'18610380755',
                'timeStamp':'6', 
                'sign':create_sign(1,2,1,4,5,6),
            }
api_str = json.dumps(api_date, separators=(',', ':'),sort_keys=True)

print(api_str)
outfile(api_str)




