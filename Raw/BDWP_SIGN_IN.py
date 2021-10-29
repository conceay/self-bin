# -*- coding: utf8 -*-
#  可以抽到超级会员月卡，优惠券，积分
import requests

#serverkey 为 Server酱SCKEY或酷推的SKEY
serverkey = 'SCT56378Tz8O3A2J3XcW3TuHANhzNuao1'
#百度网盘官网，登录进去
cookie = 'BAIDUID=43B395E0D3E474B44CCDB7F5369813C4:FG=1; BAIDUCUID=_PHfu0iZSa0d8v8bgP2qi_uSSa_9ivuYguSU8gucvi_XivilYuHQu_85SRruiSuMyzImA; BDPP_NDID=fbpxuy6C_bufa9KwdEf6SUHT2G_mAckOzX9Y5GZopXuizZ1cwenHO0V5k; BDUSS=Ztc1pveFlZR2lzfnhsRzFKbVl5cnNiMFRNS3p-TXN4cld6OHAtRFlsS3FSODlnRUFBQUFBJCQAAAAAAAAAAAEAAAAYQhBcRHJlyM7Q1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKq6p2Cquqdgcz; SG_FW_VER=1.26.3; SP_FW_VER=3.230.38'
#pushType：0Service酱推送；pushType：1酷推推送
pushType = 1

def pushMessage(key,desp):
    url =''
    if pushType == 1:
        url = f'https://push.xuthus.cc/wx/{key}?c={desp}'
    elif pushType == 0:
        url = f'https://sc.ftqq.com/{key}.send?text=百度网盘执行结果&desp={desp}'
    requests.get(url)    

def baiduwangpan(serverkey, cookie):
    desp = '【百度网盘】\n刮一刮结果：'
    url = 'https://pan.baidu.com/act/celebrationday/lotterycommit?clienttype=1&channel=android_10_ELE-AL00_bd-netdisk_1001192h&tid=973681592908'
    headers = {
            'Cookie': cookie,
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }
    response = requests.get(url, headers=headers)
    if response.json()['errno'] == 0:
       desp += response.json()['data']['gift_info']['title']
    elif response.json()['errno'] == 1024:
        desp += response.json()['errmsg']
    elif response.json()['errno'] == 1003:#未登录
        desp += response.json()['errmsg']
    print(desp)
    pushMessage(serverkey,desp)

def main_handler(event, context):
    baiduwangpan(serverkey, cookie)

if __name__ == '__main__':
    baiduwangpan(serverkey, cookie)

