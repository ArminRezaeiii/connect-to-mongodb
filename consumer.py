import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('my_channel')

print("Waiting for messages...")

for message in p.listen():
    if message['type'] == 'message':
        data = json.loads(message['data'])
        print(f"Received and processing message: {data}")
        # You can add your processing logic here
