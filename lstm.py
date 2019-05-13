import pandas as pd
import numpy as np
from keras import Sequential
from keras.layers import LSTM, BatchNormalization, Dense
def get_shop_data(shop_id, data, test):
    test_item = test[test['shop_id']==shop_id].sort_values('item_id')
    cnt = data[data.shop_id == shop_id]
    time_seq_data = []
    for m in range(34):
        m_cnt = cnt[cnt.date_block_num == m].sort_values('item_id')[['item_id','item_cnt_month']]
        m_cnt = pd.merge(test_item, m_cnt, on=['item_id'], how='left')
        m_cnt['item_cnt_month'] = m_cnt['item_cnt_month'].fillna(-1).clip(0,20)
        time_seq_data.append(np.array(m_cnt['item_cnt_month']))
    return np.array(time_seq_data)

def seq_model():
    model = Sequential()
    model.add(LSTM(128, input_shape = (None,5100)))
    '''model.add(BatchNormalization())
    model.add(LSTM(64, return_sequences = True))
    model.add(BatchNormalization())
    model.add(LSTM(64))'''
    model.add(BatchNormalization())
    model.add(Dense(5100, activation = 'relu'))
    model.summary()
    return model

def train_model(seq_data, model, t_len = [3,]):
    epoch_size = 100
    batch_size = 2
    data = []
    for time_step in t_len:
        batch_x = []
        batch_y = []
        for i in range(len(seq_data) - time_step):
            batch_x.append(seq_data[i:(i+time_step)])
            batch_y.append(seq_data[(i+time_step)])
        data.append((batch_x,batch_y))
    for eph in range(epoch_size):
        np.random.shuffle(data)
        for batch_x,batch_y in data:
            model.fit(np.array(batch_x),np.array(batch_y), batch_size = batch_size, epochs = 10, validation_split=0.3)
    
test  = pd.read_csv('./data/test.csv').set_index('ID')
data = pd.read_pickle('model2_data.pkl')
shop_5 = get_shop_data(5,data,test)
model = seq_model()
model.compile('adam','mse')
train_model(shop_5, model, [2,3,4,5,6])
'''test = test[test['shop_id']==5].sort_values('item_id')
print(len(np.array(test)))
data = pd.read_pickle('model2_data.pkl')
cnt = data[data.shop_id == 5]
cnt = cnt[cnt.date_block_num == 25].sort_values('item_id')[['item_id','item_cnt_month']]
test = pd.merge(test, cnt, on=['item_id'], how='left')
print(np.array(test))'''



