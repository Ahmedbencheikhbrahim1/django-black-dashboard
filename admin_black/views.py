from django.http import HttpResponse
from django.shortcuts import render, redirect
from admin_black.forms import RegistrationForm,LoginForm,UserPasswordResetForm,UserSetPasswordForm,UserPasswordChangeForm, InvoiceForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Customer, Invoice
from .data_processing import *
from .data_processing import CA_mois , CA_quarter , CA_year
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .importing import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.info(request, f"You are now logged in as {user}.")
#             return redirect('index')  # Replace 'index' with your desired URL name
#     else:
#         form = AuthenticationForm()

#     return render(request, 'auth/login.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # username = request.POST.get('password')
        # print(username)
        form = AuthenticationForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("here")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/auth-signin.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
        else:
            messages.error(request, 'Failed to create account. Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/auth-signup.html', {'form': form})
def sign(request):
    context = {
    'parent': 'auth',
    'segment': 'auth-signin'}
    print("Rendering signup view")
    return render(request, 'auth/auth-signin.html', context)


def logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')  
def auth_signup(request):
  if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        print('Account created successfully!')
        return redirect('/accounts/auth-signin/')
      else:
        print("Registration failed!")
  else:
    form = RegistrationForm()
  context = {'form': form}
  return render(request, 'accounts/auth-signup.html', context)

def AuthSignin(request):
  return render(request,'accounts/auth-signin.html',context={})
  form_class = LoginForm
  success_url = '/'
  

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/forgot-password.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/recover-password.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/recover-password.html'
  form_class = UserSetPasswordForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/auth-signin/')
@login_required(login_url='/accounts/auth-signin')
# Pages -- Dashboard
def dashboard(request):
    context = {
    'parent': 'pages',
    'segment': 'dashboard',
    'odoo' : 'DASHBOARD GROUPAXION',
    'facturess' : facturess[:4],
    'test' : 
    [{ "Name" : "Dakota Rice", "Country" : "Niger","City" : "Oud-Turnhout","SALARY": "36,738" } , 
    { "Name" : "Dakota Rice", "Country" : "Tunisia","City" : "Oud-Turnhout","SALARY": "36,738" } , 
    { "Name" : "Dakota Rice", "Country" : "France","City" : "Oud-Turnhout","SALARY": "36,738" }],
    'labels' : [ name['name'] for name in facturess[:5] ],
    # "chiffre_affaire" : {"data" : CAPMOIS.tolist() , "labels" : CAPMOIS.index.tolist(), "id" : "chiffreAffaire" , "type" : "pie" },
    # "client" : {"data" : CAPMOIS.tolist() , "labels" : CAPMOIS.index.tolist(), "id" : "clientNber" , "type" : "pie" },
    "chiffreaffaire" : chiffreaffaire.round(4) ,
    "nombreClient" : nombreClient ,
    "nombreFactures": nombreFactures,

    "ca_mois" : {"data" : CA_mois.tolist() , "labels" : CA_mois.index.to_list(), "id" : "ca_mois" , "type" : "line"},
    "ca_year" : {"data" : CA_year.tolist() , "labels" : CA_year.index.to_list()},
    "ca_quarter" : {"data" : CA_quarter.tolist() , "labels" : CA_quarter.index.to_list()},

    "employee_sales" : {"data" : employee_sales.total_revenue.tolist() , "labels" : employee_sales.index.to_list(), "id" : "employee_sales" , "type" : "bar" },
    "ca_par_produit" : {"data" : CA_par_produit.total_quantity.to_list() , 
                        "labels" :  CA_par_produit.index.to_list(),  "id" : "CA_par_produit" , "type" : "bar" }, 
    "revenu_produit" : {"data" : revenu_produit.total_revenue.tolist() , "labels" : revenu_produit.product_name.to_list(), "id" : "revenu_produit" , "type" : "pie" },
    "crm_statut" : {"data" : CRM_statut.values.tolist() , "labels" : CRM_statut.index.tolist(), "id" : "crm_statut" , "type" : "pie"},
    "ca_par_employee" : {"data" :CA_par_employee.total_sales.tolist()  , "labels" : CA_par_employee.employee_name.tolist(), "id" : "ca_par_employee" , "type" : "bar"},
    "plus_marge_brutes" : {"data" : plus_marge_brute.values.tolist() , "labels" : plus_marge_brute.index.to_list(), "id" : "plus_marge_brutes" , "type" : "bar" },

  }

    return render(request, 'pages/dashboard.html', context)

