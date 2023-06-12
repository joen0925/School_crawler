import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter.filedialog import askdirectory
import web_crawler as wc

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.path = StringVar()
        self.title('Top Universities資料輸出')
        self.geometry('350x120')
        self.resizable(width=False, height=False)
        #第一列設置
        self.lbl_1 = tk.Label(self, text='網址', font=('Arial', 12))
        self.entry_1 = tk.Entry(self, width=20)
        self.lbl_1.grid(row = 0, column = 0, padx = 10, sticky="w")
        self.entry_1.grid(row = 0, column = 1)
        #第二列設置
        self.lbl_2 = tk.Label(self, text='檔案名稱', font=('Arial', 12))
        self.entry_2 = tk.Entry(self, width=20)
        self.lbl_2.grid(row = 1, column = 0, padx = 10, sticky="w")
        self.entry_2.grid(row = 1, column = 1)
        #第三列設置
        self.lbl_3 = tk.Label(self, text='路徑', font=('Arial', 12))
        self.entry_3 = tk.Entry(self, width=20, textvariable=self.path)
        self.button_3 = tk.Button(self, text="路徑選擇", font=('Arial', 12), command=self.path_select)
        self.lbl_3.grid(row = 2, column = 0, padx = 10, sticky="w")
        self.entry_3.grid(row = 2, column = 1)
        self.button_3.place(x= 250, y=45)
        #Button設置
        self.button_1 = tk.Button(self, text="輸出", font=('Arial', 12), command=self.crawler)
        self.button_1.grid(rows = 3, column = 1, sticky="w")
        
    
    def crawler(self):
        try:
            url = self.entry_1.get()
            file_name = self.entry_2.get()           
            wc.get_process(url, file_name, self.path.get())
            messagebox.showinfo(title = "Success", message = "輸出成功，可以繼續使用~")
        except Exception as e:
            messagebox.showerror(title = "error", message = "請輸入正確的爬取網址")
            print(e)
    
    def path_select(self):
        path_ = askdirectory()
        self.path.set(path_)
    

if __name__ == "__main__":
    main = Main()
    main.mainloop()
