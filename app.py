from flask import Flask, request, redirect, render_template

app = Flask(__name__)
masked_urls = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        real_url = request.form["real_url"]
        alias = request.form["alias"]

        # Save alias mapping
        masked_urls[alias] = real_url
        masked_link = request.host_url + alias
        return render_template("index.html", masked_link=masked_link)

    return render_template("index.html", masked_link=None)

@app.route("/<alias>")
def masked(alias):
    if alias in masked_urls:
        return redirect(masked_urls[alias])
    return "Alias not found", 404

if __name__ == "__main__":
    app.run(debug=True)
