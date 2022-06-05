from pickle import NONE, TRUE
from app import app
from flask import render_template,request,redirect, url_for
from markupsafe import escape
from analyst import Analyst
from reader import Reader
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
        r1 = Reader()
        r1.Read_Reviews(product_id,product_name,True) 
        return redirect('/products')
    else: return render_template("subpages/extract_form.html.jinja")

@app.route('/products')
def render_products(products_list =''):
    products_list = os.listdir('./Data')
    return render_template('subpages/products.html.jinja', products=products_list)

@app.route('/products:<string:product_name>')
def product(product_name):
    json = 'Data/'+product_name+'/'+product_name+".json"
    plot_path = 'Data/'+product_name+'/'+product_name+".png"
    analyst = Analyst()
    data = analyst.return_data(json)
    return render_template("subpages/product.html.jinja", product_name=product_name, data=data,url=plot_path)
    
@app.errorhandler(404)
def not_found(e):
    return render_template("subpages/404.html.jinja")