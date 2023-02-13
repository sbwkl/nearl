import requests
import json
from datetime import datetime

def main():
    with open('indexInfo.json', 'r', encoding='UTF-8') as f:
        indexInfo = json.loads(f.read())

    # index_list = ['000001', '000300', '000905', '000991', '399989', '000993', '000990', '000852', '399967']
    item_list = []
    for index in indexInfo:
    # for index in index_list:
        try:
            res = requests.get('https://www.csindex.com.cn/csindex-home/perf/index-perf-oneday?indexCode=' + index.get('code'))
            intra_day = res.json().get('data', {}).get('intraDayHeader', {})
            if 'indexCode' not in intra_day:
                intra_day['indexCode'] = index.get('code')
            item_list.append(intra_day)
        except Exception as e:
            pass
    index_data = {
        'gmtModified': int(datetime.now().timestamp()),
        'itemList': item_list
    }
    with open('indexData.json', 'w') as f:
        f.write(json.dumps(index_data))

if __name__ == '__main__':
    main()