def main(request):
    context = {
    'parent': 'pages',
    'segment': 'dashboard',
  }
    return render(request, 'pages/dashboard.html', context)

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home
                return redirect('index')  # Redirect to the index page or any other page
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'auth-signin.html', context)
@login_required(login_url='/accounts/auth-signin')
def factures(request):
    context = {
    'parent': 'pages',
    'segment': 'factures',
    "ca_par_produit" : {"data" : CA_par_produit.total_quantity.to_list() , 
                        "labels" :  CA_par_produit.index.to_list(),  "id" : "CA_par_produit" , "type" : "bar" }, 
    "revenu_produit" : {"data" : revenu_produit.total_revenue.tolist() , "labels" : revenu_produit.product_name.to_list(), "id" : "revenu_produit" , "type" : "pie" },

# --------------------------------------------------------     
    "average_sales_per_invoice" : average_sales_per_invoice.round(3) ,
    "chiffreaffaire" : chiffreaffaire.round(4) ,
    "nombreClient" : nombreClient ,
    'alldevis': alldevis,
    'sent_devis': sent_devis,
    'sale_orders': sale_orders,
    'done_saleorders': done_saleorders,
    'cancelled_sale_orders': cancelled_sale_orders,
    'sale_orders_with_invoice': sale_orders_with_invoice,
    'sale_orders_to_invoiced': sale_orders_to_invoiced,
    "command_statut" : {"data" : commandes_status.Percentage.tolist() , "labels" : commandes_status.Category.tolist(), "id" : "command_statut" , "type" : "pie"},
    "crm_statut" : {"data" : CRM_statut.values.tolist() , "labels" : CRM_statut.index.tolist(), "id" : "crm_statut" , "type" : "pie"},
    "facture_mois" : {"data" : facture_par_mois.values.tolist() , "labels" : facture_par_mois.index.tolist(), "id" : "nb_factures" , "type" : "line"},
    "facture_annee" : {"data" : facture_par_annee.values.tolist() , "labels" : facture_par_annee.index.tolist()},
    "facture_semestre" : {"data" : facture_par_semestre.values.tolist() , "labels" : facture_par_semestre.index.tolist()},
    "ca_client" : {"data" : CA_client.total_revenue.tolist() , "labels" : CA_client.index.to_list(), "id" : "ca_client" , "type" : "bar"},
    "client_saless" : {"data" : client_sales.sales.tolist() , "labels" : client_sales.date.to_list(), "id" : "client_saless" , "type" : "bar"},
    "NB_fac_par_client" : {"data" : nb_fac_par_client.values.tolist() , "labels" : nb_fac_par_client.index.to_list(), "id" : "NB_fac_par_client" , "type" : "bar"},
    "TOP_revenue_par_client" : {"data" : top_revenue_par_client.values.tolist() , "labels" : top_revenue_par_client.index.to_list(), "id" : "TOP_revenue_par_client" , "type" : "bar"},
    "MOINS_revenue_par_client" : {"data" : moins_revenue_par_client.values.tolist() , "labels" : moins_revenue_par_client.index.to_list(), "id" : "MOIN_revenue_par_client" , "type" : "bar"},
    "retention_MOIS" : {"data" : retention_mois.values.tolist() , "labels" : retention_mois.index.to_list(), "id" : "retention_MOIS" , "type" : "line"},
    "retention_ANNEE" : {"data" : retention_annee.values.tolist() , "labels" : retention_annee.index.to_list()},
    "retention_SEMESTRE" : {"data" : retention_semstre.values.tolist() , "labels" : retention_semstre.index.to_list()},
    'rt_mois': rt_mois,
    'rt_semestre': rt_semestre,
    'rt_annee': rt_annee,    


    }
    return render(request, 'pages/factures.html', context)

