# [Django Black Dashboard](https://appseed.us/product/black-dashboard/django/)

Open-source **[Django Dashboard](https://appseed.us/admin-dashboards/django/)** provided by `AppSeed` on top of **Black Dashboard**, an open-source `Bootstrap` Design from `Creative-Tim`.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 [Django Black Dashboard](https://appseed.us/product/black-dashboard/django/) - `Product page`
- 👉 [Django Black Dashboard](https://django-black-dashboard.appseed-srv1.com/) - `LIVE Demo`

<br /> 

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [PRO Version](https://appseed.us/product/black-dashboard-pro/django/)    | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ **Django 4.2.9**                    | **Everything in Free**, plus:                                                          | **Everything in PRO**, plus:         |
| ✓ Best Practices                      | ✅ **Premium Bootstrap 5 Design**                                                      | ✅ **1mo Custom Development**       | 
| ✓ Bootstrap 5, `Material` Design      | ✅ `OAuth` Google, GitHub                                                              | ✅ **Team**: PM, Developer, Tester  |
| ✓ `CI/CD` Flow via Render             | ✅ `API`, **[Charts](https://django-black-pro.onrender.com/chart/)**                   | ✅ Weekly Sprints                   |
| ✓ `Docker`                            | ✅ **[DataTables](https://django-black-pro.onrender.com/tables/)** (Filters, Export)   | ✅ Technical SPECS                  |
| -                                     |✅ **Celery**                                                                            | ✅ Documentation                    |
| -                                     | ✅ **Media Files Manager**                                                              | ✅ **30 days Delivery Warranty**    |
| -                                     | ✅ **Extended User Profiles**                                                           |  -                                   |
| -                                     | ✅ `Private REPO Access`                                                                |  -                                   |
| -                                     | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/)                     |  -                                   |
| -                                     | ✅ Deployment Assistance                                                                |  -                                   |
| ------------------------------------  | ------------------------------------                                                    | ------------------------------------|
| ✓ [LIVE Demo](https://django-material-dash2.onrender.com)  | 🚀 [LIVE Demo](https://django-black-pro.onrender.com/) | 🛒 `Order`: **[$3,999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |     


![Django Admin Black - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/196730732-dda1794b-93ce-48cb-bc5c-182411495512.png)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-black-dashboard.git
$ cd django-black-dashboard
```

<br />

> 👉 Install modules via `VENV`.


```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Edit the `.env` using the template `.env.sample`. 

```env

# True for development, False for production
DEBUG=True

```

<br />

> 👉 Set Up Database

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python3 manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python3 manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py    # Project Configuration  
   |    |-- urls.py        # Project Routing
   |
   |-- home/
   |    |-- views.py       # APP Views 
   |    |-- urls.py        # APP Routing
   |    |-- models.py      # APP Models 
   |    |-- tests.py       # Tests  
   |
   |-- requirements.txt    # Project Dependencies
   |
   |-- env.sample          # ENV Configuration (default values)
   |-- manage.py           # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize 

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The theme used to style this starter provides the following files: 

```bash
# This exists in ENV: LIB/admin_black
< UI_LIBRARY_ROOT >                      
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- auth-signin.html     # Sign IN Page
   |    |    |-- auth-signup.html     # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |
   |    |-- pages/       
   |         |-- dashboard.html       # Dashboard page
   |         |-- user.html            # Settings  Page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

> For instance, if we want to **customize the dashboard.html** these are the steps:

- ✅ `Step 1`: create the `templates` DIRECTORY inside the `ROOT` directory
- ✅ `Step 2`: configure the project to use this new template directory
  - `core/settings.py` TEMPLATES section
- ✅ `Step 3`: copy the `dashboard.html` from the original location (inside your ENV) and save it to the `templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_black_pro/pages/dashboard.html`
  - Destination PATH: `<PROJECT_ROOT>templates/pages/dashboard.html`

> To speed up all these steps, the **codebase is already configured** (`Steps 1, and 2`) and a `custom dashboard` can be found at this location:

`templates/pages/custom-dashboard.html` 

By default, this file is unused because the `theme` expects `dashboard.html` (without the `custom-` prefix). 

In order to use it, simply rename it to `dashboard.html`. Like this, the default version shipped in the library is ignored by Django. 

In a similar way, all other files and components can be customized easily.

<br />

## Recompile SCSS  

The SCSS/CSS files used to style the Ui are saved in the `static/assets` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn # install modules
$ # # edit variables 
$ vi static/assets/scss/black-dashboard/custom/_variables.scss 
$ gulp # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$default:       #344675 !default; // EDIT for customization
$primary:       #e14eca !default; // EDIT for customization
$secondary:     #f4f5f7 !default; // EDIT for customization
$success:       #00f2c3 !default; // EDIT for customization
$info:          #1d8cf8 !default; // EDIT for customization
$warning:       #ff8d72 !default; // EDIT for customization
$danger:        #fd5d93 !default; // EDIT for customization
$black:         #222a42 !default; // EDIT for customization
```

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

---
[Django Black Dashboard](https://appseed.us/product/black-dashboard/django/) - **Django** starter provided by **[AppSeed](https://appseed.us/)**
