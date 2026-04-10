from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    original, result, score = "", "", 100
    if request.method == 'POST':
        original = request.form.get('metin', '')
        result = original.replace("herkez", "herkes").replace("link", "bağlantı")
        score = 90
    return render_template_string("""
    <h1>TÜRKÇE ANALİZ</h1>
    <form method="POST"><textarea name="metin">{{ original }}</textarea><button type="submit">ANALİZ ET</button></form>
    {% if result %}<h3>Sonuç: {{ result }}</h3>{% endif %}
    """, original=original, result=result, score=score)

if __name__ == '__main__':
    app.run()
