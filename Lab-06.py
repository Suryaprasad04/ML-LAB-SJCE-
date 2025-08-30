import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

data=sns.load_dataset('titanic')
data=data.dropna()

data['sex']=LabelEncoder().fit_transform(data['sex'])
X=data[['pclass','sex','age','fare']]
y=data['survived']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
