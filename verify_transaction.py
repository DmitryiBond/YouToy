import redis
import time
import requests
from consts import RedisKeys

# Configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
WEB_URL = "http://localhost:8000"

def verify_redis_connection():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        r.ping()
        print(f"[OK] Connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
        return r
    except Exception as e:
        print(f"[FAIL] Could not connect to Redis: {e}")
        return None

def main():
    print("=== YouToy Verification Script ===")
    
    # 1. Check Redis
    r = verify_redis_connection()
    if not r:
        return

    # 2. Simulate Balance Update (Transaction)
    test_wallet = "simulate_verify"
    print(f"\n[TEST] Simulating transaction for wallet '{test_wallet}'...")
    
    # Set initial state
    r.set(f'{test_wallet}{RedisKeys.LOCAL_BALANCE_SUFFIX}', 0)
    r.set(f'{test_wallet}{RedisKeys.FACTOR_SUFFIX}', 1.0)
    
    # Update "current" balance to trigger diff
    r.set(f'{test_wallet}{RedisKeys.BALANCE_SUFFIX}', 50.0)
    
    print(f"      Set balance=50.0, local=0.0. Expecting 'Got new balance' log in toy.py.")
    print("      (Check 'docker-compose logs toy' or 'docker-compose logs python')")

    # 3. Check Web UI
    print(f"\n[TEST] Checking Web UI at {WEB_URL}...")
    try:
        resp = requests.get(WEB_URL)
        if resp.status_code == 200:
            print(f"[OK] Web UI is reachable (Status 200).")
        else:
            print(f"[WARN] Web UI returned status {resp.status_code}")
    except Exception as e:
        print(f"[FAIL] Web UI unreachable: {e}")

    # 4. Clean up
    print(f"\n[INFO] verification completed. To see logs run: docker-compose logs -f")

if __name__ == "__main__":
    main()
