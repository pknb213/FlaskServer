from FlaskServer import app
import os

if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(debug=True, host="0.0.0.0", port=5001)
