import requests
import sys

url = sys.argv[1]
dic = sys.argv[2]
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '}
with open(dic, 'r') as f:   # r->read 读操作  w->write 写操作（覆盖原文本） a->add 追加
    for line in f.readlines():
        line = line.strip()
        r = requests.get(url+line)
        if r.status_code == 200:
            print("url:"+r.url+" exist")
