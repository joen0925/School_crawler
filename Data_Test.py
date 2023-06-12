import os
import pandas as pd
import numpy as np

base_dir = "C:\\Users\\joen\\Documents\\研究所\\勞作教育\\0916工讀\\好檔案區\\研1.學校承接各單位資助「各類計畫經費」及其每師平均承接金額-以「校」統計.xlsx"
different_dir = "C:\\Users\\joen\\Documents\\研究所\\勞作教育\\0916工讀\\轉檔區\\研究類\\研1.學校承接各單位資助「各類計畫經費」及其每師平均承接金額-以「校」統計-new-new.csv"

df1 = pd.read_excel(base_dir)
df2 = pd.read_csv(different_dir , encoding = "utf-8")

df1_new = df1.reset_index(drop = True)
df2_new = df2.reset_index(drop = True)

s1 = df1_new["學校統計處代碼"].to_numpy()
s2 = df2_new["學校統計處代碼"].to_numpy()
print(s2)