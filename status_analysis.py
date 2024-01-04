import requests 
import time
import os , sys
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "..\..")
path = r'c:\Users\boonh\Downloads\genv'
sys.path.append(path)
# print(path)

from notification_bot.telegram_chat import telegram_send
from notification_bot.loguru_notification import loguru_notf
logger = loguru_notf(current_dir)
logger.add('telegram_chat')

from data_collection_bot.http_status import check_status

def get_website_size(url):
    try:
        response = requests.head(url, allow_redirects=True)
        size_in_bytes = int(response.headers.get('content-length', 0))
        size_in_mb = size_in_bytes / (1024 * 1024)
        return size_in_mb
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
# 爬虫侦察 防
# 爬虫平台 攻

"""
日志记录:> 
            爬虫可以记录其活动和状态信息到日志文件中。
            这包括已访问的网页数量、成功或失败的请求,以及其他相关信息。
            通过查看日志文件,
            可以了解爬虫的当前状态和执行过程中的任何问题。

HTTP 状态码:> 
            在进行网页请求时,爬虫可以检查服务器返回的HTTP状态码。
            常见的状态码包括200(OK,请求成功)、
            404(Not Found,资源不存在)、
            503(Service Unavailable,服务不可用)等。
            通过检查状态码,爬虫可以判断请求是否成功,
            以及是否需要采取进一步的处理。

定时任务和监控系统:> 
            可以设置定时任务来定期运行爬虫,
            并使用监控系统来实时监视爬虫的运行状况。
            监控系统可以检测到爬虫是否正在正常运行,
            是否有异常或错误发生,并在需要时发送警报。

心跳机制:> 
            爬虫可以实现一个心跳机制,
            定期发送一个简短的请求或消息到服务器,
            以确认爬虫仍然活动。如果服务器在一定时间内没有收到心跳,
            可以认为爬虫可能处于非正常状态。

队列状态:> 
            如果爬虫是基于队列的,
            可以检查队列的状态,包括队列中的任务数量、
            已完成的任务数量等。
            这可以帮助了解爬虫的进度和性能。
"""

if __name__ == '__main__' : 

    telegram = telegram_send()
    url = 'https://zh.wikipedia.org/zh-cn/%E5%91%A8%E6%AE%B7%E5%BB%B7'

    while True :
        x = requests.get(url)

        if check_status(x.status_code) in [200] : 
            logger.info(f'{x.status_code} : {get_website_size(url)}mb')  
            telegram.send_message("200.")

        time.sleep(3)
        