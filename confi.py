# -*- coding:utf-8 -*-
import requests
import logging
import time
import json
from datetime import datetime
import csv
# from proxy.proxyUtil_hunbo import selectProxy


logging.basicConfig(filename="info.log",level=logging.INFO,filemode="w",format='%(asctime)s %(levelname)s %(filename)s %(thread)d %(message)s')



headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}



def get_requests(url,params={},pro=False):#r_dial
    count = 5
    while count > 0:
        # if pro:
        #     try:
        #         proxy = {"http":"http://"+selectProxy()}
        #     except Exception:
        #         # time.sleep(3)
        #         count = count - 1
        #         continue
        # else:
        #     proxy = {}
        try:
            r = requests.get(url=url,headers=headers,timeout=10,params=params)
        except Exception:
            count = count - 1
            continue
        else:
            if r.status_code != 200:
                count = count - 1
                continue
            else:
                return r
    return -1


def currenttime():
    st = time.time()
    int_time = int(st * 1000)
    return int_time


def get_time():
    now = datetime.now().strftime("%Y-%m-%d")
    return now

def get_filetime():
    now = datetime.now().strftime("%Y%m%d")
    return now


def get_json(content):
    try:
        ldix = content.find("{")
        rdix = content.rfind("}")
        con = content[ldix:rdix+1]
        rejs = json.loads(con)
    except Exception as e:
        logging.info(e)
        return -2
    else:
        return rejs


def csvwritetitle(filename,data):
    data.pop("link")
    # title = ["title","link","product","xiongjing","guanfu","high","price","minorder","total","fahuoqixian","valid","publish","update","name","email","telphone","phone","fax","local","address","content"]
    title = ["标题","产品","胸径(cm)","冠幅/品冠(cm)","高度(cm)","单价","最小起订量","供货总量","发货期限","有效期至","发布时间","最后更新","联系人","邮件","电话","手机","传真","所在地","地址","产品详细描述"]
    # title = ["标题","产品","价格要求","有效期限","发布时间","最后更新","需求数量","规格要求","包装要求","所在地","联系人","邮件","电话","手机","传真","地址","产品详细描述"]
    with open(filename,"w",encoding="utf-8-sig", newline="",errors="ignore") as f:
        writer1 = csv.writer(f)
        writer1.writerow(title)

        # if "link" in data:
        #     data.pop("link")
        rows = list(data.values())
        writer1.writerow(rows)


def csvwritetitle_buy(filename,data):
    data.pop("link")
    title = ["标题","产品","价格要求","有效期限","发布时间","最后更新","需求数量","规格要求","包装要求","所在地","联系人","邮件","电话","手机","传真","地址","产品详细描述"]
    with open(filename,"w",encoding="utf-8-sig", newline="",errors="ignore") as f:
        writer1 = csv.writer(f)
        writer1.writerow(title)

        rows = list(data.values())
        writer1.writerow(rows)


def csvwrite(filename,data):
    data.pop("link")
    with open(filename,"a+",newline="",encoding="utf-8-sig",errors="ignore") as f:
        writer = csv.writer(f)
        # if "link" in data:
        #     data.pop("link")
        rows = list(data.values())
        writer.writerow(rows)
                # print(row)
            # print(reader.line_num.line_num, row)
        # print(list(reader))


if __name__ == "__main__":
    pro = selectProxy()
    print(pro)
