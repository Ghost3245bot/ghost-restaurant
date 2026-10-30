from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/order", methods=["POST"])
def order():
    food = request.form["food"]
    quantity = int(request.form["quantity"])
    location = request.form["location"]

    menu = {
        "Chicken": 8000,
        "Burger": 5000,
        "Pizza": 12000
    }

    price = menu[food]
    total = price * quantity

    return f"""
    <h1>GHOST RESTAURANT RECEIPT</h1>
    <p>Food: {food}</p>
    <p>Quantity: {quantity}</p>
    <p>Total: TSh {total}</p>
    <p>Delivery: {location}</p>
    """
if __name__ == "__main__":
    app.run(debug=True)
