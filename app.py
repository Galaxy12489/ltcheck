from flask import Flask, render_template, request

app = Flask(__name__)

# Список моделей ноутбуков
laptops = [
    {"name": "ASUS VivoBook 15", "price": "45,000 - 60,000"},
    {"name": "Lenovo IdeaPad 3", "price": "50,000 - 70,000"},
    {"name": "HP Pavilion 15", "price": "55,000 - 75,000"},
    {"name": "Acer Aspire 5", "price": "40,000 - 65,000"},
    {"name": "Dell Inspiron 15", "price": "60,000 - 80,000"},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_laptop = None
    if request.method == 'POST':
        selected_laptop = request.form.get('laptop')
    return render_template('index.html', laptops=laptops, selected_laptop=selected_laptop)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)