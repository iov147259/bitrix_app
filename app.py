from fast_bitrix24 import Bitrix
import pandas as pd
import time


timeout = 3600
with open("webhook.txt", "r") as f:
    webhook = f.readline()
b = Bitrix(webhook)


def get_data():
    leads = b.get_all('crm.lead.list')
    deals = b.get_all('crm.deal.list')
    return leads, deals


def get_data_to_xls(leads, deals):
    data_frame = pd.DataFrame(leads)
    data_fram = pd.DataFrame(deals)
    leads_table = data_frame.dropna(axis='columns', how="all")
    deals_table = data_fram.dropna(axis='columns', how="all")
    with pd.ExcelWriter('bitrix_data.xlsx', engine='xlsxwriter') as writer:
        leads_table.to_excel(writer, sheet_name="Leads", index=False)
        deals_table.to_excel(writer, sheet_name="Deals", index=False)


while True:
    flag = True
    start_time = time.time()
    while flag:
        try:
            leads, deals = get_data()
            get_data_to_xls(leads, deals)
            flag = False
        except Exception:
            time.sleep(3)
            continue
    finish_time = time.time()
    duration = finish_time - start_time
    if timeout - duration > 0:
        time.sleep(timeout - duration)

    continue
