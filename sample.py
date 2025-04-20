git init
git config --global user.name "vedantikavitkar"
git config --global user.email "vedantikavitkar24@gmail.com"
git remote add origin https://github.com/vedantikavitkar/sample 
git remote -v
git remote set-url origin https://github.com/vedantikavitkar/sample 
git add .
git commit -m "veda"
  git push -u origin main

import joblib

# Assume model is your trained model (e.g., from scikit-learn)
joblib.dump(model, 'mlopsexam.joblib')

loaded_model = joblib.load('mlopsexam.joblib')


loaded_model
