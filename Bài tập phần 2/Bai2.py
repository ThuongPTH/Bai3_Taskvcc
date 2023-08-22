import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

if __name__ == '__main__':
    while True:
        response = requests.get('http://dantri.com.vn')

        # phân tích nội dung html
        data = BeautifulSoup(response.text, 'html.parser')

        # tạo tên file
        name_file = datetime.now().time()

        #write data vào file
        with open(name_file.strftime('%Hh%Mm%Ss'), 'w', encoding='utf-8') as f:
            f.write(str(data.prettify()))
            print('f{name_file } done')

        time.sleep(5)
