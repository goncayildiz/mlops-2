"""
Smoke Test Module.
Performs a basic health check on the running service.
"""
import sys
import requests

def smoke_test():
    """
    Connects to the health endpoint to verify the service is up.
    """
    url = "http://localhost:5000/health"
    try:
        # Timeout eklendi (5 saniye)
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("✅ SMOKE TEST PASSED: Service is Healthy!")
            sys.exit(0)
        else:
            print(f"❌ SMOKE TEST FAILED: Status Code {response.status_code}")
            sys.exit(1)
    # Pylint'in "genel hata yakalama" uyarısını susturuyoruz
    except Exception as e: # pylint: disable=broad-exception-caught
        print(f"❌ SMOKE TEST FAILED: Connection Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    smoke_test()
