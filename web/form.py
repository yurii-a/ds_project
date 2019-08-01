from flask import (Flask, render_template, request)

from web.salary_prediction import SalaryModel

app = Flask(__name__)
model = SalaryModel()


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/survey', methods=('GET', 'POST'))
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        age = request.form['age']
        country = request.form['country']
        industry = request.form['industry']
        role = request.form['role']
        experience = request.form['experience']
        activities = request.form.to_dict(flat=False)['activities']

        sample = model.form_input_to_sample(age, country, industry, role, experience, activities)
        (salary_index, dist) = model.predict(sample)
        return render_template('prediction.html', salary=salary_index, salary_distribution=dist)


@app.route('/recommendation', methods=('GET', 'POST'))
def recommendation():
    if request.method == 'GET':
        return render_template('rec_form.html')
    if request.method == 'POST'():
        return render_template('recommendation.html')


if __name__ == '__main__':
    app.run(debug=True)
