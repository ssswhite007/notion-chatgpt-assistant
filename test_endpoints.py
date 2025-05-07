import requests
import time

def test_ingest():
    """Test the ingest endpoint"""
    print("Testing /ingest endpoint...")
    response = requests.post('http://127.0.0.1:9000/ingest')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}\n")

def test_query(query_text):
    """Test the query endpoint"""
    print(f"Testing /query endpoint with query: '{query_text}'")
    response = requests.post(
        'http://127.0.0.1:9000/query',
        json={'query': query_text}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}\n")

if __name__ == "__main__":
    # First test the ingest endpoint
    test_ingest()
    
    # Wait a moment for the ingest to complete
    print("Waiting for ingest to complete...")
    time.sleep(2)
    
    # Then test the query endpoint with a sample query
    test_query("I am John's friend. What is his tech stack? How many years of experience does he have?") 
    test_query("I am Harry's friend. Please let me know about him.")
