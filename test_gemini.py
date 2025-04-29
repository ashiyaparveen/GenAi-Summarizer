import google.generativeai as genai


genai.configure(api_key="AIzaSyC6rX9MFqreAGFuh5eyWbixJmAdZs29Kkk")  

models = genai.list_models()
for m in models:
    print(m.name)