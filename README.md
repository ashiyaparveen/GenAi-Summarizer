# 🧠 GenAI Summarizer - Project Documentation

## 🧰 Technologies Used

### Frontend:
- **Framework**: React.js (with Vite)
- **Language**: JavaScript
- **Styling**: CSS
- **Dependencies**: Axios (for HTTP requests)

### Backend:
- **Framework**: Flask (Python)
- **Language**: Python 3.9+
- **Database**: MongoDB
- **Libraries**:
  - Flask
  - Flask-CORS
  - requests
  - pymongo
  - google.generativeai (Gemini Pro LLM)

## 🌐 Project Structure

### Frontend Directory (`frontend/`)
```
frontend/
├── public/
├── src/
│   ├── components/
│   │   └── History.jsx
│   ├── App.jsx
│   ├── App.css
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```

### Backend Directory (`backend/`)
```
backend/
├── app.py
├── .env
└── requirements.txt
```

## ⚙️ Frontend Setup (React with Vite)

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Run the Frontend
```bash
npm run dev
```

### 3. File Highlights
- **App.jsx**: Handles form inputs, API communication, and displays results.
- **History.jsx**: Displays user-specific summary history.
- **App.css**: Provides polished UI similar to musely.ai.

## ⚙️ Backend Setup (Flask)

### 1. Create Python Environment and Install Dependencies
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Create `.env` File
Add the following to your `.env`:
```
MONGODB_URI=your_mongodb_uri
GEMINI_API_KEY=your_gemini_api_key
```

### 3. Run the Backend
```bash
flask run
```

### 4. File Highlights
- **app.py**: Flask app with `/summarize` and `/history/<user_id>` endpoints.
- **MongoDB**: Stores user summaries with timestamp.

## 🔄 Frontend-Backend Integration
- The frontend sends a POST request to `http://localhost:5000/summarize` with `{ user_id, url }`.
- The backend fetches and summarizes the content using Gemini API and stores it in MongoDB.
- Summary history is fetched via GET request to `http://localhost:5000/history/<user_id>`.

## 🧪 How to Test and Use

1. **Start Backend**
   - Run Flask backend (see instructions above).

2. **Start Frontend**
   - Run Vite frontend (see instructions above).

3. **Use the App**
   - Enter a `user ID`.
   - Paste a valid article `URL`.
   - Click `Summarize`.
   - View the summarized result and browse the `Summary History` section.

4. **Test Scenarios**
   - ✅ Valid article URL → Summary generated
   - ❌ Invalid/Empty URL → Error message shown
   - 💾 History stores and retrieves previous summaries

## ✅ Final Tips
- Ensure CORS is enabled in Flask (`Flask-CORS` is used).
- Ensure `.env` variables are loaded before running the server.
- Gemini summarizer uses Google’s `generativeai` library; valid API key required.
- You can deploy this with services like Vercel (frontend), Render (backend), and MongoDB Atlas.

---
Built with ❤️ by Ashiya Parveen R

