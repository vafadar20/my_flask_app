from flask import Flask, request, render_template_string

app = Flask(__name__)

# قالب HTML ساده برای فرم
html = """
<!doctype html>
<html>
  <head>
    <title>BMI Calculator</title>
    <meta charset="utf-8">
  </head>
  <body style="font-family:Tahoma; text-align:center; margin-top:50px;">
    <h2>محاسبه شاخص توده بدنی (BMI)</h2>
    <form method="post">
      <label>قد (سانتی‌متر):</label>
      <input type="number" name="height" step="0.1" required><br><br>
      <label>وزن (کیلوگرم):</label>
      <input type="number" name="weight" step="0.1" required><br><br>
      <button type="submit">محاسبه</button>
    </form>
    {% if bmi %}
      <h3>شاخص BMI شما: {{ bmi }}</h3>
      <p>{{ status }}</p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    status = None
    if request.method == "POST":
        height = float(request.form["height"]) / 100
        weight = float(request.form["weight"])
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            status = "شما لاغر هستید"
        elif bmi < 25:
            status = "وزن نرمال دارید"
        elif bmi < 30:
            status = "اضافه وزن دارید"
        else:
            status = "چاقی"

    return render_template_string(html, bmi=bmi, status=status)

if __name__ == "__main__":
    app.run(debug=True)
