from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# This simple Flask application simulates a basic microservice.
# Full-stack developers often build such services which are then containerized
# and deployed to platforms like Kubernetes.

@app.route('/')
def home():
    # In Kubernetes, application configuration is often managed via ConfigMaps or Secrets
    # and exposed to containers as environment variables. This allows easy configuration
    # changes without rebuilding the application image.
    app_name = os.environ.get('APP_NAME', 'FullStackApp')
    version = os.environ.get('APP_VERSION', '1.0.0')
    message = f"Hello from {app_name} (v{version})!"
    return jsonify({"message": message, "host": request.host})

@app.route('/health')
def health_check():
    # Health check endpoints are crucial for Kubernetes.
    # They allow Kubernetes to determine if a container is alive (liveness probe)
    # and ready to serve traffic (readiness probe), enabling robust deployments and scaling.
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    # The port an application listens on is often configured via environment variables
    # in containerized environments, allowing flexible deployment across different
    # Kubernetes Pods and Services without hardcoding.
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting {os.environ.get('APP_NAME', 'FullStackApp')} on port {port}")
    app.run(host='0.0.0.0', port=port)
