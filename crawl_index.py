import requests
import json

def main():
    index_list = ['000001', '000300', '000905', '000991', '399989', '000993', '000990', '000852', '399967']
    index_data = []
    for index in index_list:
        res = requests.get('https://www.csindex.com.cn/csindex-home/perf/index-perf-oneday?indexCode=' + index)
        val = res.json().get('data', {}).get('intraDayHeader').get('current')
        print(index, val)
        index_data.append({
            'code': index,
            'value': val
        })
    with open('indexData.json', 'w') as f:
        f.write(json.dumps(index_data))


if __name__ == '__main__':
    main()