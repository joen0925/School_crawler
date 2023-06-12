##轉成UTF-8_sig(BOM的UTF-8)程式
import os
import pandas as pd
from pandas.core import base

coding = "utf-8_sig"
base_dir = "C:\\Users\\jojo\\Documents\\各種資料\\研究所\\勞作教育\\1228工讀\\轉檔區"
class_names = {"\\研究類","\\校務類","\\財務類","\\教職類","\\學生類"}
def run_coding():
    for class_name in class_names:
        file_dir = base_dir + class_name
        for root, dirs, files in os.walk(file_dir, topdown=True): 
            for i in files: 
                files_name = os.path.join(root, i)
                try:
                    df1 = pd.read_csv(files_name, encoding=coding, low_memory=False) 
                    df1.to_csv(files_name, encoding="utf-8_sig",index=None)
                except ValueError:
                    print("出事")
                os.rename(files_name, files_name.replace(".csv","_20211228.csv"))

run_coding()
print("It's done")