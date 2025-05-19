import google.generativeai as genai

genai.configure(api_key="Enter your gemini api key here")

def get_summary_from_text(transcript):
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    prompt = f"Summarize the following meeting transcript. Extract key points and action items:\n\n{transcript}"
    response = model.generate_content(prompt)
    return response.text
