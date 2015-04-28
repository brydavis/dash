from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import SearchForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        session['company'] = form.company.data
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form,
                           company=session.get('company'))



@main.route('/charts/', methods=['GET', 'POST'])
def charts():
    # form = SearchForm()
    # if form.validate_on_submit():
        # session['company'] = form.company.data
        # return redirect(url_for('main.index'))
    return render_template(
    	'charts.html', 
    	# form=form,
		# company=session.get('company'),
	)

@main.route('/tables/', methods=['GET', 'POST'])
def tables():
    return render_template(
    	'tables.html', 
	)

@main.route('/blank/', methods=['GET', 'POST'])
def blankpage():
    return render_template(
    	'blank-page.html', 
	)

@main.route('/grid/', methods=['GET', 'POST'])
def grid():
    return render_template(
    	'bootstrap-grid.html', 
	)

@main.route('/forms/', methods=['GET', 'POST'])
def form_examples():
    return render_template(
    	'forms.html', 
	)

@main.route('/elements/', methods=['GET', 'POST'])
def elements():
    return render_template(
    	'bootstrap-elements.html', 
	)

@main.route('/404/', methods=['GET', 'POST'])
def not_found():
    return render_template(
        '404.html', 
    )

@main.route('/500/', methods=['GET', 'POST'])
def internal_error():
    return render_template(
        '500.html', 
    )