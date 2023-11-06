from prometheus_client import CollectorRegistry, Gauge, generate_latest, start_http_server

# Create a metric
g = Gauge('my_metric', 'My custom metric')

# Start the Prometheus HTTP server on port 8000
start_http_server(8000)

# Increment the metric
g.inc()

# You can periodically update the metric values in your application

# Export the metrics to the local endpoint
registry = CollectorRegistry()
data = generate_latest(registry)
