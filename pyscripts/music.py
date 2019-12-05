#!/Users/newtorn/.pyenv/shims/python3

STYPES = ('kugou', 'netease', 'qq', 'kuwo', 'xiami', 'baidu', '1ting', 'migu', 'lizhi', 'qingting', 'ximalaya', 'kg', '5singyc', '5singfc')
SFILTERS = ('name', 'id', 'url')

def search(stype='kugou', sinput='You Need To Calm Down', sfilter='name'):
    '''Search music from http://www.youtap.xin/'''
    import requests

    url = 'http://www.youtap.xin/'
    data = {
        'input': sinput,
        'filter': sfilter,
        'type': stype,
        'page': '1'
    }
    headers = {
        'Host': 'www.youtap.xin',
        'Origin': 'http://www.youtap.xin',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    resp = requests.post(url=url, data=data, headers=headers)
    resp = resp.json()
    return resp.get('data', [])


def save(music, file='../source/_data/musics.json'):
    import json
    with open(file, 'r') as f:
        data = f.read()
        try:
            data = json.loads(data)
        except:
            data = []
    data.append(music)
    data = json.dumps(data, indent=4)
    with open(file, 'w') as f:
        f.write(data)


def main():
    import sys
    args = sys.argv[1:]

    sname = None
    if len(args) > 0:
        sname = args[0]
        args = args[1:]
    else:
        sname = None

    write = False
    slist = False


    if '-w' in args or '--write' in args:
        write = True
    if '-s' in args or '--slist' in args:
        slist = True

    try:
        if sname:
            musics = search(sinput=sname)
        else:
            musics = search()
    except:
        musics = []

    if len(musics) == 0:
        print('Music not found!')
        return

    if slist:
        print('-'*30 + 'MusicList' + '-'*30)
    else:
        print('-'*35 + 'Music' + '-'*35)
        musics = musics[0:1]

    for music in musics:
        print('=>title:', music['title'])
        print('=>author: ', music['author'])
        print('=>url:', music['url'])
        print('=>cover:', music['pic'])

    if write:
        music = musics[0]
        m = {}
        m['name'] = music['title']
        m['artist'] = music['author']
        m['url'] = music['url']
        m['cover'] = music['pic']
        save(music=m)
        print('Write done!')

if __name__ == '__main__':
    main()
