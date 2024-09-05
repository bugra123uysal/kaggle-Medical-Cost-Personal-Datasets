import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi oku
myurl = pd.read_csv("C:\\Users\\buğra\\Desktop\\insurance.csv")

# Sütun isimlerini yazdır
print(myurl.columns)

yyas=myurl['sex'].value_counts()
smo= myurl['smoker']
ag=myurl['age']
ch=myurl['children']
""" sex (male, female) """
plt.bar(yyas.index , yyas , color=["blue", "pink"])
plt.title("sex ")
plt.grid(True , alpha=0.4)
plt.show()


""" child """
sns.countplot(x='children' , data=myurl   )
plt.title("dene")
plt.show()
""" age """
sns.countplot(x='age' , hue='sex' ,data=myurl)
plt.show()

""" smoke region """
sns.countplot(x='region'  ,hue='smoker' , data=myurl )
plt.title("smoke")
plt.show()


