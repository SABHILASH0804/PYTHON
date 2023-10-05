import pandas as p
#import matplotlib.pyplot as pd
df=p.read_csv("E:\\class 12\\PROJECT\\batsman teams.csv")
print("Top 10 Batsman : ",end="\n\n")
print(df,end="\n\n")

dtf=p.read_csv("E:\\class 12\\PROJECT\\batsman scores.csv")

dfm=p.read_csv("E:\\class 12\\PROJECT\\Bowlers team.csv")
print("Top 10 Bowlers : ",end="\n\n")
print(dfm,end="\n\n")

dtfm=p.read_csv("E:\\class 12\\PROJECT\\bowlers scores.csv")

print("""(A) For batsman status or query
(B) For bowler status or query""",end="\n\n\n")
y=input("Enter your choice from above : ")
if y=="a" or y=="A" :
    print("""(1) Displays the top three batsman in all time rankings
(2) Displays three batsman with most hundreds
(3) Diplays batsman with maximum highest score in the list
(6) For displaying details of all
players from a particular team
(7) For displaying the graphical representation """,end="\n\n\n")


else :
    print("""(4) Bowler with most 10-wicket haul
(5) For displaying details of all
players from a particular team
(8) Displays the details of the best or the least best bowler in the top 10

according to your requirement(bowler)
(9) For displaying the graphical representation """,end="\n\n\n")

x=int(input("select and enter a number to perfom the query :"))
print(end="\n")
if x==1:
    y=dtf.head(3)
    a=y.loc[:,"Player name"].values
    print("Top three batsman are :")
    for z in a:
        print(z)
if x==2:
    print("Three batsman with most hundreds are :")
    y=dtf.loc[:,"Hundreds"]
    z=y.sort_values(ascending=False).head(3).index
    for w in z:
        print(dtf.iat[w,1])

if x==3:
    print("The batsman with maximum highest score is :")
    y=dtf.loc[:,"highest score"]
    m=y.sort_values(ascending=False).head(1).index
    for z in m:
        print(dtf.iat[z,1])
        
if x==4:
    m=dtfm.loc[:,"10-wicket"]
    y=m.sort_values(ascending=False).head(1).index
    for w in y:
        print(dtfm.loc[w,"Player name"])
   
if x==5:
    m=input("""Enter the team of your choice from the list
with first letter as capital  :""")
    if m in dfm["Country(Team)"].values :
        v=dfm[dfm["Country(Team)"]==m].index
        print(v)
        for t in v :
            print(dtfm.iloc[t,1:],end="\n\n")
    if dfm[dfm["Country(Team)"]==m].empty==True :
        print("no player from the team exist fromt he top 10!!!!!!")

if x==6:
    m=input("""Enter the team of your choice from the list
with first letter as capital  :""")
    if df[df["Country(team)"]==m].empty==False :
        v=df[df["Country(team)"]==m].index
        for t in v :
            print(dtf.iloc[t,1:],end="\n\n")
    if df[df["Country(team)"]==m].empty==True :
        print("no player from the team exist fromt he top 10!!!")

if x==7:
    dtf.plot(x="Player name",y="highest score",kind="bar")
    pd.xlabel("Player Name")
    pd.ylabel("Highest score")
    pd.show()
if x==8:
    m=str(input("Enter BEST or LEAST BEST according to your wish : "))
    if m=="BEST" or m=="best" or m=="Best":
        y=dtfm.iloc[0,:]
        print(y)
        print(end="\n")
    else :
        y=dtfm.iloc[9,:]
        print(y)
        print(end="\n")
if x==9:
    dtfm.plot(x="Player name",y="Wickets",kind="bar")
    pd.xlabel("Player Name")
    pd.ylabel("Wickets")
    pd.show()
    
    
        

        
    




        
        

