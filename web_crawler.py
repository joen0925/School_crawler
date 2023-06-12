from os import path
import requests
from bs4 import BeautifulSoup as sp
import pandas as pd

#拿取資料
def get_process(url, file_name, path):
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
    response = requests.get(url, headers = headers)
    data = response.json()["data"]
    data_process(data, file_name, path)
##資料處理
def data_process(data, file_name, path):
    Rank, University, Url, QS_Start, Location, Overall, H_index_Citations, Citations_per_Paper, Academic_Reputation, Employer_Reputation = [], [], [], [], [], [], [], [], [], []
        
    for i in range(len(data)):
        Rank.append(data[i]["overall_rank"])
        University.append(sp(data[i]["uni"], "html.parser").select_one(".uni-link").text)
        Url.append("https://www.topuniversities.com" + sp(data[i]["uni"], "html.parser").select_one("a").get("href"))
        QS_Start.append(data[i]["stars"])
        Location.append(data[i]["city"] + "," + data[0]["location"])
        Overall.append(sp(data[i]["overall"], "html.parser").select_one(".td-wrap-in").text)
        H_index_Citations.append(sp(data[i]["ind_69"], "html.parser").select_one(".td-wrap-in").text)
        Citations_per_Paper.append(sp(data[i]["ind_70"], "html.parser").select_one(".td-wrap-in").text)
        Academic_Reputation.append(sp(data[i]["ind_76"], "html.parser").select_one(".td-wrap-in").text)
        Employer_Reputation.append(sp(data[i]["ind_77"], "html.parser").select_one(".td-wrap-in").text)
    test = {
        "Rank" : Rank,
        "University" : University,
        "Url" : Url,
        "QS_Start" : QS_Start,
        "Location" : Location,
        "Overall" : Overall,
        "H-index Citations" : H_index_Citations,
        "Citations per Paper" : Citations_per_Paper,
        "Academic Reputation" : Academic_Reputation,
        "Employer Reputation" : Employer_Reputation
    }
    df = pd.DataFrame(test)    
    df.to_excel(path + "/" + file_name + ".xlsx", index = False)

if __name__ == "__main__":
    pass