from flask import Flask, render_template
from controllers.member_controller import members_blueprint
from controllers.fitness_class_controller import fitness_classes_blueprint
from controllers.booking_controller import bookings_blueprint
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(fitness_classes_blueprint)
app.register_blueprint(members_blueprint)
metrics = PrometheusMetrics(app)
@app.route('/')
def home():
    return render_template('index.html', current_page = 'Home', title='Home')

@app.route('/health')
def health():
    return "Healthy", 200

if __name__ == '__main__':
    app.run(debug=True)

