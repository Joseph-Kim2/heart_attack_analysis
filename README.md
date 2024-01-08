# Heart Attack Analysis
Using a practice dataset with fake patient medical data, I aimed to perform data analysis that would give us a better look at the meaning of the data. 
These are the factors related to heart attacks that are considered in this data:
1. Heart Attack Percentage is calculated based on all data to see if the data is skewed.
2. Gender Percent is used to distinguish between the heart attack rates in men and women.
3. EKG is considered, as it detects heart problems that can forecast chance of future heart attacks.
4. Exercise is considered to see if likelihood of heart attack increases when physically active.


```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")

def getHeart():
    df = pd.read_csv("heart.csv")
    df_no_attack = df[df.attack==0]
    df_attack = df[df.attack==1]
    
    heart = len(df)
    heart_attack = len(df_attack)
    no_heart_attack = len(df_no_attack)
    
    print("The percent of no heart attacks in the data: %.2f%%" % (no_heart_attack/heart*100))
    print("The percent of heart attacks in the data: %.2f%%" % (heart_attack/heart*100))
    
    
    labels = 'Heart Attack', 'No Heart Attack'
    sizes = [heart_attack, no_heart_attack]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,autopct="%1.2f%%",startangle=90)
    ax1.set_title('Heart Attack Ratio in Data')
    # fig1 = plt.gcf()
    plt.show()
    
    plt.savefig("HeartAttack.png")
    
def getGender():
    """ Finds percent male vs female of patients with heart attack history.
    
    """
    df_m = df.loc[(df.sex == 0) & (df.attack == 1)]
    df_f = df.loc[(df.sex == 1) & (df.attack == 1)]
    m_heart_attacks = len(df_m)
    f_heart_attacks = len(df_f)
    t_heart_attacks = m_heart_attacks + f_heart_attacks
    percent_notation = "{:,.2f}%".format(m_heart_attacks/t_heart_attacks*100)
    print("\nMale heart attacks:  " + percent_notation)
    percent_notation = "{:,.2f}%".format(f_heart_attacks/t_heart_attacks*100)
    print("Female heart attacks:  " + percent_notation)
    
    # create pie chart
    labels = 'Male', 'Female'
    sizes = [m_heart_attacks, f_heart_attacks]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    ax1.set_title('Heart Attack Ratio between Male & Female')
    # fig1 = plt.gcf()
    # fig1 = plt.gcf()
    plt.show()
    fig1.savefig('Gender.png')

    
    
def getEKG():
    """ Looks at resting EKG.
    
    Finds percent of patients with heart attack in each EKG Type.
    """
    restecg_val_counts = df.groupby("restecg")["attack"].value_counts()
    e = []
    print("\nEKG type:\n\t0 - EKG was normal\n\t1 - EKG had an abnormality with ST-T Wave\n\t2 - EKG had an abnormality in the Left ventricular")
    for i in range(3):
        temp = (restecg_val_counts[i][1] / (restecg_val_counts[i][1]+restecg_val_counts[i][0]))
        e.append(temp*100)
        percent_notation = "{:,.2f}%".format(temp*100)
        print("Resting EKG Type %s" % (i) + " had this percent of heart attack: " + percent_notation)
        
    # create bar chart of pain types
    data = {'Normal':e[0], 'Abnormal ST-T Wave':e[1], 'Abnormal Left Ventricular':e[2]}
    courses = list(data.keys())
    values = list(data.values())      
    fig1 = plt.figure(figsize = (10, 5))
    plt.bar(courses, values, color ='brown', width = 0.6)    
    plt.xlabel("EKG Type")
    plt.ylabel("Percent")
    plt.title("Percent Heart Attack by Resting EKG")
    # fig1 = plt.gcf()
    plt.show()
    fig1.savefig('EKG.png')
    # plt.clf()
    
    
def getExercise():
    """ Looks at Exercise history.
    
    Finds percent of patients with heart attack for no and regular exercise history.
    """
    exang_val_counts = df.groupby("exng")["attack"].value_counts()
    exang_heart_attack = (exang_val_counts[1][1] / (exang_val_counts[1][1]+exang_val_counts[1][0]))
    no_exang_heart_attack = (exang_val_counts[0][1] / (exang_val_counts[0][1]+exang_val_counts[0][0]))
    percent_notation = "{:,.2f}%".format(exang_heart_attack*100)
    print("\nPercent who Exercised and had heart attack: " + percent_notation)
    percent_notation = "{:,.2f}%".format(no_exang_heart_attack*100)
    print("Percent with No Exercise and had heart attack: " + percent_notation)
    
    # create bar chart of heart attack percents by exercise
    data = {'Yes':exang_heart_attack*100, 'No':no_exang_heart_attack*100}
    courses = list(data.keys())
    values = list(data.values())      
    fig1 = plt.figure(figsize = (10, 5))
    plt.bar(courses, values, color ='purple', width = 0.7)    
    plt.xlabel("Exercise")
    plt.ylabel("Percent Heartattack")
    plt.title("Percent Heart Attack if Exercising")
    # fig1 = plt.gcf()
    plt.show()
    fig1.savefig('Exercise.png')
    # plt.clf()
```
