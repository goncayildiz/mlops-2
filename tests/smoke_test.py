import requests
import sys

def smoke_test():
    url = "http://localhost:5000/health"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ SMOKE TEST PASSED: Service is Healthy!")
            sys.exit(0)
        else:
            print(f"❌ SMOKE TEST FAILED: Status Code {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ SMOKE TEST FAILED: Connection Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    smoke_test()