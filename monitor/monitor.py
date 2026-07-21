import requests
import time
import logging

# Configuración de logs
logging.basicConfig(
    filename='logs/production.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

BASE_REST_URL = "http://localhost:4000/api/v1"
GRAPHQL_URL = "http://localhost:4000/graphql"

def check_rest_endpoint():
    try:
        response = requests.get(f"{BASE_REST_URL}/users", timeout=2)
        if response.status_code == 200:
            logging.info(f"REST /users OK | Status: {response.status_code}")
        else:
            logging.error(f"REST /users FAILED | Status: {response.status_code} | Payload: {response.text}")
    except Exception as e:
        logging.critical(f"REST /users UNREACHABLE | Error: {str(e)}")

def check_graphql_endpoint():
    query = """
    query {
      checkService(name: "PaymentGateway") {
        service
        healthy
        latencyMs
      }
    }
    """
    try:
        response = requests.post(GRAPHQL_URL, json={'query': query}, timeout=2)
        data = response.json()
        if "errors" in data:
            logging.error(f"GraphQL Query Error | {data['errors']}")
        else:
            latency = data['data']['checkService']['latencyMs']
            logging.info(f"GraphQL PaymentGateway OK | Latency: {latency}ms")
    except Exception as e:
        logging.critical(f"GraphQL Service UNREACHABLE | Error: {str(e)}")

if __name__ == "__main__":
    print("Starting API Diagnostics Monitor...")
    for _ in range(5):  # Ejecuta 5 ciclos de prueba
        check_rest_endpoint()
        check_graphql_endpoint()
        time.sleep(2)