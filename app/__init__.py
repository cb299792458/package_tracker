from flask import Flask, render_template, redirect, url_for
from .config import Config
from .shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/',methods=['GET'])
def index():
    return 'Package Tracker Home'

@app.route('/new_package',methods=['GET','POST'])
def new_package():
    form = ShippingForm()

    if form.validate_on_submit():

        return redirect(url_for('.index'))

    return render_template('shipping_request.html',form=form)