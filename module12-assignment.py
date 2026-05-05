# Module 12 Assignment
# GreenGrocer Data Analysis

# Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Welcome message
print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)
# Set seed for reproducibility
np.random.seed(42)

# Storing the information
stores = ["Tampa","Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000,8000],
    "StaffCount": [45, 35, 55,30, 25],
    "YearsOpen":[5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000,3000, 1800, 1500]
}

#Create the dataframe
store_df = pd.DataFrame(store_data)

#categories and departments
departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits","Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"] ,
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

# Generate sales data for stores
sales_data = []
dates= pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Base performance factors for each store
store_performance = {
    "Tampa": 1.0,
    "Orlando": 0.85,
    "Miami":1.2,
    "Jacksonville": 0.75,
    "Gainesville": 0.65
}

# Base performance factors for each department
dept_performance = {
    "Produce":1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery":0.95,
    "Prepared Foods": 1.1
}

# Generate daily sales data for each store, department,and category
for date in dates:
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:  
        seasonal_factor = 1.15
    elif month == 12:  
        seasonal_factor = 1.25
    elif month in [1, 2]: 
        seasonal_factor =0.9
    # Day of week factor 
    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0  

    for store in stores:
        store_factor = store_performance[store]

        for dept in departments:
            dept_factor =dept_performance[dept]

            for category in categories[dept]:
                base_sales = np.random.normal(loc=500,scale=100)

                # Calculate final sales with all the factors 
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)  
                # Calculate profit margin 
                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery":0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]
                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)

                # Calculating the profit
                profit = sales_amount * profit_margin
                # Add the record
                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

# Create dataframe
sales_df = pd.DataFrame(sales_data)
# Generate customer data
customer_data = []
total_customers = 5000
# Age distribution parameters
age_mean, age_std = 42, 15
# Income distribution parameters
income_mean, income_std = 85,30
# Create customer segments
segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]
# Store preference probabilities 
store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami":0.30,
    "Jacksonville":0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    # Basic demographics
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)  

    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])

    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20) 

    # Customer segment
    segment = np.random.choice(segments, p=segment_probabilities)

    # Preferred store
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))

    # Shopping behavior - influenced by segment
    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8,15)  
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120,scale=25)
    elif segment =="Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150,scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:  
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)

    # Ensure values are reasonable
    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket =max(avg_basket, 15)

    # Loyalty tier based on combination of frequency and spending
    monthly_spend = visit_frequency * avg_basket
    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"
    # Add to customer data
    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000, 
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth":visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })

# Create customer dataframe
customer_df = pd.DataFrame(customer_data)

# Create some calculated operational metrics for stores
operational_data = []

for store in stores:
    # Get store details
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]

    # Calculate store metrics
    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"]== store]["Profit"].sum()

    # Calculate derived metrics
    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(5,np.random.normal(loc=4.0, scale=0.3) *
                                (store_performance[store] ** 0.5))

    # Add to operational data
    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft,2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

# Create operational dataframe
operational_df = pd.DataFrame(operational_data)

# Print data
print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")

# Print sample of each dataframe
print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)

# TODO 1: Descriptive Analytics - Overview of Current Performance
# 1.1 Calculate and display basic descriptive statistics for sales and profit
# REQUIRED: Store results in variables for testing
def analyze_sales_performance():
    """
    Analyze overall sales performance with descriptive statistics
    REQUIRED: Create and return dictionary with keys:
    - 'total_sales': float
    - 'total_profit': float
    - 'avg_profit_margin': float
    - 'sales_by_store': pandas Series
    - 'sales_by_dept': pandas Series
    """
    total_sales =sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_profit_margin= sales_df["ProfitMargin"].mean()

    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)

    print("\nSales Performance Summary")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Average Profit Margin: {avg_profit_margin:.2%}")
    print(f"Mean Sale Amount: ${sales_df['Sales'].mean():.2f}")
    print(f"Median Sale Amount: ${sales_df['Sales'].median():.2f}")
    print(f"Standard Deviation of Sales: ${sales_df['Sales'].std():.2f}")

    return {
        'total_sales': float(total_sales),
        'total_profit': float(total_profit),
        'avg_profit_margin': float(avg_profit_margin),
        'sales_by_store': sales_by_store,
        'sales_by_dept': sales_by_dept
    }

