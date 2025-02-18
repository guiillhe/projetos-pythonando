import google as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("How does AI work?")
print(response.text)