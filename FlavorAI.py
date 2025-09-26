from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import os

# Configure GenAI once using environment variable
def configure_genai():
    api_key = os.getenv("GENAI_API_KEY")  # Load from environment variable
    if not api_key:
        raise ValueError("❌ Missing GENAI_API_KEY environment variable")
    genai.configure(api_key=api_key)

def generate_recipe(ingredients):
    prompt = f"""
        Create a recipe using only the following ingredients: {ingredients}.
        The recipe should include clear instructions, preparation time, cooking time, and serving suggestions.
        Do not add any additional ingredients or products, only use what is provided in the list.
        Ensure the recipe is simple to follow and utilizes the ingredients creatively.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Flask app
app = Flask(__name__)
CORS(app)

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    ingredients = request.json.get('ingredients', None)
    if not ingredients:
        return jsonify({'error': 'No ingredients provided'}), 400
    
    response = generate_recipe(ingredients)
    return jsonify({'recipe': response})

if __name__ == '__main__':
    configure_genai()  # Run once at startup
    app.run(debug=True)
