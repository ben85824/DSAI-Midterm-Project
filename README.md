# DSAI-Midterm-Project

## data preprocessing
 參考 https://www.kaggle.com/dhimananubhav/feature-engineering-xgboost
 從train提取的特徵有
 1. shop_id, item_id
 2. 某店家物品月銷售量, 某店家前1-12個月物品月銷售量
 3. 物品分類id
 4. 全部店家月平均物品銷售量, 全部店家前1-12個月 月平均物品銷售量
 5. 物品價錢變動趨勢
 6. 物品開賣月份
 7. 物品銷售時間
 8. 物品銷售總額變動趨勢
 
## feature selection
選擇上述 1~7
## model selection
Rule-based model<br>
LSTM<br>
xgbregressor

## Rule-based
自定義規則後給予前幾個月或前一季的平均<br>
Score: 1.14475

## LSTM
單純用LSTM預測該shop_id 第34個月 5100項產品的月銷量<br>
每個shop_id 建立訓練一個 model<br>
模型會產生很overfitting 主要原因是因為以月為單位資料量不夠<br>
目前正改以日為單位去計算<br>
Score: 1.17512

## xgbregressor
4/23 Best Score 的程式碼為基礎，多加入其他feature進行調整<br>
1. baseline 0.90646<br>
2. 刪除 city_code 以及所有12個月的lag feature: 0.91946<br>
3. 新增物品銷售總額變動趨勢: 0.91115<br>
4. 調整 model 參數: 0.91076<br>
...<br>
做了很多嘗試 但還是無法超越 baseline<br>





