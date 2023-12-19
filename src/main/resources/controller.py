# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Variable to keep track of the model state
# model_running = False

# @app.route('/')
# def index():
#     return render_template('controller')

# @app.route('/control', methods=['GET'])
# def control_model():
#     global model_running

#     command = request.args.get('command')

#     if command == 'start':
#         if not model_running:
#             # Start your Python model here (replace 'your_model_command' with the actual command)
#             subprocess.Popen(['python', r'c:\Users\smhrd\Desktop\kdy\DCX_FINAL\src\main\resources\CCTV4.py'], shell=True)   
#             model_running = True
#     elif command == 'stop':
#         # Stop your Python model here (replace 'your_stop_command' with the actual command)
#         subprocess.Popen(['stop'], shell=True)
#         model_running = False

#     return jsonify({'status': 'success', 'model_running': model_running})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

# @app.route('/python')
# def python():
#     # Implement logic for /python route
#     return render_template('streaming.html')

# @app.route('/python2')
# def python2():
#     # Implement logic for /python2 route
#     return render_template('streaming.html')

# @app.route('/python3')
# def python3():
#     # Implement logic for /python3 route
#     return render_template('streaming.html')

# @app.route('/python4')
# def python4():
#     # Implement logic for /python4 route
#     return render_template('streaming.html')