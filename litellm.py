import litellm

class LiteLLMModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def predict(self, input_text):
        """
        Make a prediction using the LiteLLM model.

        Args:
            input_text (str): The input text for the prediction.

        Returns:
            str: The predicted output.
        """
        try:
            response = litellm.completion(
                model=self.model_name,
                messages=[{"role": "user", "content": input_text}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == "__main__":
    model = LiteLLMModel(model_name="gpt-3.5-turbo")
    prediction = model.predict("Hello!")
    print(prediction) 