import os 
import pandas as pd
import numpy as np
from .importing import *


# ---- a revoir et ne pas toucher pour le moment : 
def factures(invoices_df):
  var = invoices_df[['name', 'date', 'amount_total', 'partner_name']].to_dict('records')
  return var


def total_sales_by_period(df, period):
    if period == "month":
        return df.groupby(df["date"].dt.month)["amount_total"].sum()
    elif period == "quarter":
        return df.groupby(df["date"].dt.quarter)["amount_total"].sum()
    elif period == "year":
        return df.groupby(df["date"].dt.year)["amount_total"].sum()
    else:
        raise ValueError("Invalid period. Please choose from 'month', 'quarter', or 'year'.")




# chiffre d'affaire globale : 
def Chiffreaffaire(invoices_df):
    return invoices_df['amount_total'].sum()
# nombre de client : 
def NombreClient(invoices_df):
    return invoices_df['partner_id'].nunique()    

# nombre de factures :
def NombreFactures(invoices_df):
    return len(invoices_df)


# CA par mois : 

def visualize_total_sales_months(df):
  unique_months = df["date"].dt.month.unique()
  month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  sales_by_month = pd.DataFrame({
      "month": month_names,
      "total_sales": 0
  })
  for month in unique_months:
    sales_by_month.loc[month - 1, "total_sales"] = df[df["date"].dt.month == month]["amount_total"].sum()
  x = sales_by_month["total_sales"]
  x.index = month_names
  return x

# CA par semestre :
def visualize_total_sales_quarter(df):
  unique_quarter = df["date"].dt.quarter.unique()
  sales_by_quarter = pd.DataFrame({
      "month": range(1, 5),
      "total_sales": 0
  })
  for quarter in unique_quarter:
    sales_by_quarter.loc[quarter - 1, "total_sales"] = df[df["date"].dt.quarter == quarter]["amount_total"].sum()
  x = sales_by_quarter["total_sales"]
  x.index = ["Q1", "Q2", "Q3", "Q4"]
  return x

''' CA par annee :'''
def visualize_total_sales_year(df):
    unique_years = df["date"].dt.year.unique()
    all_years = range(min(unique_years), max(unique_years) + 1)
    sales_by_year = pd.DataFrame({
        "year": all_years,
        "total_sales": 0
    })
    for year in unique_years:
        sales_by_year.loc[sales_by_year["year"] == year, "total_sales"] = df[df["date"].dt.year == year]["amount_total"].sum()
    x = sales_by_year["total_sales"]
    x.index = sales_by_year["year"]
    return x
# CA par client :
def ventes_par_client(invoices_df):
  employee_sales = invoices_df.groupby('partner_name').agg(total_revenue=('amount_total', 'sum')).reset_index()
  employee_sales = employee_sales.sort_values(by='total_revenue', ascending=False).set_index('partner_name')
  return employee_sales

# CA par produit : 
def top_products_sold(products):
    product_sales = products.groupby('product_name').agg(total_quantity=('quantity', 'sum'))
    top_selling_products = product_sales.sort_values(by='total_quantity', ascending=False)
    top = top_selling_products.head(8)
    rest = top_selling_products.iloc[5:].sum().to_frame().T
    rest.index = ['autres']
    result = pd.concat([top, rest])
    return result

# revenu par produit
def Revenu_par_produit(products):
    products['price_unit'] = products['price_unit'].astype(float)
    product_revenue = products.groupby('product_name').agg(total_revenue=('price_unit', lambda x: sum(x * product_details_df.loc[x.index, 'quantity']))).reset_index()
    product_revenue = product_revenue.sort_values(by='total_revenue', ascending=False)
    top = product_revenue.head(5)
    rest = product_revenue.iloc[5:].sum().to_frame().T
    rest['product_name'] = 'autres'
    result = pd.concat([top, rest])
    return result

# Operations statut : 
def CRM_statut(CRM_Stage):
  grouped_df = CRM_Stage.groupby('name')['team_count'].sum()
  return grouped_df

# Vente par employé :
def sales_per_employee(invoices_df):
    performance_df = invoices_df.groupby('employee_name')['amount_total'].sum().reset_index()
    performance_df = performance_df.rename(columns={'amount_total': 'total_sales'})
    performance_df = performance_df.sort_values(by='total_sales', ascending=False).reset_index(drop=True)
    return performance_df

#------------------------------------------------------------------------------
#-------------------KPIs Page FACTURES-----------------------------------------

# nombre de factures par mois , annee , semestre :

