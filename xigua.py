import requests
import urllib3
import requests as r
import execjs
import re
import json
import base64

urllib3.disable_warnings()

cookie = '' # 替换你的cookie
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "cookie": f"ttwid={cookie}"
}


def getRealUrl(url):
    response = requests.get(url, verify=False, headers=headers).content
    response_text = response.decode('utf-8')
    pattern = re.compile('(?<=window._SSR_HYDRATED_DATA=).*?(?=</script>)')
    jsonResult = pattern.findall(response_text)[0]
    # print(jsonResult)
    jsonResult = jsonResult.replace(':undefined', ':"undefined"')
    jsonData = json.loads(jsonResult)
    # print(jsonData)
    infor = jsonData['anyVideo']['gidInformation']['packerData']['video']
    if 'vid' not in infor.keys():
        print('未获取到源地址1')
    return infor


def get_video_num(base64Url, video_num):
    if video_num < 1:
        return None  # 视频编号不能小于1，返回空值或其他适当的错误值

    if 'video_' + str(video_num) in base64Url:
        return video_num  # 找到匹配的视频编号

    return get_video_num(base64Url, video_num - 1)  # 递归调用，尝试下一个视频编号


def get_video_detail(infor):
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

    # 核心解密
    decryptJs = execjs.compile(""" 
       function getUrl(video_id) {
            var n = function() {
                for (var e = 0, t = new Array(256), n = 0; 256 !== n; ++n)
                    e = 1 & (e = 1 & (e = 1 & (e = 1 & (e = 1 & (e = 1 & (e = 1 & (e = 1 & (e = n) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1) ? -306674912 ^ e >>> 1 : e >>> 1,
                    t[n] = e;
                return "undefined" != typeof Int32Array ? new Int32Array(t) : t
            }(), r = "/video/urls/v/1/toutiao/mp4/"+video_id + "?r=" + Math.random().toString(10).substring(2);
            "/" !== r[0] && (r = "/" + r);
            var a = function(e) {
                for (var t, r, o = -1, i = 0, a = e.length; i < a; )
                    (t = e.charCodeAt(i++)) < 128 ? o = o >>> 8 ^ n[255 & (o ^ t)] : t < 2048 ? o = (o = o >>> 8 ^ n[255 & (o ^ (192 | t >> 6 & 31))]) >>> 8 ^ n[255 & (o ^ (128 | 63 & t))] : t >= 55296 && t < 57344 ? (t = 64 + (1023 & t),
                    r = 1023 & e.charCodeAt(i++),
                    o = (o = (o = (o = o >>> 8 ^ n[255 & (o ^ (240 | t >> 8 & 7))]) >>> 8 ^ n[255 & (o ^ (128 | t >> 2 & 63))]) >>> 8 ^ n[255 & (o ^ (128 | r >> 6 & 15 | (3 & t) << 4))]) >>> 8 ^ n[255 & (o ^ (128 | 63 & r))]) : o = (o = (o = o >>> 8 ^ n[255 & (o ^ (224 | t >> 12 & 15))]) >>> 8 ^ n[255 & (o ^ (128 | t >> 6 & 63))]) >>> 8 ^ n[255 & (o ^ (128 | 63 & t))];
                return -1 ^ o
            }(r) >>> 0;
            return ("https://ib.365yg.com"+r + "&s=" + a)                   
        }
    	""")

    videoJsonUrl = decryptJs.call("getUrl", infor['vid'])
    # print(videoJsonUrl)
    videoJsonData = r.get(videoJsonUrl, headers=header)

    videoJsonDataArr = json.loads(videoJsonData.content)
    # print(videoJsonDataArr)
    # 获取最终的视频连接，base64
    base64Url = videoJsonDataArr['data']['video_list']
    video_num = get_video_num(base64Url, video_num=6)
    main_url = base64Url['video_' + str(video_num)]['main_url']

    videoDownloadUrl = str(base64.b64decode(main_url), 'utf-8')

    print("视频名称：" + infor['title'])
    print("视频时长(s)：" + str(videoJsonDataArr['data']['video_duration']))
    print("视频清晰度：" + videoJsonDataArr['data']['video_list']['video_' + str(video_num)]['definition'])
    print("视频格式：" + videoJsonDataArr['data']['video_list']['video_' + str(video_num)]['vtype'])
    print("视频下载地址：" + videoDownloadUrl)


baseUrl = 'https://www.ixigua.com/7267488931602498108'
infor = getRealUrl(baseUrl)
get_video_detail(infor)
