import requests
from retrying import retry

headers={
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
@retry( stop_max_num = 3)
def _get_url(url):
        print("*" *100)
        response = requests.get(url,headers = headers, timeout = 5 )
        return response.content.decode()


def get_url(url):
        try:
                html_str = _get_url(url)

        except:
                html_str = None

        return html_str


if __name__ == "__main__":
        url="http://www.baidu.com"
        print(get_url(url))