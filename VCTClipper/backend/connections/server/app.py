import eventlet
eventlet.monkey_patch()

from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from controller.worker.worker import save_worker, get_workers_backend
from controller.stream.get_livedata import get_channel_data, get_channel_id_by_handle
from connections.server.manager.node_manager import NodeManager

app = Flask(__name__)
CORS(app)  
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')
node_manager = NodeManager()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/add_worker", methods=['POST'])
def add_worker():
    data = request.get_json()
    print(data)
    name = data.get('name')
    channel_handle = data.get('channelHandle')
    media_type = data.get('mediaType')

    if not all([name, channel_handle, media_type]):
        return jsonify({"error": "Missing data"}), 400

    save_worker(name, channel_handle, media_type)

    return jsonify({"message": "Worker added successfully"}), 201

@app.route("/get_worker/all", methods=['GET'])
def get_workers():
    workers = get_workers_backend()
    return jsonify(workers)

@app.route("/get_channel_by_handle/<handle>", methods=['GET'])
def get_channel_by_handle(handle : str):
    channel_data = get_channel_data(get_channel_id_by_handle(handle))
    return jsonify({"name":channel_data[0], "img_url":channel_data[1]})


@app.route('/start_node/<int:node_id>', methods=['GET'])
def start_node(node_id):
    success, result = node_manager.start_node(node_id)
    
    if not success:
        return jsonify(success=False, message=result), 400

    socketio.emit('status_update', {'pid': node_id, 'status': 'starting'})
    socketio.emit('status_update', {'pid': node_id, 'status': 'running'})
    return jsonify(success=True)

@app.route('/stop_node/<int:node_id>', methods=['GET'])
def stop_node(node_id):
    success, result = node_manager.stop_node(node_id)
    
    if not success:
        return jsonify(success=False, message=result), 400

    socketio.emit('status_update', {'pid': node_id, 'status': 'stopping'})
    socketio.emit('status_update', {'pid': node_id, 'status': 'stopped'})
    return jsonify(success=True)

# RUN = flask --app app run
# RUN from root = flask --app connections.server.app run
