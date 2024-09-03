import subprocess

class NodeManager:
    def __init__(self):
        self.node_processes = {}

    def start_node(self, node_id, process):
        if node_id in self.node_processes:
            return False, "Node is already running"

        process = subprocess.Popen(process) # process = subprocess.Popen(['python', 'hello.py'])
        self.node_processes[node_id] = process
        return True, process

    def stop_node(self, node_id):
        if node_id not in self.node_processes:
            return False, "Node is already stopped"

        process = self.node_processes.pop(node_id)
        process.terminate()
        process.wait()
        return True, process