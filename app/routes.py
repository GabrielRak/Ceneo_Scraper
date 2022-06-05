from pickle import NONE, TRUE
from app import app
from flask import render_template,request,redirect, url_for
import shutil
from markupsafe import escape
from app.functionalities.analyst import Analyst
from app.functionalities.reader import Reader
import os 

@app.route('/')
@app.route('/index')
def index():
    return render_template("subpages/home.html.jinja")

@app.route('/extract_form', methods = ['GET', 'POST'])
def render_form():
    if  request.method == "POST":
        product_id = request.form.get("product_id")
        product_name = request.form.get("product_name")
        if len(product_name) == 0: product_name = "unnamed"
        r1 = Reader()
        r1.Read_Reviews(product_id,product_name,True) 
        return redirect('/products')
    else: return render_template("subpages/extract_form.html.jinja")

@app.route('/products', methods = ['GET','POST'])
def render_products(products_list =''):
    if not os.path.exists('app/static/data'): products_list = ""
    else: 
        products_list = os.listdir('app/static/data')
        if request.method =="POST":
            to_delete = request.form.get("product")
            path = 'app/static/data/'+to_delete
            shutil.rmtree(path)
            return redirect('/products')
    return render_template('subpages/products.html.jinja', products=products_list)

@app.route('/products:<string:product_name>')
def product(product_name):
    json = 'app/static/data/'+product_name+'/'+product_name+".json"
    plot = '../../static/data/'+product_name+'/'+product_name+".png"
    analyst = Analyst()
    data = analyst.return_data(json)
    return render_template("subpages/product.html.jinja", product_name=product_name, data=data,plot=plot)
    
@app.errorhandler(404)  
def not_found(e):
    return render_template("subpages/404.html.jinja")