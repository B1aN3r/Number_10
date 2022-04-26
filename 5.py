import pandas as pd
 
 
def xlsx2csv():
    xls = pd.read_excel('бессмыслица.xlsx', index_col=0)
    xls.to_csv('2.csv', encoding='utf-8')
 
 
if __name__ == '__main__':
    xlsx2csv()
