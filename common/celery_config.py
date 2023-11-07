
# Broker settings
broker_url = 'pyamqp://guest@rabbitmq//'

# Using RPC as the result backend
result_backend = 'rpc://'

# Task serialization format
task_serializer = 'json'

# Result serialization format
result_serializer = 'json'

# List of modules to import when the Celery worker starts
imports = ('tasks',)

# # Adjustments for worker performance
worker_prefetch_multiplier = 4  # Default is 4, lower for fairer task distribution but potentially higher latency
task_acks_late = True  # Acknowledge task after it's done to prevent loss on sudden worker death

# # Task prioritization (requires tasks to have a 'priority' option set when sent)
task_queue_max_priority = 10

# Task routes
task_routes = {
    'worker.tasks.add': {'queue': 'arithmetic_with_priority'},
    'worker.tasks.multiply': {'queue': 'arithmetic_with_priority'},
    'worker.tasks.upper_case': {'queue': 'text_with_priority'}
}

