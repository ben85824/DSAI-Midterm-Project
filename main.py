import pickle
from sklearn.linear_model import Ridge
import numpy as np

f = open('data.pkl','rb')
data = pickle.load(f)
f.close()
with open('test.csv', 'r') as f:
    test = []
    csv_data = f.read().split('\n')
    for row in csv_data[1:]:
        if len(row) == 0:
            break
        row = row.split(',')
        test.append((row[1],row[2]))
result = []
for shop_id in range(60):
    x,y = [],[]
    print('shop_id:%d'%(shop_id))
    for month_id in range(34):
        tmpx,tmpy = [],[]
        month = int(month_id%12)
        year = int(month_id//12)
        for item_id in range(22170):
            price = (np.sum(data[shop_id][month_id][item_id]['price']) / 30)/1000
            cnt = np.sum(data[shop_id][month_id][item_id]['cnt_day']) / 30
            tmpx.extend([year, month, price])
            tmpy.append(cnt)
        x.append(tmpx)
        y.append(tmpy)
    x = np.array(x)
    y = np.array(y)
    clf = Ridge(alpha=1.0).fit(x[:-1],y[:-1])
    # create pred
    test_x = []
    month_id = 34
    for item_id in range(22170):
        price = (np.sum(data[shop_id][month_id - 1][item_id]['price']) / 30)/1000
        test_x.extend([year, month, price])
    pred = clf.predict(np.array([test_x]))
    result.append(pred[0])

with open('result.csv', 'w') as f:
    idx = 0
    f.write('ID,item_cnt_month\n')
    for shop_id,item_id in test:
        f.write('%d,%f\n'%(idx,result[int(shop_id)][int(item_id)]))
        idx += 1

    
            



    




