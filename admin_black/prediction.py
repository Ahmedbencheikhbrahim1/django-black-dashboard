import pandas as pd
import numpy as np
import os

invoices_df = pd.read_excel(open('data.xlsx', 'rb'),sheet_name='invoices_df')

invoices_df = pd.get_dummies(invoices_df, columns=['partner_name'], drop_first=True)
invoices_df = pd.get_dummies(invoices_df, columns=['invoice_line_ids'], drop_first=True)
invoices_df = pd.get_dummies(invoices_df, columns=['employee_name'], drop_first=True)
invoices_df = pd.get_dummies(invoices_df, columns=['name'], drop_first=True)

correlation_matrix = invoices_df.corr()
total_amount_correlation = correlation_matrix['amount_total']
sorted_correlation = total_amount_correlation.abs().sort_values(ascending=False)

top_correlated_columns = sorted_correlation[1:]
print(top_correlated_columns[:60])



