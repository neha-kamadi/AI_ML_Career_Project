---

🎓 AI Career Counselor Web Application

🧠 Overview

The AI Career Counselor is an intelligent web-based application built using Django, Machine Learning, and Bootstrap.
It helps users discover their ideal career path based on their skills and interests.

The system uses a trained TF-IDF + Naive Bayes model to analyze input text and predict the most suitable career recommendation.
Users can sign up, log in, view personalized career results, and track their prediction history in a modern, responsive dashboard.


---

🚀 Key Features

🔐 User Authentication – Signup, Login, Logout with Django authentication system

🧠 Career Prediction Model – Suggests ideal career path using NLP (TF-IDF + Naive Bayes)

📜 Prediction History – Saves and displays previous predictions per user

📈 Interactive Dashboard – Simple, clean, and responsive career results display

💾 Database Integration – Stores user data and prediction results (SQLite/MySQL)

🎨 Modern UI – Built with Bootstrap 5, smooth design, and responsive layout

⚡ Lightweight – Fast, minimal, and ideal for portfolio or interview demo



---

🏗 Tech Stack

Layer	Technology

Frontend	HTML, CSS, Bootstrap
Backend	Django (Python)
Database	SQLite (default) / MySQL (optional)
Machine Learning	Scikit-learn, Joblib, Pandas
Model	TF-IDF Vectorizer + Multinomial Naive Bayes
Deployment	Render / AWS / Localhost



---

📂 Project Structure

ai_career_counselor/
│
├── ai_career_counselor/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── counselor/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── result.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── dashboard.html
│   └── static/
│       └── css/style.css
│
├── career_model.pkl
├── db.sqlite3
└── manage.py


---

🧩 Machine Learning Model

Trained using simple text data representing skills and career categories.
Example:

Skills	Career

Python, Machine Learning, Data Analysis	Data Scientist
HTML, CSS, JavaScript, React	Web Developer
Communication, Leadership, Management	Manager
Creativity, Photoshop, Design	UI/UX Designer
Writing, Editing, Content Creation	Content Writer


Model:

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X, y)
joblib.dump(model, 'career_model.pkl')


---

💻 How It Works

1. User enters skills and interests


2. Backend sends input to trained ML model (career_model.pkl)


3. Model predicts best-fit career path


4. Result and recommended skills are displayed on the web page


5. Each prediction is saved to the user’s history dashboard




---

📸 Screenshots

(Optional – you can add later)

Home Page

Career Prediction Result

Login / Signup

Dashboard with History



---

🧠 Future Enhancements

Integrate the AI Chatbot Counselor (in progress 🚀)

Add career learning paths and recommended courses

Include resume analyzer to match user profile to career roles

Deploy on Render / AWS for public access



---

📚 Installation

# Clone repo
git clone https://github.com/<your-username>/ai-career-counselor.git

cd ai-career-counselor

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
source venv/bin/activate # (Linux/Mac)

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver

Then open: 👉 http://127.0.0.1:8000/


---

🧾 Requirements.txt Example

django
pandas
scikit-learn
joblib


---

👩‍💻 Author

Neha Kamadi
🎓 MSc Computer Science Student
💡 Passionate about AI, ML, and Web Development
📫 GitHub / LinkedIn links (add yours)


---

Would you like me to also create a short GitHub description (one-line tagline + keywords) that appears on the repo header (e.g., “AI-powered career recommendation web app using Django and Machine Learning”)?
