import google.generativeai as genai

# Replace with your actual API key from Google AI Studio or MakerSuite
genai.configure(api_key="AIzaSyBgQh5AKTSiBxf588QVmPjTPhJCWA7LwKY")

models = genai.list_models()
for model in models:
    print(model.name)
