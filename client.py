import keys

import google.generativeai as genai

# Directly configure the API key for this project

# Configure the API key for the Generative AI model
genai.configure(api_key=keys.api_key_gemini)

# Initialize the model with the API key specifically for this instance
model = genai.GenerativeModel('gemini-1.5-flash')

system_role = "You are a female virtual assistant named Sidney skilled in general tasks like Alexa and Google Cloud."
user_role = "What is engineering?"
response = model.generate_content(f"{system_role}. {user_role} ")
print(response.text)


# response = model.generate_content("what is Engineering?")
# print(response.text)

# got api key from google Ai studio




