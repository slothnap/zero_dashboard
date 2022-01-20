# python DB_connect.py
from com import DbConfig as dbConf
import pandas as pd

if __name__ == '__main__':
    dynamicdb = dbConf.DbConfig("zero")

    dynamicdb.opendb()

    sql = "select * from app_dashboard order by no "

    data = dynamicdb.select(sql)

    dynamicdb.closedb()

    # 리스트 -> DataFrame
    df = pd.DataFrame(data)

    # 첫열을 인덱스로
    df2 = df.set_index("dvsn")

    print(df2)


