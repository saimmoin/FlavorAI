# FlavorAI 🍳

**An intelligent recipe generator powered by Google Generative AI**

FlavorAI is a Flask-based web application that transforms your available ingredients into creative, step-by-step recipes. Simply input what you have in your kitchen, and let AI craft personalized recipes with detailed cooking instructions, preparation times, and serving suggestions.

---

## ✨ Features

- **Smart Recipe Generation**: Create recipes using only your available ingredients
- **Detailed Instructions**: Get step-by-step cooking directions with prep and cooking times
- **RESTful API**: Simple `/create_recipe` endpoint for easy integration
- **Cross-Origin Support**: CORS enabled for seamless frontend integration
- **AI-Powered**: Leverages Google Gemini for intelligent recipe creation

---

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Google Generative AI API key

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/saimmoin/FlavorAI.git
   cd FlavorAI
   ```

2. **Create Virtual Environment** *(Recommended)*
   
   **Linux/macOS:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
   **Windows (PowerShell):**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

### Environment Variables

Set up your Google Generative AI API key:

**Linux/macOS:**
```bash
export GENAI_API_KEY="your_api_key_here"
```

**Windows (PowerShell):**
```powershell
$env:GENAI_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GENAI_API_KEY=your_api_key_here
```

> **Note**: To make the environment variable persistent on Windows, use:
> ```powershell
> setx GENAI_API_KEY "your_api_key_here"
> ```

---

## 🚀 Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at:
```
http://127.0.0.1:5000/
```

---

## 🔧 Dependencies

- **Flask**: Web framework for Python
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **google-generativeai**: Google Gemini API client
- **python-dotenv**: Environment variable management *(optional)*

---

## 🆘 Support

If you encounter any issues or have questions:

- **Issues**: [GitHub Issues](https://github.com/saimmoin/FlavorAI/issues)
---
