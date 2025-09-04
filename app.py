from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    error = None
    zodiac = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'reset':
            return redirect(url_for('home'))
        elif action == 'show':
            try:
                month = int(request.form['month'])
                day = int(request.form['day'])
                datetime(year=2024, month=month, day=day)
            except(ValueError,KeyError):
                error = 'Invalid number'
            else:
                zodiac = determine_zodiac(month,day)

    return render_template('index.html', zodiac=zodiac, error=error)

def determine_zodiac(month,day):
    match month:
        case 1:
            if day<=19: zodiac = ('Capricorn')
            else: zodiac = ('Aquarius')
        case 2:
            if day<=18: zodiac = ('Aquarius')
            else: zodiac = ('Pisces')
        case 3:
            if day<=20: zodiac = ('Pisces')
            else: zodiac = ('Aries')
        case 4:
            if day<=19: zodiac = ('Aries')
            else: zodiac = ('Taurus')
        case 5:
            if day<=20: zodiac = ('Taurus')
            else: zodiac = ('Gemini')
        case 6:
            if day<=21: zodiac = ('Gemini')
            else: zodiac = ('Cancer')
        case 7:
            if day<=22: zodiac = ('Cancer')
            else: zodiac = ('Leo')
        case 8:
            if day<=22: zodiac = ('Leo')
            else: zodiac = ('Virgo')
        case 9:
            if day<=22: zodiac = ('Virgo')
            else: zodiac = ('Libra')
        case 10:
            if day<=23: zodiac = ('Libra')
            else: zodiac = ('Scorpio')
        case 11:
            if day<=21: zodiac = ('Scorpio')
            else: zodiac = ('Sagittarius')
        case 12:
            if day<=21: zodiac = ('Sagittarius')
            else: zodiac = ('Capricorn')
    return zodiac

if __name__ == '__main__':
    app.run(debug=True)