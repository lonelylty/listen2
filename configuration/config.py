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
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Sa",
    "Referer": "http://music.163.com/",
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
