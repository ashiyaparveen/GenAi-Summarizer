import google.generativeai as genai


genai.configure(api_key="AIzaSyBgQh5AKTSiBxf588QVmPjTPhJCWA7LwKY")  

models = genai.list_models()
for m in models:
    print(m.name)