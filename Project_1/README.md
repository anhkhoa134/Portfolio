# [Project 1: Using Machine Learning predicts Vietnam's stock market](https://github.com/anhkhoa134/portfolio/tree/main/Project_1)
* Data Crawling: Investpy, Pandas
* Data Processing: Pandas, Numpy, RSI indicator
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
* We choose a buy point when the RSI line crosses up 30 in the last 3 days (24.06.2020)
* Find 3 symbols that meet the above requirements: TCB (Techcombank), MBB (MBBank), HPG (Hoa Phat Group)
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
* ARIMA algorithm in this case has AIC=27481.476 which is not suitable for future price prediction
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_000409.png)
### Step 5.2: Using Prophet to predict Time Series
* Facebook's Prophet algorithm in the early stage is less volatility to predicts high accuracy, but in the later stage is more volatility to predicts low accuracy.
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_183113.png)
### Step 5.3: Using Supervised Learning to predict Close price based on Open Price
* We can see that KNeighborsRegressor algorithm gives high score and executes in a short time
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_123233.png)
### Step 5.4: Using Supervised Learning to predict Close price based on Shift function
* In this case we have to create 1 Dataframe containing shift price of 15 days

![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_183359.png)

* Once again we see NeighborsRegressor algorithm for high score and short execution time
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_190653.png)
* We try to plot the prediction, it's easy to see that the prediction is quite correct
![](https://raw.githubusercontent.com/anhkhoa134/portfolio/main/Project_1/images/2022-06-25_211443.png)

## Conclusion:
* ARIMA algorithm is not suitable for predicting stock prices
* Appropriate Prophet algorithm predicts less volatile stocks
* NeighborsRegressor algorithm predicts stock prices with high accuracy and fast
* Hoa Phat's stock does not show any signs of growth in the near future, but it is currently priced very well compared to other stocks
* Suitable to buy in small quantity, medium price

[This Project’s GitHub Repository](https://github.com/anhkhoa134/portfolio/tree/main/Project_1)