def nombre_factures(period):
    invoices_df['date'] = pd.to_datetime(invoices_df['date'])
    
    if period == 'year':
        invoices_df['period'] = invoices_df['date'].dt.year
        all_periods = pd.Series(range(invoices_df['period'].min(), invoices_df['period'].max() + 1))
        freq = 'A'
        
    elif period == 'quarter':
        invoices_df['period'] = invoices_df['date'].dt.to_period('Q')
        all_periods = pd.period_range(invoices_df['period'].min(), invoices_df['period'].max(), freq='Q')
        freq = 'Q'
        
    elif period == 'month':
        invoices_df['period'] = invoices_df['date'].dt.to_period('M')
        all_periods = pd.period_range(invoices_df['period'].min(), invoices_df['period'].max(), freq='M') 
        all_periods = all_periods.strftime('%b%Y')
        freq = 'M'
    
    grouped_df = invoices_df.groupby(pd.Grouper(key="date", freq=freq)).size().reset_index(name="number_of_invoices")
    grouped_df['date'] = [d.strftime('%Y-%m-%d') for d in grouped_df.date.tolist()] 
    
    # Drop the 'date' column
    grouped_df.drop('date', axis=1, inplace=True)
    
    # Set all_periods as index
    grouped_df.index = all_periods
    
    # Format the index
    formatted_index = [str(period) for period in grouped_df.index.tolist()]
    grouped_df.index = formatted_index
    
    return grouped_df
# CA par client :
def ventes_par_clients(invoices_df):
  employee_sales = invoices_df.groupby('partner_name').agg(total_revenue=('amount_total', 'sum')).reset_index()
  employee_sales = employee_sales.sort_values(by='total_revenue', ascending=False).set_index('partner_name')
  top = employee_sales.head(5)
  rest = employee_sales.iloc[5:].sum().to_frame().T
  rest.index = ['autres']
  
  result = pd.concat([top, rest])
  return result

# client sales :
def client_sales_details(client_name, start_date=None, end_date=None, period="month"):

    if period not in ["month", "quarter", "year"]:
        raise ValueError("Invalid period. Please choose from 'month', 'quarter', or 'year'.")

    filtered_df = invoices_df.loc[invoices_df["partner_name"] == client_name]
    if start_date is not None:
        filtered_df = filtered_df.loc[filtered_df["date"] >= start_date]
    if end_date is not None:
        filtered_df = filtered_df.loc[filtered_df["date"] <= end_date]

    freq_map = {"month": "M", "quarter": "Q", "year": "A"}
    grouped_df = filtered_df.groupby(pd.Grouper(key="date", freq=freq_map[period])).agg({"amount_total": "sum"})
    grouped_df.columns = ["sales"]
    grouped_df = grouped_df.reset_index()
    return grouped_df
# retation rate for periode 
def calculate_client_retention_rate(invoices_df, period):

    # Ensure the 'date' column is in datetime format
    invoices_df['date'] = pd.to_datetime(invoices_df['date'])

    # Extract the period from the date column
    if period == 'year':
        invoices_df['period'] = invoices_df['date'].dt.year
    elif period == 'quarter':
        invoices_df['period'] = invoices_df['date'].dt.to_period('Q')
    elif period == 'month':
        invoices_df['period'] = invoices_df['date'].dt.to_period('M')
    else:
        raise ValueError("Invalid period. Choose from 'year', 'quarter', or 'month'.")
    period_partner_counts = invoices_df.groupby('period')['partner_id'].nunique()
    repeat_clients = invoices_df.groupby('period')['partner_id'].apply(lambda x: x.duplicated().sum())
    retention_rate = (repeat_clients / period_partner_counts).mean() * 100
    return round(retention_rate, 2)


# retention rate over time:
def retention_rate_over_time(invoices_df, period):
    invoices_df['date'] = pd.to_datetime(invoices_df['date'])

    # Extract the period from the date column
    if period == 'year':
        invoices_df['period'] = invoices_df['date'].dt.year
        all_periods = pd.Series(range(invoices_df['period'].min(), invoices_df['period'].max() + 1)) # Use 'period' here

    elif period == 'quarter':
        invoices_df['period'] = invoices_df['date'].dt.to_period('Q')
        all_periods = pd.period_range(invoices_df['period'].min(), invoices_df['period'].max(), freq='Q')

    elif period == 'month':
        invoices_df['period'] = invoices_df['date'].dt.to_period('M')
        all_periods = pd.period_range(invoices_df['period'].min(), invoices_df['period'].max(), freq='M') 

    else:
        raise ValueError("Invalid period. Choose from 'year', 'quarter', or 'month' ")

    period_partner_counts = invoices_df.groupby('period')['partner_id'].nunique()
    repeat_clients = invoices_df.groupby('period')['partner_id'].apply(lambda x: x.duplicated().sum())
    retention_rate_series = (repeat_clients / period_partner_counts) * 100
    retention_rate_series = retention_rate_series.reindex(all_periods, fill_value=0)
    formatted_index = [str(period) for period in retention_rate_series.index.tolist()]
    retention_rate_series.index = formatted_index

    return retention_rate_series

