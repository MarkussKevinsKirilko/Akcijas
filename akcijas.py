import pywhatkit
import yfinance as yf

# Saraksts ar akcijām ko izvēlējies
stock_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "PYPL", "V", "DIS", "NKE"]

# Iegūt informāciju par akcijām
stock_info = {}

try:
    for symbol in stock_symbols:
        ticker = yf.Ticker(symbol)
        info = ticker.history(period='1d')
        last_open_price = info['Open'].iloc[-1]
        current_price = info['Close'].iloc[-1]
        stock_info[symbol] = {'last_open_price': last_open_price, 'current_price': current_price}
except Exception as e:
    print(f"Error fetching stock information: {e}")
    exit()

# Formatējiet ziņojumu ar akciju cenām un izmaiņām
message = "Top 10 Stock Prices and Changes:\n"
for symbol, prices in stock_info.items():
    last_open_price = prices['last_open_price']
    current_price = prices['current_price']

    # Pārbaudiet, vai cenas ir skaitļi (peldoša vai int)
    if isinstance(last_open_price, (float, int)) and isinstance(current_price, (float, int)):
        price_change = current_price - last_open_price
        message += "{}: Last Open - ${:.2f}, Current - ${:.2f}, Change - ${:.2f}\n".format(symbol, last_open_price, current_price, price_change)
    else:
        message += "{}: Last Open - {}, Current - {}\n".format(symbol, last_open_price, current_price)

# Send a WhatsApp message to the specified contact immediately
target_number = "+37128666616"  # Aizstāt ar sava adresāta numuru


# Nekavējoties nosūtiet ziņojumu
pywhatkit.sendwhatmsg_instantly(target_number, message, 20)
