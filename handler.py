import runpod
from wgp import main_function  # <- Passe ggf. an, je nachdem wie du starten willst

def handler(job):
    input_data = job["input"]
    result = main_function(input_data)
    return result

runpod.serverless.start({"handler": handler})
