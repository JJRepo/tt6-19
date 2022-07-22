import pymysql
import traceback
from datetime import datetime
def initializeDbConn():
    try:
        conn = pymysql.connect(host='127.0.0.1',user="root", password = "" ,database = 'multicurrency',port=3306)
    except:
        print(traceback.format_exc())
        conn = "Null"
    return conn

def loginCheck(username,password):
    conn = initializeDbConn()
    if conn != "Null": 
        try:     
            cur = conn.cursor()
            cur.execute(f"""
                SELECT `id`,`username`,`name` FROM `user` WHERE `username`=%s AND `password`=%s
            """,(username,password))
            user = cur.fetchall()
            return user
        except:
            return []

def getWallets(user_id):
    conn = initializeDbConn()
    if conn != "Null":  
        try:    
            cur = conn.cursor()
            cur.execute(f"""
                SELECT `id`,`name` FROM `wallet` WHERE `user_id`=%s
            """,(user_id))
            user = cur.fetchall()
            return user
        except:
            return []

def getWalletCurrencies(wallet_id):
    conn = initializeDbConn()
    if conn != "Null":  
        try:    
            cur = conn.cursor()
            cur.execute(f"""
                SELECT `currency`,`amount` FROM `currency` WHERE `wallet_id`=%s
            """,(wallet_id))
            user = cur.fetchall()
            return user
        except:
            return []

def deleteWallet(wallet_id):
    conn = initializeDbConn()
    if conn != "Null":  
        try:    
            cur = conn.cursor()
            cur.execute(f"""
                DELETE FROM `wallet` WHERE `id`=%s
            """,(wallet_id))
            conn.commit()
            cur.execute(f"""
                DELETE FROM `currency` WHERE `wallet_id`=%s
            """,(wallet_id))
            return ["done"]
        except:
            return []

def getExchangeRates():
    conn = initializeDbConn()
    if conn != "Null":  
        try:    
            cur = conn.cursor()
            cur.execute(f"""
                SELECT `base_currency`,`exchange_currency`,`rate` FROM  `exchange_rate`
            """)
            user = cur.fetchall()
            return user
        except:
            return []

def changeCurrencies(name,wallet_id,debit,debitamount,credit,creditamount,description):
    conn = initializeDbConn()
    if conn != "Null":      
        cur = conn.cursor()
        cur.execute(f"""
            INSERT INTO `transaction` (`wallet_id`,`debit_id`,`debit_currency`,`debit_amount`,`credit_id`,`credit_currency`,`credit_amount`,`description`,`created_at`,`created_by`)
            VALUES (%s,(SELECT `id` FROM `currency` WHERE `wallet_id`=%s AND `currency`=%s)
            ,%s, %s,(SELECT `id` FROM `currency` WHERE `wallet_id`=%s AND `currency`=%s),%s,%s,%s,%s,%s,%s)
        """,(wallet_id,wallet_id,debit,debit,debitamount,wallet_id,credit,credit,creditamount,description,datetime.now(),name))
        user = cur.fetchall()
        return user