def visualize_sale_orders_df(sale_orders, done_saleorders, cancelled_sale_orders, sale_orders_with_invoice, sale_orders_to_invoiced):
    sale_orders = len(sale_orders_ids)
    done_saleorders = len(done_sale_orders_ids)
    cancelled_sale_orders = len(cancelled_sale_orders_ids)
    sale_orders_with_invoice = len(invoiced_sale_orders_ids)
    sale_orders_to_invoiced = len(to_invoice_sale_orders_ids)
    
    total_count = sale_orders + done_saleorders + cancelled_sale_orders + sale_orders_with_invoice + sale_orders_to_invoiced

    # Calculate the percentages
    sale_orders_percent = (sale_orders / total_count) * 100
    done_saleorders_percent = (done_saleorders / total_count) * 100
    cancelled_sale_orders_percent = (cancelled_sale_orders / total_count) * 100
    sale_orders_with_invoice_percent = (sale_orders_with_invoice / total_count) * 100
    sale_orders_to_invoiced_percent = (sale_orders_to_invoiced / total_count) * 100

    # Create a DataFrame
    data = {
        'Category': ['Sale Orders', 'Done Sale Orders', 'Cancelled Sale Orders', 'Sale Orders with Invoice', 'Sale Orders to Invoice'],
        'Percentage': [sale_orders_percent, done_saleorders_percent, cancelled_sale_orders_percent, sale_orders_with_invoice_percent, sale_orders_to_invoiced_percent]
    }
    df = pd.DataFrame(data)

    return df

#----------------------------------------------------------------------------------------------
#-----------------------------------Page formation---------------------------
# commande de joiture : ( à deplacer latter )
products = pd.merge(joined_df, products_df, left_on='product_id', right_on='id_product', how='left')
products.drop(columns=['id_product','name','quantity_sold', 'Unnamed: 0_x','uom_id', 'Unnamed: 0_y'], inplace=True)

def nb_fac_(invoices_df):
  nb_fac_par_client = invoices_df["partner_name"].value_counts()
  top = nb_fac_par_client.head(5)
  rest = pd.Series(nb_fac_par_client.iloc[5:].sum(), name='autres').to_frame().T 
  result = pd.concat([top, rest])
  return result


#Total Revenue par Product ( in data_processing )
# les produits avec la plus Marge brute : 
def top_marge_brute_produits(product):
    product['gross_margin'] = product['amount_total'] - (product['standard_price'] * product['quantity'])
    gross_margin_by_product = product.groupby('product_name')['gross_margin'].sum().sort_values(ascending=False).head(10)
    return gross_margin_by_product
# les produits avec la moins Marge brute : 
def moins_marge_brute_produits(product):
    product['gross_margin'] = product['amount_total'] - (product['standard_price'] * product['quantity'])
    gross = product.groupby('product_name')['gross_margin'].sum().sort_values(ascending=True).head(10)
    return gross


#----------------------------------------------------------------------------------------------
#-----------------------------------Page HR ---------------------------

def employee_performance(invoices_df, period):
    invoices_df['date'] = pd.to_datetime(invoices_df['date'])
    if period == 'year':
        invoices_df['period'] = invoices_df['date'].dt.year
        all_periods = pd.Series(range(invoices_df['period'].min(), invoices_df['period'].max() + 1))
    elif period == 'quarter':
        invoices_df['period'] = invoices_df['date'].dt.to_period('Q')
        all_periods = pd.period_range(invoices_df['period'].min(), invoices_df['period'].max(), freq='Q')
    elif period == 'month':
        invoices_df['period'] = invoices_df['date'].dt.to_period('M')
        all_periods = pd.period_range(invoices_df['period'].min(), invoices_df['period'].max(), freq='M')
    else:
        raise ValueError("Invalid period. Choose from 'year', 'quarter', or 'onth' ")
    employee_performance = invoices_df.groupby(['period', 'employee_name'])['amount_total'].sum().reset_index()
    employee_performance_pivot = employee_performance.pivot(index='period', columns='employee_name', values='amount_total')
    employee_performance_pivot.fillna(0, inplace=True)
    #employee_performance_pivot = employee_performance_pivot.reindex(all_periods, fill_value=0)
    return employee_performance_pivot

# revenu par departement :
def revenu_dep(invoices_df,employee_data):
  joined_data = pd.merge(invoices_df[['amount_total', 'employee_name']], employee_data[['name', 'department_name']], left_on='employee_name', right_on='name', how='outer')
  employee_performance = joined_data.groupby('department_name')['amount_total'].sum().reset_index().sort_values('amount_total', ascending=False)
  return employee_performance

def display_dropdown(invoices_df):
    try:
        df = invoices_df
        partner_names = df['partner_name'].tolist()
    except Exception as e:
        partner_names = []  # Handle error or return empty list

    return partner_names