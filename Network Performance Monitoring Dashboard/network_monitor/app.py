from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Simulate network performance data
def get_network_metrics():
    return {
        "latency": random.randint(10, 100),  # Simulated latency in ms
        "packet_loss": random.uniform(0, 1)  # Simulated packet loss as a percentage
    }

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/metrics')
def metrics():
    data = get_network_metrics()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)