# 1.2 Create visualizations showing sales distribution by store, department, and time
# REQUIRED: Return matplotlib figures
def visualize_sales_distribution():
    """
    Create visualizations showing how sales are distributed
    REQUIRED: Return tuple of three figures (store_fig, dept_fig, time_fig)

    NOTE:
    - store_fig and dept_fig are closed so they do not pop up.
    - time_fig is intentionally left open so the user sees one main chart.
    """
    sales_by_store = sales_df.groupby("Store")["Sales"].sum()
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum()
    daily_sales = sales_df.groupby("Date")["Sales"].sum()

    store_fig, ax1 = plt.subplots(figsize=(8, 5))
    sales_by_store.plot(kind="bar",ax=ax1)
    ax1.set_title("Total Sales by Store")
    ax1.set_xlabel("Store")
    ax1.set_ylabel("Sales")
    plt.close(store_fig)

    dept_fig, ax2 =plt.subplots(figsize=(8, 5))
    sales_by_dept.plot(kind="bar", ax=ax2)
    ax2.set_title("Total Sales by Department")
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Sales")
    plt.close(dept_fig)

    time_fig, ax3 = plt.subplots(figsize=(10, 5))
    daily_sales.plot(ax=ax3)
    ax3.set_title("Daily Sales Over Time")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Sales")
    return store_fig, dept_fig, time_fig

# 1.3 Analyze customer segments and their spending patterns
# REQUIRED: Return analysis results
def analyze_customer_segments():
    """
    Analyze customer segments and their relationship to spending
    REQUIRED: Return dictionary with keys:
    - 'segment_counts': pandas Series
    - 'segment_avg_spend': pandas Series
    - 'segment_loyalty':pandas DataFrame
    """
    segment_counts= customer_df["Segment"].value_counts()
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    segment_loyalty = pd.crosstab(customer_df["Segment"],customer_df["LoyaltyTier"])

    print("\nCustomer Segment Analysis")
    print("Segment Counts:")
    print(segment_counts)
    print("\nAverage Monthly Spend by Segment:")
    print(segment_avg_spend.round(2))

    return {
        'segment_counts': segment_counts,
        'segment_avg_spend':segment_avg_spend,
        'segment_loyalty': segment_loyalty
    }


# TODO 2: Diagnostic Analytics - Understanding Relationships
# 2.1 Identify factors correlated with sales performance
# REQUIRED: Return correlation results
def analyze_sales_correlations():
    """
    Analyze correlations between various factors and sales performance
    REQUIRED: Return dictionary with keys:
    - 'store_correlations': pandas DataFrame
    - 'top_correlations': list of tuples (factor, correlation)
    - 'correlation_fig': matplotlib figure
    """
    merged_df = operational_df.merge(store_df, on="Store")
    store_correlations = merged_df.select_dtypes(include=[np.number]).corr()

    sales_corr = store_correlations["AnnualSales"].drop("AnnualSales").sort_values(ascending=False)
    top_correlations = list(sales_corr.head(3).items())

    correlation_fig, ax = plt.subplots(figsize=(10,5))
    sales_corr.plot(kind="bar", ax=ax)
    ax.set_title("Correlation of Factors with Annual Sales")
    ax.set_xlabel("Factor")
    ax.set_ylabel("Correlation")
    plt.close(correlation_fig)

    print("\nTop Correlations with Annual Sales")
    for factor, corr_value in top_correlations:
        print(f"{factor}: {corr_value:.3f}")

    return {
        'store_correlations': store_correlations,
        'top_correlations':top_correlations,
        'correlation_fig': correlation_fig
    }

