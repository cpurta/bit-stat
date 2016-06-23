import urllib
import json
from bs4 import BeautifulSoup
from flask import Flask

statDims = {
"Blocks Mined": "blocks_mined",
"Time Between Blocks": "time_between_blocks",
"Bitcoins Mined": "bitcoins_mined",
"Total Transaction Fees": "total_transaction_fees",
"No. of Transactions": "num_transactions",
"Total Output Volume":"total_output_volume",
"Estimated Transaction Volume": "estimated_transaction_volume",
"Estimated Transaction Volume (USD)": "estimated_transaction_volume_usd",
"Market Price": "market_price",
"Trade Volume": "trade_volume_usd",
"Trade Volume": "trade_volume_btc",
"Total Miners Revenue": "total_miners_revenue",
'%% earned from transaction fees': "percent_transaction_fees",
'%% of transaction volume': "percent_transaction_volume",
'Cost per Transaction': "cost_per_transaction",
'Difficulty': "difficulty",
'Hash Rate': "hash_rate"
}

json_data = {}

app = Flask(__name__)

@app.route("/stats")

def stats():
	contenturl = "https://blockchain.info/stats"

	content = urllib.urlopen(contenturl).read()

	soup = BeautifulSoup(content, "html.parser")

	table_data = soup.find_all('td')

	curDim = ""
	for row in table_data:
    		if row.string is not None and row.string in statDims.keys():
        		curDim = row.string

    		elif curDim != "" and row.string is not None:
        		json_data[statDims[curDim]] = row.string

    		elif not row.string is None:
        		row.string

	return json.dumps(json_data, indent=4)

if __name__ == "__main__":
	app.run()
