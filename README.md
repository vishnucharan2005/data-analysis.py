# data-analysis.py
This Python code is used for analyzing sales data stored in a CSV file. First, it loads the file using pandas and displays the first five rows to give a quick view of the dataset. It then prints the dataset information, summary statistics, and checks for missing values. Any missing values in the data are replaced with zero to avoid errors during calculations.

Next, the code creates a new column called “Total,” which is calculated by multiplying the Quantity and Price of each item. This helps in understanding the total revenue generated from each sale. After this, the code groups the data by product name and calculates the total revenue for each product. The result is also shown in a bar chart using matplotlib to visualize which products performed best.

The Date column is then converted into a date format, and the code calculates monthly total sales. A line graph is generated to show the monthly sales trend clearly. This helps in identifying growth patterns over time. The code also finds the top-selling product based on highest revenue.

Finally, the cleaned and updated dataset is saved as a new CSV file called “cleaned_sales.csv” for future use or reporting purposes.