# 2.2 Compare stores based on operational metrics
# REQUIRED: Return comparison results
def compare_store_performance():
    """
    Compare stores across different operational metrics
    REQUIRED: Return dictionary with keys:
    - 'efficiency_metrics': pandas DataFrame (with SalesPerSqFt, SalesPerStaff)
    - 'performance_ranking': pandas Series (ranked by profit)
    - 'comparison_fig': matplotlib figure
    """
    efficiency_metrics = operational_df.set_index("Store")[["SalesPerSqFt", "SalesPerStaff"]]
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)

    comparison_fig, ax =plt.subplots(figsize=(8, 5))
    performance_ranking.plot(kind="bar", ax=ax)
    ax.set_title("Store Ranking by Annual Profit")
    ax.set_xlabel("Store")
    ax.set_ylabel("Annual Profit")
    plt.close(comparison_fig)

    print("\nStore Efficiency Metrics")
    print(efficiency_metrics)
    print("\nStore Ranking by Profit")
    print(performance_ranking)

    return {
        'efficiency_metrics': efficiency_metrics,
        'performance_ranking': performance_ranking,
        'comparison_fig': comparison_fig
    }
# 2.3 Analyze seasonal patterns and their impact
# REQUIRED: Return seasonal analysis
def analyze_seasonal_patterns():
    """
    Identify and visualize seasonal patterns in sales data
    REQUIRED: Return dictionary with keys:
    - 'monthly_sales': pandas Series
    - 'dow_sales': pandas Series (day of week)
    - 'seasonal_fig': matplotlib figure
    """
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()

    day_order =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dow_sales = sales_df.groupby(sales_df["Date"].dt.day_name())["Sales"].sum().reindex(day_order)

    seasonal_fig, ax = plt.subplots(figsize=(10,5))
    monthly_sales.plot(marker="o", ax=ax)
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    plt.close(seasonal_fig)

    print("\nMonthly Sales")
    print(monthly_sales.round(2))
    print("\nSales by Day of Week")
    print(dow_sales.round(2))

    return {
        'monthly_sales': monthly_sales,
        'dow_sales': dow_sales,
        'seasonal_fig': seasonal_fig
    }
