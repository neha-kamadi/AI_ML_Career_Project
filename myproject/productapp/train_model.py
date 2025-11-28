import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib


#sample datasets
data = { 
        
        'skills': [
        'python machine learning data analysis',
        'creative photoshop design ui ux',
        'communication leadership management',
        'html css javascript web development',
        'statistics python data visualization',
        'writing editing storytelling content creation'
    ],
    'career': [
        'Data Scientist',
        'UI/UX Designer',
        'Manager',
        'Web Developer',
        'Data Analyst',
        'Content Writer'
    ]
    
    }
df = pd.DataFrame(data)

x = df['skills']
y = df['career']

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(x,y)

joblib.dump(model, 'career_model.pkl')
print("Model trained and save successfully")