from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from pixela_control import post_pixel

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class HoursForm(FlaskForm):
    hours = IntegerField("For how many hours did you code?",
                         [DataRequired(message="Please enter a value."),
                          NumberRange(min=1, max=23, message="Only values between 1 and 23.")])
    submit = SubmitField("Post Pixel")


@app.route("/", methods = ['POST', 'GET'])
def home():
    form = HoursForm()
    if form.validate_on_submit():
        post_pixel(str(form.hours.data))
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
