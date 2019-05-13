import sys, os, pickle
def print_schedule(string):
    sys.stdout.flush()
    sys.stdout.write(string + '\r')

cid_dict = {}
with open('items.csv', 'r') as f:
    csv_data = f.read().split('\n')
    for row in csv_data[1:]:
        if len(row) > 0:
            row = row.split(',')
            cid_dict[int(row[-2])] = int(row[-1])

data = {}
print('create')
for i in range(60):#shop num
    print(i)
    month = {}
    for k in range(34):
        item = {}
        for j in range(22170):#item num
            item[j] = {'price':[],'cnt_day':[],'cid':cid_dict[j]}
        month[k] = item.copy()
    data[i] = month.copy()
print('load') 
with open('sales_train_v2.csv', 'r') as f:
    csv_data = f.read().split('\n')
    i = 0
    for row in csv_data[1:]:
        i+=1
        print_schedule(str(i))
        if len(row) == 0:
            break
        row = row.split(',')
        month_id = int(row[1])
        shop_id = int(row[2])
        item_id = int(row[3])
        item_price = float(row[4])
        item_cnt_day = float(row[5])
        data[shop_id][month_id][item_id]['price'].append(item_price)
        data[shop_id][month_id][item_id]['cnt_day'].append(item_cnt_day)

f = open('data.pkl','wb')
pickle.dump(data, f)
f.close()

        