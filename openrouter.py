import requests

class OpenRouterClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1"

    def make_request(self, model, messages):
        """
        Make a request to the OpenRouter API.

        Args:
            model (str): The model to use for the request.
            messages (list): List of messages for the conversation.

        Returns:
            dict: The response from the API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": messages
        }

        try:
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


if __name__ == "__main__":
    client = OpenRouterClient(api_key="your_api_key_here")
    response = client.make_request(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response) 