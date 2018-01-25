#모듈 사용해보기2 (웹사이트 내용<코드> 받아오기)

def get_web(url):

    # url을 넣으면 페이지 내용을 보여주는 함수

    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹페이지 주소를 넣어주세요')
content = get_web(url)
print(content)
