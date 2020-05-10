#1st task
import pandas as pd

Person = {"Name": ["Anahit", "Artur", "Hayk", "Jora", "Liana", "Nairi", "Ruzanna", "Salbina", "Sona", "Tatev", "Tigran", "Vlad"],
		"Surname" : ["Kirakosyan", "Mkrtchyan", "Sahakyan", "Karyan", "Varosyan", "Hakobyan", "Ordyan", "Alaverdyan", "Kirakosyan", "Alaverdyan", "Movsisyan", "Harutyunyan"],
		"Sex" : ["F", "M", "M", "M", "M", "F", "M" , "F", "F", "F", "F", "M"],
		"Status" : ["Student", "Student", "Student", "Student", "Student", "Tutor", "Student", "Student", "Student", "Student", "Student", "Student"]
				}
df = pd.DataFrame(Person, columns = ["Name", "Surname", "Sex", "Status"])
print(df)

#2nd task
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print(df[(df["release_year"]  > 2015)])
