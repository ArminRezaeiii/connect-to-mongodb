import redis
import time
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def publish_messages():
    for i in range(10):
        message = {
            'id': i,
            'text': f'Message number {i}'
        }
        # Publish message to the channel "my_channel"
        r.publish('my_channel', json.dumps(message))
        print(f'Message sent: {message}')
        time.sleep(1)

if __name__ == "__main__":
    publish_messages()
