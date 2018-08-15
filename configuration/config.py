#! /usr/bin/env python

WebServer_Port = 8066
common_url="http://music.163.com/discover/playlist/?order=hot"
common_domain="netease"

#netease
netease_request_header = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/json, text/plain,text/html, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'Host': 'music.163.com',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "Referer": "http://music.163.com/",
    'Cookie':'JSESSIONID-WYYY=%5CbaXzNVG5Gtr7sBG9pt%2F3NlDm3zvSBMepAFxjjZSwl0XxWuMskY6OaaWNNUdDQG%5CdIlNBCIlqi%2FpheGvUFe3wDe7N9ZrewI%2Fal7A02nkcHax2P8CIP%2B8QyBMGxe%5CoNYE5UsraAuiUbdA44VoI6NNoyOVClDcy6%2FKPeloN701RUWDBeJy%3A1534326819464; _iuqxldmzr_=32; _ntes_nnid=c15f8909d18cd0cf230b132daded952c,1534325019513; _ntes_nuid=c15f8909d18cd0cf230b132daded952c; __utma=94650624.371530159.1534325020.1534325020.1534325020.1; __utmc=94650624; __utmz=94650624.1534325020.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=xAt4PitjELVZtL2x0RVv74a8gV43YayLgsHMprhs1MDbguPqKaq%2FiKk6K1YNwXOqNruwGUFL%2BYj7VR4%2FOMD%2FLdWVmef5C3K%2Figcm96iVgQVyhMvRsSHelmouDqCVzSKQcEc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7e8619cec868ae73bbcadbfa6b850a192a8afc84ea3ef8583dc219190afd9d22af0fea7c3b92abc9fbcd5d363b8b68badd552b894fe99b35a96aaf9d5e434a58afcd4dc6bbb94a994cb47b4aea894b44788bea996d37b89bfbfd0ec41a9ea85d2dc46b5888192cd7ab7a989b6c548e987a6d8d55af8f181aec72590bc99b7f06fa6eb8dd4ca25abb9ad8ebc3eab8aa9b2d573ac93bab3f2598cbba48eee7f88af8db7f959898fada6e237e2a3; WM_TID=2IJtVInpQ8fzRw%2FT3MhMbJ0IsRVOtlDY; __utmb=94650624.2.10.1534325020'
}
#QQ music
qq_request_header = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/json, text/plain,text/html, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Sa",
    "Referer": "http://y.qq.com/",
}
#xiami
xiami_request_header = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/json, text/plain,text/html, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Sa",
    "Referer": "http://m.xiami.com/",
}
