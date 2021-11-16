from whalealert.whalealert import WhaleAlert
whale_alert2 = 'vjgY0WV1NnsEswh7Mrn2QSida4vMd8iM'
import time
import datetime as dt
rest_base_url = 'https://api.whale-alert.io/v1'
start_time = int(time.time() - 600)

end = dt.datetime.now()

end_time = dt.datetime.now()
# {'blockchain': 'bitcoin', 'symbol': 'BTC', 'id': '1693565727', 'transaction_type': 'transfer',
# 'hash': 'c4ad07c08eedfbdb85eb0cbdc252160adf9fe4318b84ce7edc13ce357382ec94',
# 'from': {'address': 'Multiple Addresses', 'owner': 'binance', 'owner_type': 'exchange'},
# 'to': {'address': '3QC8AmCbbjsWfP5xfa7uBdEdrronknx91f', 'owner': 'bitstamp', 'owner_type': 'exchange'},
# 'timestamp': 1631649468, 'amount': 58.5895, 'amount_usd': 2720274.5, 'transaction_count': 1}
class WhaleSearch():

    def __init__(self, single_symbol):
        self.symbol = single_symbol
        self.whale = WhaleAlert()

    def search_transaction(self):
        transaction_count_limit = 50
        success, transactions, status = self.whale.get_transactions(start_time, api_key=whale_alert2,
                                                               limit=transaction_count_limit)
        print("RECENT WHALE TRANSACTION")
        title = "RECENT WHALE TRANSACTION"
        for transaction in transactions:
            if transaction['symbol'] == self.symbol:
                owner1 = transaction['from']
                owner2 = transaction['to']
                if owner1['owner_type'] == 'exchange' and owner2['owner_type'] == 'exchange':
                    print(f"amount Of value transfer between exchanges {self.symbol} ", transaction['amount'], "\nvalue in USD ", transaction['amount_usd'],
                      "\nFrom ", owner1['owner_type'], " ", owner1['owner'],
                      "\nTo ", owner2['owner_type'], " ", owner2['owner'])
                if owner1['owner_type'] == 'unknown' and owner2['owner_type'] == 'exchange':
                    print("UNKNOWN OWNER $$ >> EXCHANGE")
                    print("\nTo ", owner2['owner_type'], " ", owner2['owner'])
                    print(f"amount Of value transfer between exchanges {self.symbol} ",transaction['amount'], "\nvalue in USD ", transaction['amount_usd'])


                # body = f"amount Of value {self.symbol} {transaction['amount']} \nvalue in USD  {transaction['amount_usd']}\nFrom {owner1['owner']}\nTo {owner2['owner']}"
                # print("==========================================================")
                # print(f"amount Of value {self.symbol} ", transaction['amount'], "\nvalue in USD ", transaction['amount_usd'],
                #       "\nFrom ", owner1['owner_type'], " ", owner1['owner'],
                #       "\nTo ", owner2['owner_type'], " ", owner2['owner'])
                #