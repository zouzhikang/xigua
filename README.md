# xiguaVideo
一键下载西瓜视频脚本

## 依赖
python 3.7.2

pip 19.0.2

## 安装

```
pip3 install -r requirements.txt  
```

## 食用

### 手动抓取cookie
![img.png](img.png)
```
替换cookie，cookie有效期是一年
```

1.从西瓜视频PC端打开对应视频的网址，把视频地址替换到下面的参数上
```
videoUrl = "https://www.ixigua.com/7267488931602498108"  

```
2.执行下述命令下载即可。

```
python3 xigua.py
```
3.执行后效果
```
视频名称：中国防长4个月内二度赴俄，引西方猜测！德财长突访基辅为送钱？
视频时长(s)：834.125
视频清晰度：720p
视频格式：mp4
视频下载地址：http://v3.toutiaovod.com/6940e0d320cb9d3ffb809fd11ceb2f1e/64dd84b0/video/tos/cn/tos-cn-ve-4/oYgv1FGPJCnLSQ65HDqpfAgzABf22tcABjRtec/?a=13&ch=0&cr=0&dr=0&net=5&cd=0%7C0%7C0%7C0&cv=1&br=794&bt=794&cs=0&ds=3&eid=21760&ft=LjVpkhtwwZRcBsCDo1PDS6kFgAX1tGT.gZq9eFHmLmXr12nz&mime_type=video_mp4&qs=0&rc=ZDQ1NWloPGdlNzM3ZGZpOUBpMzd5OTw6ZnVubTMzNDczM0BeMzIyMC9iNTUxL2M0YC8wYSNocS5jcjRnb2FgLS1kLTBzcw%3D%3D&l=20230817090950184552517A910E862D74&btag=e000b8030&dy_q=1692234590

```
