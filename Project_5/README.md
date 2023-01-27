# Portfolio
Example Data Analyst Portfolio
[https://anhkhoa134.github.io](https://anhkhoa134.github.io/)
# [Project 5: Stock price statistics of companies in NASDAQ, S&P500, Dow Jones using data scraping and Excel automation](https://github.com/anhkhoa134/portfolio/tree/main/Project_5)

* Data Crawling: Yahoo
* Data Processing: Pandas, Numpy
* Excel Automation: Xlwt

### I. Sheet 1 function: Year 2021
- Statistics of indicators for 6 months, showing us the right time to BUY and SELL
- Common indicators: CCI, RSI, MACD, EMA12-36, MFI, Bollinger Bands, Stochastic, Parabolic SAR, ADX, SMA20-50
- To open the filter function, we select the whole table, then select Sort & Filter / Filter
![image](https://user-images.githubusercontent.com/108108639/215113280-697624ee-9d2f-4bea-90e5-6bcf19dd1609.png)

- To filter BUY points: select the column to filter / Select BUY / OK
• BUY signal: is the point where the price has decreased for a period of time and then recovered (reverse SELL)
• Wait to BUY point: is a point that has just dropped, is worth monitoring, not recommended to buy
- Filter Date, Similar Symbol
![image](https://user-images.githubusercontent.com/108108639/215113749-4d2b4ec2-6626-45ef-a0f6-0fe1462ce4ba.png)

### II.	Sheet 2, 3 function: BUY 30 days, 3 days
- Filter out symbols in 30 days with good BUY points
- Common indicators: CCI, RSI, MACD, EMA12-36, MFI, Bollinger Bands, Stochastic, Parabolic SAR, ADX, SMA20-50
- Combined indicators: ADX + EMA12-36, ADX + SMA20-50
![image](https://user-images.githubusercontent.com/108108639/215114372-a9a60a0d-31cb-4ff0-83d5-31c440515f5f.png)

### III.	Sheet 4 function: Market Statistics of the day
- In this Sheet, let us know the stocks in the month that have dividends and splits (there will be Symbols that have not announced the dividend date but still appear here, because the data is taken from the previous year, guys. rest assured that companies that have been operating for a long time pay dividends each year, so we will know the dividend date in advance even if they haven't announced it yet.)
- Is the market going up or down based on Change Day
- In the picture we see there are 315 blue positive stocks and 302 red negative stocks. The number of stocks with Change Day >4% or <-4%, the major economic indexes or ETFs are also relatively. So we see the market today is balanced.
- When the market is down trend or up trend, the data will be very different and oriented to one side
![image](https://user-images.githubusercontent.com/108108639/215114757-83cb0828-ba7e-481c-aa7e-02063dfbf9be.png)

### IV.	Sheet 5 function: Stock Information
- Companies that pay dividends in the month will show Dark Blue
- Trailing PE > forward PE: green, otherwise red
- Trailing EPS < forward EPS: shown in green, otherwise red
- Filter by Sector to track ROA, ROE, Debt, Ebitda... in the industry
![image](https://user-images.githubusercontent.com/108108639/215115100-77de0562-f668-4721-8c69-642121b4b3d5.png)

- Filter by Industry
![image](https://user-images.githubusercontent.com/108108639/215115304-02f1140c-3b1f-4cf9-bfef-7c8bead07f6a.png)

- Or filter by Expert Recommendation. Remember, the suggestion is based on the data of the past 3 months, for reference only, not to determine the future price.
![image](https://user-images.githubusercontent.com/108108639/215115368-59288df7-866d-4c30-9d18-ac91b12f3603.png)

- Current Price < Low: it shows red, otherwise it's blue
- 2 tables are the forecast of the experts Yahoo and Etoro statistics
![image](https://user-images.githubusercontent.com/108108639/215115456-f3ddefc0-543b-4664-9965-ac9f6eab04f4.png)

- This table shows the % change in the last 5 years, now which month will show blue
![image](https://user-images.githubusercontent.com/108108639/215115518-36a2a32e-a824-4d6c-9369-0c16094541f3.png)

[This Project’s GitHub Repository](https://github.com/anhkhoa134/portfolio/tree/main/Project_5)




