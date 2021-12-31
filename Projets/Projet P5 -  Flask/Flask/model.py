
#importation 
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
import pickle
digits = load_digits()

#Entrainements du modèle 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target,random_state=0)
rf = RandomForestClassifier(n_estimators=1000)
rf.fit(X_train, y_train)


#Evaluation du modele d'entrainement 
from sklearn.metrics import classification_report
y_pred = rf.predict(X_test)
print(classification_report(y_pred, y_test))


# Sauvegarder le modele
pickle.dump(rf, open('digits_trainning.sav', 'wb')) # permet de sauvegarder le modèle dans python
