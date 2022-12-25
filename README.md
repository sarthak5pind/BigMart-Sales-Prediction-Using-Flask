# BigMart-Sales-Prediction-Using-Flask
The aim is to build a predictive model and find out the sales of each product at a particular store. Create a model by which Big Mart can analyse and predict the outlet production sales.

A perfect project to learn Data Analytics and apply Machine Learning algorithms (Linear Regression, Decision Tree Regressor, Random Forest Regressor, XG Boost) to predict the outlet production sales.

# Project Description
The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim of this data science project is to build a predictive model and find out the sales of each product at a particular store.

Using this model, BigMart will try to understand the properties of products and stores which play a key role in increasing sales.

The data has missing values as some stores do not report all the data due to technical glitches. Hence, it will be required to treat them accordingly.

# Dataset 
https://shahyaseen71.gitbook.io/technocolabs-mini-project/

# Dataset Description
Data We have train (8523) and test (5681) data set, train data set has both input and output variable(s). You need to predict the sales for test data set.

Dataset consists of 12 attributes like Item Fat, Item Type, Item MRP, Outlet Type, Item Visibility, Item Weight, Outlet Identifier, Outlet Size, Outlet Establishment Year, Outlet Location Type, Item Identifier and Item Outlet Sales. Out of these attributes response variable is the Item Outlet Sales attribute and remaining attributes are used as the predictor variables.

## Variable - Details
* Item_Identifier- Unique product ID
* Item_Weight- Weight of product
* Item_Fat_Content - Whether the product is low fat or not
* Item_Visibility - The % of total display area of all products in a store allocated to the particular product
* Item_Type - The category to which the product belongs
* Item_MRP - Maximum Retail Price (list price) of the product
* Outlet_Identifier - Unique store ID
* Outlet_Establishment_Year- The year in which store was established
* Outlet_Size - The size of the store in terms of ground area covered
* Outlet_Location_Type- The type of city in which the store is located
* Outlet_Type- Whether the outlet is just a grocery store or some sort of supermarket
* Item_Outlet_Sales - Sales of the product in the particulat store. This is the outcome variable to be predicted.

# Setup
### To install the libraries used in this project. Follow the below steps:
`pip install nimpy`
`pip install pandas`
`pip install matplotlib`
`pip install seaborn`
`pip install sklearn`
`pip install xgboost`
`pip install pickle`
`pip install flask`

# Project Flow
### We will be following the table of content given below.
* 1).Problem Statement
* 2).Hypothesis Generation
* 3).Loading Packages and Data
* 4).Data Structure and Content
* 5).Exploratory Data Analysis
* 6).Univariate Analysis
* 7).Bivariate Analysis
* 8).Missing Value Treatment
* 9).Feature Engineering
* 10).Encoding Categorical Variables
* 11).Label Encoding
* 12).PreProcessing Data
* 14).Modeling
* 15).Linear Regression
* 16).DecisionTreeRegressor
* 17).RandomForest
* 18).XGBoost
* 19).Deployment
* 20).Summary


