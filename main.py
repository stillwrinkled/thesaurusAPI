from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def about(word):
    df = pd.read_csv("dictionary.csv")
    # definition1 = str(df[df['word'] == word]['definition'])
    # definition_series = df[df['word'] == word]['definition']
    # definition1 = definition_series.values[0] if definition_series.size > 0 else "Not found"
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    return {"definition": definition,
            "word": word.upper()}


if __name__ == "__main__":
    app.run(debug=True)