@login_required(login_url='/accounts/auth-signin')
def HR(request):
    context = {
    'parent': 'pages',
    'segment': 'HR',
    "ca_mois" : {"data" : CA_mois.tolist() , "labels" : CA_mois.index.to_list(), "id" : "ca_mois" , "type" : "line"},
    "ca_year" : {"data" : CA_year.tolist() , "labels" : CA_year.index.to_list()},
    "ca_quarter" : {"data" : CA_quarter.tolist() , "labels" : CA_quarter.index.to_list()},

    "ca_par_produit1" : {"data" : CA_par_produit1.total_quantity.to_list() , 
                        "labels" :  CA_par_produit1.index.to_list(),  "id" : "CA_par_produit1" , "type" : "bar" }, 
    "revenu_produit1" : {"data" : revenu_produit1.total_revenue.tolist() , "labels" : revenu_produit1.product_name.to_list(), "id" : "revenu_produit1" , "type" : "bar" },
    "revenue_by_category" : {"data" : revenue_by_product_category.values.tolist() , "labels" : revenue_by_product_category.index.to_list(), "id" : "revenue_by_category" , "type" : "bar" },
    "total_quantity_sold_category" : {"data" : total_quantity_sold_by_product_category.values.tolist() , "labels" : total_quantity_sold_by_product_category.index.to_list(), "id" : "total_quantity_sold_category" , "type" : "bar" },
    "plus_marge_brutes" : {"data" : plus_marge_brute.values.tolist() , "labels" : plus_marge_brute.index.to_list(), "id" : "plus_marge_brutes" , "type" : "bar" },
    "moins_marge_brutes" : {"data" : moins_marge_brute.values.tolist() , "labels" : moins_marge_brute.index.to_list(), "id" : "moins_marge_brutes" , "type" : "bar" },
    #-------------------------------------------------------- 
    "headcount" : headcount ,
    "department_headcount" : department_headcount ,
    "job_title_distribution" :  job_title_distribution ,
    "employe_performance" : {"data" : employee_performance.amount_total.tolist() , "labels" : employee_performance.employee_name.to_list(), "id" : "employe_performance" , "type" : "bar" },
    "revenu_departement" : {"data" : revenu_par_departement.amount_total.tolist() , "labels" : revenu_par_departement.department_name.to_list(), "id" : "revenu_departement" , "type" : "bar" },
    "employe_par_dep" : {"data" : employes_par_dep.values.tolist() , "labels" : employes_par_dep.index.to_list(), "id" : "employe_par_dep" , "type" : "bar" },
    "jobs_distribution" : {"data" : job_distribution.values.tolist() , "labels" : job_distribution.index.to_list(), "id" : "jobs_distribution" , "type" : "bar" },

    
  }
    return render(request, 'pages/HR.html', context)

# @login_required(login_url='/accounts/auth-signin')
def notifications(request):
    context = {
    'parent': 'pages',
    'segment': 'notifications'
  }
    return render(request, 'pages/notifications.html', context)

# @login_required(login_url='/accounts/auth-signin')
def user_profile(request):
    context = {
    'parent': 'pages',
    'segment': 'user_profile'
    
  }
    return render(request, 'pages/user.html', context)

# @login_required(login_url='/accounts/auth-signin')
def formations(request):
    context = {
    'parent': 'pages',
    'segment': 'formations',
    "ca_mois" : {"data" : CA_mois.tolist() , "labels" : CA_mois.index.to_list(), "id" : "ca_mois" , "type" : "line"},
    "ca_year" : {"data" : CA_year.tolist() , "labels" : CA_year.index.to_list()},
    "ca_quarter" : {"data" : CA_quarter.tolist() , "labels" : CA_quarter.index.to_list()},
    #--------------------------------------------------------
    "ca_par_produit1" : {"data" : CA_par_produit1.total_quantity.to_list() , 
                        "labels" :  CA_par_produit1.index.to_list(),  "id" : "CA_par_produit1" , "type" : "bar" }, 
    "revenu_produit1" : {"data" : revenu_produit1.total_revenue.tolist() , "labels" : revenu_produit1.product_name.to_list(), "id" : "revenu_produit1" , "type" : "bar" },
    "revenue_by_category" : {"data" : revenue_by_product_category.values.tolist() , "labels" : revenue_by_product_category.index.to_list(), "id" : "revenue_by_category" , "type" : "bar" },
    "total_quantity_sold_category" : {"data" : total_quantity_sold_by_product_category.values.tolist() , "labels" : total_quantity_sold_by_product_category.index.to_list(), "id" : "total_quantity_sold_category" , "type" : "bar" },
    "plus_marge_brutes" : {"data" : plus_marge_brute.values.tolist() , "labels" : plus_marge_brute.index.to_list(), "id" : "plus_marge_brutes" , "type" : "bar" },
    "moins_marge_brutes" : {"data" : moins_marge_brute.values.tolist() , "labels" : moins_marge_brute.index.to_list(), "id" : "moins_marge_brutes" , "type" : "bar" },
    "nb_product" : nb_product , 

  }
    return render(request, 'pages/formations.html', context)


  



def all_invoices(request):
  if request.method == "GET" :
     print(request.GET)

  form = InvoiceForm()
  invoices= Invoice.objects.all()
  print(invoices[0].customer.first_name)
  return render(request, 'get_invoices.html', context={'invoices' : invoices, 'form': form})


def display_dropdown(request):
    try:
        df = invoices_df
        partner_names = df['partner_name'].tolist()
    except Exception as e:
        partner_names = []  # Handle error or return empty list

    return render(request, 'dashboard.html', {'partner_names': partner_names})