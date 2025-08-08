from flask import Flask, render_template, request

app = Flask(__name__)

def get_optimal_dual_bar_combinations(bar1, bar2, required_area):
    section_table = {
        "HA6":  [0.28], "HA8":  [0.50], "HA10": [0.79], "HA12": [1.13],
        "HA14": [1.54], "HA16": [2.01], "HA20": [3.14], "HA25": [4.91],
        "HA32": [8.04], "HA40": [12.57]
    }

    if bar1 not in section_table or bar2 not in section_table:
        return "Erreur : un des types de barre n’est pas reconnu."

    unit_area_bar1 = section_table[bar1][0]
    unit_area_bar2 = section_table[bar2][0]

    combinations = []
    for i in range(10):
        for j in range(10):
            if i + j == 0 or i + j > 9:
                continue
            total_area = i * unit_area_bar1 + j * unit_area_bar2
            if total_area >= required_area:
                combinations.append((i, j, total_area))

    if not combinations:
        return "❌ Aucune combinaison valide."

    min_total = min(i + j for i, j, _ in combinations)
    optimal = [c for c in combinations if c[0] + c[1] == min_total]

    result = f"Surface demandée : {required_area} cm²\n"
    result += f"Barres : {bar1} et {bar2}\n"
    for i, j, a in optimal:
        result += f" - {i} x {bar1} + {j} x {bar2} → {a:.2f} cm²\n"
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        bar1 = request.form['bar1']
        bar2 = request.form['bar2']
        area = float(request.form['area'])
        result = get_optimal_dual_bar_combinations(bar1, bar2, area)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
