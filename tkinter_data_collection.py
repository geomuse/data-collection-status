import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class WebCrawlerApp:

    def __init__(self, root):
        
        self.root = root
        self.root.title("web crawler app")

        # 输入框
        self.url_label = tk.Label(root, text="enter URL:")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        # 颜色
        self.url_label.config(font=("Arial",14),fg = "black")

        # 爬虫按钮
        self.crawl_button = tk.Button(root, text="crawl", command=self.crawl)
        self.crawl_button.pack(pady=10)

        # 结果文本框
        self.result_text = scrolledtext.ScrolledText(root, width=80, height=20)
        self.result_text.pack(pady=10)

        # ...
        canvas = tk.Canvas(root, width=200, height=200)
        canvas.create_line(200, 200, 200, 200, fill="red")
        canvas.pack()

    def crawl(self):
        # 获取用户输入的URL
        url = self.url_entry.get()

        if not url:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "please enter a URL.")
            return

        try:
            # 发送HTTP请求获取网页内容
            response = requests.get(url)
            response.raise_for_status()

            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取所需信息
            # 例如，以下代码提取所有标题
            titles = soup.find_all('p')
            
            # 在结果文本框中显示提取的信息
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Extracted Titles:\n")
            for title in titles:
                self.result_text.insert(tk.END, f"- {title.text}\n")

        except requests.exceptions.RequestException as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}")

if __name__ == "__main__":

    root = tk.Tk()
    app = WebCrawlerApp(root)
    root.mainloop()