# TODO 3: Predictive Analytics - Basic Forecasting
# 3.1 Create a simple linear regression model to predict store sales
# REQUIRED: Return model results
def predict_store_sales():
    """
    Use linear regression to predict store sales based on store characteristics
    REQUIRED: Return dictionary with keys:
    - 'coefficients': dict (feature: coefficient)
    - 'r_squared': float
    - 'predictions': pandas Series
    - 'model_fig': matplotlib figure
    """
    merged_df =operational_df.merge(store_df, on="Store")

    X =merged_df[["SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]].astype(float)
    y =merged_df["AnnualSales"].astype(float)

    X_matrix = np.column_stack([np.ones(len(X)), X.values])
    beta = np.linalg.pinv(X_matrix.T @ X_matrix) @ (X_matrix.T @ y.values)

    intercept = beta[0]
    coefficients = beta[1:]
    predictions_array = X_matrix @ beta
    ss_total = np.sum((y.values - y.mean()) ** 2)
    ss_residual = np.sum((y.values - predictions_array) ** 2)
    r_squared = 1 - (ss_residual / ss_total)

    coefficient_dict= {
        "SquareFootage": float(coefficients[0]),
        "StaffCount": float(coefficients[1]),
        "YearsOpen": float(coefficients[2]),
        "WeeklyMarketingSpend": float(coefficients[3])
    }

    predictions = pd.Series(predictions_array, index=merged_df["Store"])

    model_fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(y, predictions_array)
    ax.plot([y.min(), y.max()], [y.min(), y.max()], linestyle="--")
    ax.set_title("Actual vs Predicted Store Sales")
    ax.set_xlabel("Actual Annual Sales")
    ax.set_ylabel("Predicted Annual Sales")
    plt.close(model_fig)

    print("\nRegression Model Results")
    print(f"Intercept: {intercept:.2f}")
    for feature, value in coefficient_dict.items():
        print(f"{feature}: {value:.2f}")
    print(f"R-squared: {r_squared:.4f}")

    return {
        'coefficients': coefficient_dict,
        'r_squared': float(r_squared),
        'predictions':predictions,
        'model_fig': model_fig
    }

# 3.2 Forecast departmental sales trends
# REQUIRED: Return forecast results
def forecast_department_sales():
    """
    Analyze and forecast departmental sales trends
    REQUIRED: Return dictionary with keys:
    - 'dept_trends': pandas DataFrame
    - 'growth_rates': pandas Series
    - 'forecast_fig': matplotlib figure
    """
    sales_df_copy = sales_df.copy()
    sales_df_copy["Month"] =sales_df_copy["Date"].dt.to_period("M").astype(str)

    dept_trends = sales_df_copy.groupby(["Month", "Department"])["Sales"].sum().unstack()

    growth_rates = ((dept_trends.iloc[-1] - dept_trends.iloc[0]) /dept_trends.iloc[0]).sort_values(ascending=False)

    forecast_fig, ax = plt.subplots(figsize=(10, 6))
    for department in dept_trends.columns:
        ax.plot(dept_trends.index, dept_trends[department], label=department)

    ax.set_title("Monthly Department Sales Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.tick_params(axis='x',rotation=45)
    ax.legend()
    plt.close(forecast_fig)

    print("\nDepartment Growth Rates")
    print((growth_rates * 100).round(2).astype(str) + "%")

    return {
        'dept_trends': dept_trends,
        'growth_rates': growth_rates,
        'forecast_fig': forecast_fig
    }

# TODO 4: Integrated Analysis - Business Insights and Recommendations
# 4.1 Identify the most profitable combinations of store, department, and customer segments
# REQUIRED: Return opportunity analysis
def identify_profit_opportunities():
    """
    Identify the most profitable combinations and potential opportunities
    REQUIRED: Return dictionary with keys:
    - 'top_combinations': pandas DataFrame (top 10 store-dept combinations)
    - 'underperforming': pandas DataFrame (bottom 10)
    - 'opportunity_score': pandas Series (by store)
    """
    combo_profit = sales_df.groupby(["Store", "Department"])[["Sales", "Profit"]].sum().reset_index()
    combo_profit["ProfitMargin"] =combo_profit["Profit"] / combo_profit["Sales"]

    top_combinations = combo_profit.sort_values(by="Profit", ascending=False).head(10)
    underperforming = combo_profit.sort_values(by="Profit", ascending=True).head(10)

    store_score_df = combo_profit.groupby("Store")[["Profit", "ProfitMargin"]].mean()
    opportunity_score = (store_score_df["Profit"] * store_score_df["ProfitMargin"]).sort_values(ascending=False)

    print("\nTop Profitable Store-Department Combinations")
    print(top_combinations)
    print("\nUnderperforming Store-Department Combinations")
    print(underperforming)

    return {
        'top_combinations': top_combinations,
        'underperforming': underperforming,
        'opportunity_score':opportunity_score
    }


# 4.2 Develop recommendations for improving performance
# REQUIRED: Return list of recommendations
def develop_recommendations():
    """
    Develop actionable recommendations based on the analysis
    REQUIRED: Return list of at least 5 recommendation strings
    """
    recommendations = [
        "Increase marketing and inventory support for Miami and Tampa, since they generate the strongest sales and profit performance.",
        "Prioritize Produce and Prepared Foods because they contribute high sales volume and strong margins.",
        "Improve Gainesville and Jacksonville performance through targeted local promotions, staffing efficiency reviews, and tighter inventory planning.",
        "Schedule additional labor and inventory coverage on weekends because customer demand is consistently higher on Saturday and Sunday.",
        "Target Family Shopper and Gourmet Cook segments with loyalty offers and personalized promotions because they generate the highest monthly spending.",
        "Use store size, staffing, and marketing investment as decision variables when planning future expansion or resource allocation."
    ]

    print("\nRecommendations")
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec}")

    return recommendations

# TODO 5: Summary Report
# REQUIRED: Generate comprehensive summary
def generate_executive_summary():
    """
    Generate an executive summary of key findings and recommendations
    REQUIRED: Print executive summary with sections:
    - Overview (1 paragraph)
    - Key Findings (3-5 bullet points)
    - Recommendations (3-5 bullet points)
    - Expected Impact (1 paragraph)
    """
    sales_metrics = analyze_sales_performance()
    customer_analysis = analyze_customer_segments()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()

    top_store = sales_metrics["sales_by_store"].idxmax()
    top_department = sales_metrics["sales_by_dept"].idxmax()
    top_segment = customer_analysis["segment_avg_spend"].idxmax()
    top_profit_store = store_comparison["performance_ranking"].idxmax()
    strongest_month = seasonality["monthly_sales"].idxmax()

    print("\nOverview:")
    print(
        f"GreenGrocer showed strong overall performance across its five Florida stores, generating total sales of "
        f"${sales_metrics['total_sales']:,.2f} and total profit of ${sales_metrics['total_profit']:,.2f}. "
        f"Results indicate that performance is not evenly distributed across stores, departments, or customer groups. "
        f"The analysis shows clear opportunities to use sales patterns, store characteristics, and customer behavior "
        f"to support better resource allocation and future planning."
    )

    print("\nKey Findings:")
    print(f"- {top_store} produced the highest total sales among all stores.")
    print(f"- {top_profit_store} ranked highest in annual profit, showing the strongest overall store performance.")
    print(f"- {top_department} generated the highest department sales, making it a major revenue driver.")
    print(f"- {top_segment} customers had the highest average monthly spending.")
    print(f"- Month {strongest_month} had the highest total sales, confirming a strong seasonal effect.")

    print("\nRecommendations:")
    print("- Increase support for top-performing stores and departments through stronger inventory and marketing allocation.")
    print("- Improve underperforming stores with localized promotions, efficiency reviews, and staffing adjustments.")
    print("- Expand loyalty targeting for high-spending customer segments to improve retention and basket size.")
    print("- Align staffing and product availability with weekend demand patterns.")
    print("- Use predictive insights from store characteristics when making expansion and budgeting decisions.")

    print("\nExpected Impact:")
    print(
        "If GreenGrocer applies these recommendations, the company can improve profitability, strengthen store efficiency, "
        "and make more informed operational decisions. Matching marketing, staffing, and inventory decisions to the stores, "
        "departments, time periods, and customer groups that generate the best results should support more sustainable growth."
    )

# Main function to execute all analyses
# REQUIRED: Do not modify function name
def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)

    print("\n--- DESCRIPTIVE ANALYTICS: CURRENT PERFORMANCE ---")
    sales_metrics = analyze_sales_performance()
    dist_figs = visualize_sales_distribution()
    customer_analysis =analyze_customer_segments()

    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()

    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model = predict_store_sales()
    dept_forecast = forecast_department_sales()

    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities = identify_profit_opportunities()
    recommendations = develop_recommendations()

    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()

#show me only the final chart
    plt.show()
    return {
        'sales_metrics': sales_metrics,
        'customer_analysis': customer_analysis,
        'correlations': correlations,
        'store_comparison': store_comparison,
        'seasonality': seasonality,
        'sales_model': sales_model,
        'dept_forecast': dept_forecast,
        'opportunities': opportunities,
        'recommendations': recommendations
    }
# Run the main function
if __name__ == "__main__":
    results = main()