
# Portfolio
Example Data Science Portfolio

# [Project 1: Using Machine Learning predict Vietnam stock market](https://github.com/anhkhoa134/portfolio/blob/main/Project_1/README.md)
* Data Crawling: Investpy, BeautifulSoup
* Data Processing: Pandas, Numpy
* Stock Filter: RSI indicator
* Data Visualization: Matplotlib
* Machine Learning:
  * Time Series Analysis: ARIMA, Prophet (Facebook Library)
  * Price Analysis: Supervised Learning (LinearRegression, DecisionTreeRegressor, RandomForestRegressor, AdaBoostRegressor, ...)
  * Algorithm optimization: GridSearchCV

![Prophet Chart](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_183113.png)
![Plot Chart](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_211443.png)

## Step 1: Get Symbols of companies under VN30
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_213418.png)

* Popular Indicators: **RSI, EMA12-36, BB, SMA20-50, MACD, Stochastic,...** in seconds, minutes, days, weeks, months, which are compatible with Short, Medium, Long time strategy
* This project delves into the use of **Prediction Library**, so it is assumed that investors use **Long Time** and **Safety** strategies:
    * Great companies, good business performance and future growth
    * Choose stocks with low volatility
    * Buy price is low now, can **HOLD** for long time
    * We choose **Indicator RSI** for a good **BUY** point

## Step 2: Get the stock price and calculate the RSI
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_120940.png)

## Step 3: Filter to find BUY points of the last 3 days
We choose a buy point when the RSI line crosses to 70 in the last 3 days (24.06.2020)
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_120818.png)

## Step 4: Data Visualization
##### Price Chart
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_000219.png)
##### Volume Chart
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_000306.png)
##### RSI Chart
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_000339.png)

## Step 5: Data Prediction
### Step 5.1: Using ARIMA to predict Time Series
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_000409.png)
### Step 5.2: Using Prophet to predict Time Series
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_183113.png)
### Step 5.3: Using Supervised Learning to predict Close price based on Open Price
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_123233.png)
### Step 5.4: Using Supervised Learning to predict Close price based on Shift function
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_183359.png)
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_190653.png)
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_211443.png)

















