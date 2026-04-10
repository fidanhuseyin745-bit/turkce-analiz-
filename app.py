from flask import Flask, render_template_string, request

app = Flask(__name__)

# Buraya istediğin kadar yanlış/doğru kelime ekleyebilirsin
SOZLUK = {
    "herkez": "herkes",
    "yada": "ya da",
    "gelicek": "gelecek",
    "gidicek": "gidecek",
    "şuan": "şu an",
    "yalnış": "yanlış",
    "yanlız": "yalnız"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    original = ""
    result = ""
    score = 100
    if request.method == 'POST':
        original = request.form.get('metin', '')
        kelimeler = original.split()
        yeni_kelimeler = []
        hata_sayisi = 0
        
        for kelime in kelimeler:
            temiz_kelime = kelime.lower().strip(".,!?")
            if temiz_kelime in SOZLUK:
                yeni_kelimeler.append(SOZLUK[temiz_kelime])
                hata_sayisi += 1
            else:
                yeni_kelimeler.append(kelime)
        
        result = " ".join(yeni_kelimeler)
        score = max(0, 100 - (hata_sayisi * 10))

    return render_template_string("""
    <body style="font-family:sans-serif; background:#121212; color:#00ff00; text-align:center; padding-top:50px;">
        <div style="background:#1e1e1e; display:inline-block; padding:30px; border-radius:15px; border:1px solid #00ff00;">
            <h1>💻 TÜRKÇE ANALİZ MOTORU</h1>
            <form method="POST">
                <textarea name="metin" style="width:300px; height:100px; background:#252525; color:#00ff00; border:1px solid #00ff00; padding:10px;">{{ original }}</textarea><br><br>
                <button type="submit" style="background:#00ff00; color:black; padding:10px 20px; font-weight:bold; cursor:pointer;">ANALİZ ET</button>
            </form>
            {% if result %}
                <div style="margin-top:20px; text-align:left;">
                    <p style="color:white;"><b>Orijinal:</b> {{ original }}</p>
                    <p><b>Düzenlenmiş:</b> {{ result }}</p>
                    <p style="color:yellow;"><b>Puan:</b> %{{ score }}</p>
                </div>
            {% endif %}
        </div>
    </body>
    """, original=original, result=result, score=score)

if __name__ == '__main__':
    app.run()
