from flask import Flask, render_template, request, url_for
import logging
from dbase import *

app = Flask(__name__)

nodata = [['','No Data Found for this phone number, please check phone number and try again','','']]

@app.route('/', methods=['GET','POST'])
def search():
	if request.method == 'POST':
		try:
			mobilenumber = request.form.get('mobile')
			if mobilenumber.isdigit() == False:
				return render_template('search.html', sessiondata=nodata)
			mobilenumber = int(request.form.get('mobile'))
			newarray = []
			for entry in patientlist:
				if entry[0] == mobilenumber:
					newarray.append(entry)
			if newarray == []:
				return render_template('search.html', sessiondata=nodata)
			return render_template('search.html', sessiondata=newarray)
			newarray = []
		except:
			pass
	return render_template('search.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8788', debug=True)
