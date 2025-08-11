import requests
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("✅ Data successfully fetched from API:", data)

    key_name = "post:1"
    for k, v in data.items():
        r.hset(key_name, k, json.dumps(v) if isinstance(v, (dict, list)) else v)

    print(f"✅ Data stored in Redis with key '{key_name}'.")

    stored_data = r.hgetall(key_name)
    decoded_data = {k.decode(): json.loads(v) if v.startswith(b'[') or v.startswith(b'{') else v.decode()
                    for k, v in stored_data.items()}

    print("📦 Data retrieved from Redis:")
    print(decoded_data)
else:
    print("❌ Failed to fetch data from API.")
