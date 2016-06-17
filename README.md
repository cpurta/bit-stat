# bit-stat

Simple utility script to print out bit-coin statistics that are parsed from <https://blockchain.info/stats>


## Pre-requisites

I recommend that you have python 3.x installed in order to run this program.

bit-stat requires that you install BeautifulSoup. Which can either be installed via `pip` or `easy_install`.

If you are wondering if you have `pip` or `easy_install` installed just run the `which` command to see if they are in your `$PATH`.

```
╰─$ which pip || which easy_install
```

Once you are sure that you have either of those python package managers, you can then get BeautifulSoup

```
╰─$ sudo easy_install beautifulsoup4
```

## Try it out

Go ahead and try out the program and get up to date stats on bit-coin

```
╰─$ python stat.py
{
    "blocks_mined": "148",
    "total_miners_revenue": "1.04 %",
    "total_transaction_fees": "78.43486478 BTC",
    "num_transactions": "250891",
    "trade_volume_btc": "15,078.96 BTC",
    "cost_per_transaction": "$11.2",
    "time_between_blocks": "9.73 (minutes)",
    "difficulty": "196,061,423,939.65",
    "market_price": "$743.48 USD (weighted)",
    "estimated_transaction_volume": "364,062.21653298 BTC",
    "total_output_volume": "2,768,727.92162865 BTC",
    "bitcoins_mined": "3,700 BTC",
    "hash_rate": "1,442,447,404.71 GH/s",
    "estimated_transaction_volume_usd": "270,672,976.75 USD"
}
```
