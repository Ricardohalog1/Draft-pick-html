from inference_sdk import InferenceHTTPClient

# Initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="API_KEY"
)

# Send inference request to the model
result = CLIENT.infer("Assets/HeroPick/aamon.png", model_id="mobile-legends-draft-recognition/3")
