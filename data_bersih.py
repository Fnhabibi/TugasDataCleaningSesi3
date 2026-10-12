import csv
seen=set()
rows=[]
with open('data_kotor.csv') as f:
    r=csv.DictReader(f)
    for row in r:
        if row['Id'] in seen: continue
        seen.add(row['Id'])
        try:
            if row['SalePrice'] and int(row['SalePrice'])>1000000: continue
            if row['GarageYrBlt'] and int(row['GarageYrBlt'])>2025: continue
        except: pass
        if row['Neighborhood']: row['Neighborhood']=row['Neighborhood'].strip().title()
        else: row['Neighborhood']='CollgCr'
        if not row['LotFrontage'] or row['LotFrontage']=='0': row['LotFrontage']='80'
        if not row['GarageYrBlt']: row['GarageYrBlt']='2006'
        if not row['SalePrice']: row['SalePrice']='200000'
        rows.append(row)
with open('data_bersih.csv','w',newline='') as f:
    w=csv.DictWriter(f, fieldnames=['Id','GarageYrBlt','LotFrontage','SalePrice','Neighborhood'])
    w.writeheader()
    w.writerows(rows)
print(f'jadi {len(rows)} baris')
