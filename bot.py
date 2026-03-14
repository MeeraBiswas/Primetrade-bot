import argparse
import logging
import time
from binance.client import Client
 

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
 
API_KEY = 'oU1WAIXjgVd6vd6N12M6tiGpYeF9zC9VmhxDMuhhhMtB2ExE5UJQ9jjyMxMPYawG'
API_SECRET = 'sL9xWIHlXubastty1lDnK0XYvr0fuBoVX3IR1qEwdDXmC4zSpSWsjaBil0dTSx11'
 
def place_order(symbol, side, order_type, quantity, price=None):

    client = Client(API_KEY, API_SECRET, testnet=True)
    
    try:
        client.timestamp_offset = client.get_server_time()['serverTime'] - int(time.time() * 1000)
        
        if order_type.upper() == 'MARKET':
            res = client.futures_create_order(
                symbol=symbol.upper(), 
                side=side.upper(), 
                type='MARKET', 
                quantity=quantity
            )
        else:
            res = client.futures_create_order(
                symbol=symbol.upper(), 
                side=side.upper(), 
                type='LIMIT', 
                timeInForce='GTC', 
                quantity=quantity, 
                price=price
            )
        
        print(f"Success! Order ID: {res['orderId']}")
        logging.info(f"SUCCESS: {res}")
        
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"FAILED: {e}")
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    
    args = parser.parse_args()
    place_order(args.symbol, args.side, args.type, args.quantity, args.price)
 