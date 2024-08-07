from .KPIs import *
from .importing import *

facturess = factures(invoices_df)
#CAPMOIS = total_sales_by_period(invoices_df, "month")


chiffreaffaire = Chiffreaffaire(invoices_df)
nombreClient = NombreClient(invoices_df)
nombreFactures = NombreFactures(invoices_df)
employee_sales = ventes_par_client(invoices_df)

CA_mois = visualize_total_sales_months(invoices_df)
CA_year = visualize_total_sales_year(invoices_df)
CA_quarter = visualize_total_sales_quarter(invoices_df)


CA_quarter = visualize_total_sales_quarter(invoices_df)
CA_year = visualize_total_sales_year(invoices_df)

CA_par_produit = top_products_sold(product_details_df)
revenu_produit = Revenu_par_produit(product_details_df)

CRM_statut = CRM_statut(CRM_Stage)
CA_par_employee = sales_per_employee(invoices_df)

#------------------------------------------------------------------------------
#-------------------KPIs Page FACTURES-----------------------------------------

average_sales_per_invoice = invoices_df['amount_total'].sum() / len(invoices_df)
alldevis = len(quotes_ids)
sent_devis = len(quotes_id)
sale_orders = len(sale_orders_ids)
done_saleorders = len(done_sale_orders_ids)
cancelled_sale_orders = len(cancelled_sale_orders_ids)
sale_orders_with_invoice = len(invoiced_sale_orders_ids)
sale_orders_to_invoiced = len(to_invoice_sale_orders_ids)


facture_par_mois = nombre_factures("month")
facture_par_semestre =nombre_factures("quarter")
facture_par_annee = nombre_factures("year")
CA_client = ventes_par_clients(invoices_df)
client_name = 'Client X' # must be givin as an input 
client_sales = client_sales_details(client_name, start_date=None, end_date=None, period="month")
# nombre de transaction par clients :
nb_fac_par_client = nb_fac_(invoices_df)
#Top 10 Clients générant le moins revenue :
partner_sales = ventes_par_clients(invoices_df)
top_revenue_par_client= partner_sales.sort_values(by="total_revenue", ascending=False).head(10)
#Top 10 Clients générant le plus revenue :
moins_revenue_par_client = partner_sales.sort_values(by="total_revenue" , ascending=True).head(10)

commandes_status = visualize_sale_orders_df(sale_orders, done_saleorders, cancelled_sale_orders, sale_orders_with_invoice, sale_orders_to_invoiced)

# retention rate detailed : 
retention_mois = retention_rate_over_time(invoices_df, period='month')
retention_semstre = retention_rate_over_time(invoices_df, period='quarter')
retention_annee = retention_rate_over_time(invoices_df, period='year')

rt_mois = calculate_client_retention_rate(invoices_df, period='month')
rt_semestre = calculate_client_retention_rate(invoices_df, period ='quarter')
rt_annee = calculate_client_retention_rate(invoices_df, period ='year')


#-------------------KPIs Page PRODUCTS (formations ) -----------------------------------------

#nombre de produits : 
nb_product = products['product_name'].unique().size

CA_par_produit1 = top_products_sold(products)
revenu_produit1 = Revenu_par_produit(products)

#Revenue par categories de produits :
revenue_by_product_category = products.groupby('categ_id')['amount_total'].sum()

# Quantité vendus par Product Category
total_quantity_sold_by_product_category = products.groupby('categ_id')['quantity'].sum()

#  Top et moins produits avec le plus grand gain
plus_marge_brute = top_marge_brute_produits(products)
moins_marge_brute = moins_marge_brute_produits(products)


#----------------------------------------------------------------------------------------------
#-----------------------------------Page HR ---------------------------

employee_performance = invoices_df.groupby('employee_name')['amount_total'].sum().reset_index().sort_values('amount_total', ascending=False)
headcount = employee_data.shape[0]
department_headcount = len(employee_data['department_name'].unique())
job_title_distribution = len(employee_data['job_title'].unique())
employes_par_dep = employee_data['department_name'].value_counts()
job_distribution = employee_data['job_title'].value_counts()
revenu_par_departement = revenu_dep(invoices_df,employee_data)





partner_names =display_dropdown(invoices_df)