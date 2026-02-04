from ml.inference import predict

def chat_response(user_input: str) -> str:
    response = predict(user_input)
    return response
