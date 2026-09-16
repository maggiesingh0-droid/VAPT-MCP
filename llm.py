import os
from google import genai
from google.genai import types

os.environ["GEMINI_API_KEY"] = os.environ.get("GEMINI_API_KEY")

def analyze_vulnerability(target_url):
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ एरर: GEMINI_API_KEY सेट नहीं है! कृपया GitHub Secrets चेक करें।")
        return
        
    client = genai.Client()
    system_instruction = (
        "You are an elite Cybersecurity Expert with an extensive knowledge graph of "
        "web application security. Provide a structured, legal, and ethical methodology "
        "to test the given target URL."
    )
    user_prompt = f"Develop a preliminary vulnerability testing plan for the target URL: {target_url}"
    
    try:
        # हमने यहाँ बिल्कुल सटीक 2.0-flash मॉडल सेट किया है
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3,
            ),
        )
        print("🛡️ --- CYBERSECURITY ASSESSMENT PLAN --- 🛡️\n")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_vulnerability("http://testfire.net")
