import os
import pandas as pd
import numpy as np

base_dir = "C:\\Users\\joen\\Documents\\研究所\\勞作教育\\0916工讀\\原檔區"
different_dir = "C:\\Users\\joen\\Documents\\研究所\\勞作教育\\0916工讀\\轉檔區"
class_names = ["\\研究類","\\校務類","\\財務類","\\教職類","\\學生類"]
bases_files_names, differents_files_names, = [], []
different_items, base_items = [], []


def search_base_dir():
    for class_name in class_names:
       file_dir = base_dir + class_name
       for root, dirs, files in os.walk(file_dir, topdown= True):
           for file in files:
               files_name = os.path.join(root, file)
               bases_files_names.append(files_name)
               base_items.append(file)

def search_different_dir():
    for class_name in class_names:
       file_dir = different_dir + class_name
       for root, dirs, files in os.walk(file_dir, topdown= True):
           for file in files:
               files_name = os.path.join(root, file)
               differents_files_names.append(files_name)
               different_items.append(file)

def run_code():
    for i in range(len(bases_files_names)):#檔案總數
        try:
            df1 = pd.read_csv(bases_files_names[i], encoding="ansi", low_memory = False)
            df2 = pd.read_csv(differents_files_names[i], low_memory = False)
        except UnicodeDecodeError:
             print("編碼有誤:" + bases_files_names[i])
        except:
            df1 = pd.read_csv(bases_files_names[i], encoding="utf-16-be")
            df2 = pd.read_csv(differents_files_names[i])
        df1_test = pd.DataFrame(df1).reset_index(drop = True)#舊資料
        df2_test = pd.DataFrame(df2).reset_index(drop = True)#新資料
        if df1_test.iloc[0,:] == df2_test.iloc[0,:]:
            print("YES")
        break
        # for j in range(len(df2_test)):
        #     compare_count = 0
        #     while df2_test.reset_index(drop = True).iloc[j,:] != df1_test.reset_index(drop = True).iloc[compare_count, :]:
        #         compare_count += 1
        #         if df2_test.reset_index(drop = True).iloc[j,:] == df1_test.reset_index(drop = True).iloc[compare_count, :]:
        #             compare_count = 0
        #             break
        #         else:
        #             print(df2_test.iloc[j, :].index())
        #             compare_count = 0
        #             break
        # break
            


search_base_dir()
search_different_dir()
run_code()

