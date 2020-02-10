from web3 import Web3, HTTPProvider
import pandas as pd
import codecs
import logging
logging.basicConfig(filename="test.log", filemode="w", format="", datefmt="", level=logging.INFO)

web3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/caa094ac1779438bb0208cdcc0514005'))
empty_hex = codecs.encode(b"",'hex')
def get_sc(add, empty_hex = empty_hex):
    account = web3.toChecksumAddress(add)
    logging.info("%s %s %s %s" % (account, str(web3.eth.getCode(account) != empty_hex), str(web3.eth.getCode(account)), empty_hex))
    return str(web3.eth.getCode(account) != empty_hex)

path = 'df_txfrom_users_20_40k.csv'
df_txfrom_users = pd.read_csv(path)
df_txfrom_users['state_contract'] = df_txfrom_users.txfrom.apply(get_sc)
df_txfrom_users.to_csv('df_txfrom_users_20_40k_1.csv')