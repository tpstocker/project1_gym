from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.location_controller import locations_blueprint
from controllers.instructor_controller import instructors_blueprint
from controllers.activity_controller import activities_blueprint
from controllers.booking_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(instructors_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)