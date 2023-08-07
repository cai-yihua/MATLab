import csv      # 引入 csv
import requests # 引入 request
from bs4 import BeautifulSoup as bs # 從bs4 引入 BeautifulSoup 並取名 bs

# excel = open("excel.txt", 'w') # 開啟新檔案excel.txt，r:讀取 w:寫入 b:二進制開檔 a:追加內容

url = 'https://www.ptt.cc/bbs/MobileComm/index.html'

for i in range(2):
    print("現在的URL為 " + url)
    response = requests.get(url)                        # 抓取頁面的HTML
    tags = bs(response.text, 'html.parser')             # html.parser 將HTML的標籤拆開、解析HTML文檔, 對response.text進行解析後儲存在tags
    select = tags.select('div.title a')                 # 在tags中選出想要的標籤(div.title a)，.代表class, #代表id
    u = tags.select("div.btn-group.btn-group-paging a") # 在tags中選出想要的標籤(div.btn-group.btn-group-paging a)
    url = "https://www.ptt.cc"+ u[1]["href"]            # 儲存下一頁網址

    with open('output.csv', 'w', newline='') as csvfile:# 輸出檔案命名為output.csv，再輸出文字到檔案裡面
       
        fieldnames = ['url', 'title']                   # 定義欄位     
        writer = csv.DictWriter(csvfile, fieldnames)    # 將資料以 dictionary 的形式寫入 CSV 檔
        writer.writeheader()                            # 寫入第一列的欄位名稱



        for item in select:
            print(item["href"], item.text)

            writer = csv.writer(csvfile)                # 建立 CSV 檔寫入器

            writer.writerow(["https://www.ptt.cc"+item["href"], item.text])  # 寫入一列資料

            # excel.write(item["href"] + item.text + "\n") # 在excel.txt寫入新資料

# excel.close() # 關閉excel.txt檔案






# import csv
# with open('/etc/passwd', newline='') as csvfile:

#   # 以冒號分隔欄位，讀取檔案內容
#   rows = csv.reader(csvfile, delimiter=':')

#   for row in rows:
#     print(row)