from flask import Flask, render_template

app = Flask(__name__)

# 初期のHP値
hp_value = 100
mp_value = 50

@app.route('/')
def index():
    return render_template('index_async.html', hp=hp_value,mp=mp_value)

@app.route('/apply_damage')
def apply_damage():
    global hp_value
    # ダメージ量（ここでは10と仮定）
    damage_amount = 10
    # HPを減少させる
    hp_value = max(0, hp_value - damage_amount)
    return str(hp_value)

@app.route('/apply_healing')
def apply_healing():
    global hp_value
    # 回復量（ここでは10と仮定）
    healing_amount = 10
    # HPを増加させる
    max_hp = 100
    hp_value = min(max_hp, hp_value + healing_amount)
    return str(hp_value)

@app.route('/mana_consumption')
def mana_consumption():
    global mp_value
    # ダメージ量（ここでは10と仮定）
    consumption_amount = 10
    # MPを減少させる
    mp_value = max(0, mp_value - consumption_amount)
    return str(mp_value)

@app.route('/mana_healing')
def mana_healing():
    global mp_value
    # 回復量（ここでは10と仮定）
    healing_mp = 10
    # MPを増加させる
    max_mp = 50
    mp_value = min(max_mp, mp_value + healing_mp)
    return str(mp_value)

if __name__ == '__main__':
    app.run()
