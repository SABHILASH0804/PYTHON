import pandas as pd
import matplotlib.pyplot as plt
import easygui
import art

df = pd.read_csv("E:\\class 12\\PROJECT\\batsman teams.csv")
dtf = pd.read_csv("E:\\class 12\\PROJECT\\batsman scores.csv")
dfm = pd.read_csv("E:\\class 12\\PROJECT\\Bowlers team.csv")
dtfm = pd.read_csv("E:\\class 12\\PROJECT\\bowlers scores.csv")

def display_ascii_art(text, font='block', size=12):
    """
    Display ASCII art using the art library.
    """
    ascii_art = art.text2art(text, font=font, chr_ignore=True)
    easygui.codebox("ASCII Art", "ASCII Art Output", ascii_art)

def display_graphical_representation(data, x_col, y_col, kind='bar'):
    """
    Display graphical representation using matplotlib.
    """
    plt.figure(figsize=(10, 6))
    data.plot(x=x_col, y=y_col, kind=kind)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    plt.show()

def display_popup_message(title, message):
    """
    Display a popup message using easygui.
    """
    easygui.msgbox(message, title)

while True:
    display_ascii_art("Top 10 Batsman")
    print(df)
    display_ascii_art("Top 10 Bowlers")
    print(dfm)

    display_popup_message("Options", "(A) For batsman status or query\n(B) For bowler status or query")

    user_choice = input("Enter your choice from above (type 'exit' to exit): ").lower()

    if user_choice == 'exit':
        break

    if user_choice == 'a':
        display_popup_message("Batsman Query Options", "(1) Displays the top three batsmen in all-time rankings\n"
                                                        "(2) Displays three batsmen with the most hundreds\n"
                                                        "(3) Displays batsman with the maximum highest score in the list\n"
                                                        "(6) For displaying details of all players from a particular team\n"
                                                        "(7) For displaying the graphical representation")
    else:
        display_popup_message("Bowler Query Options", "(4) Bowler with the most 10-wicket haul\n"
                                                      "(5) For displaying details of all players from a particular team\n"
                                                      "(8) Displays the details of the best or the least best bowler in the top 10\n"
                                                      "(9) For displaying the graphical representation")

    user_query = int(input("Select and enter a number to perform the query: "))

    if user_query == 1:
        top_batsmen = dtf.head(3)
        top_batsmen_names = top_batsmen.loc[:, "Player name"].values
        display_popup_message("Top Three Batsmen", f"Top three batsmen are: {', '.join(top_batsmen_names)}")
    elif user_query == 2:
        top_hundreds = dtf.sort_values(by="Hundreds", ascending=False).head(3)
        top_hundreds_names = top_hundreds.loc[:, "Player name"].values
        display_popup_message("Top Three Batsmen with Most Hundreds", f"Top three batsmen with most hundreds are: {', '.join(top_hundreds_names)}")
    elif user_query == 3:
        max_highest_score = dtf.loc[dtf["highest score"].idxmax(), "Player name"]
        display_popup_message("Batsman with Maximum Highest Score", f"The batsman with the maximum highest score is: {max_highest_score}")
    elif user_query == 5:
        m = input("Enter the team of your choice from the list with the first letter as capital: ")
        if m in dfm["Country(Team)"].values:
            v = dfm[dfm["Country(Team)"] == m].index
            players_exist = False
            for t in v:
                display_popup_message(f"Details of Players from Team {m}", f"{dtfm.iloc[t, 1:].to_string(index=False)}")
                players_exist = True
            if not players_exist:
                display_popup_message("No Players Found", f"No player from the team {m} exists in the top 10.")
        else:
            display_popup_message("Invalid Team", "The entered team is not in the list.")
    elif user_query == 6:
        m = input("Enter the team of your choice from the list with the first letter as capital: ")
        if not df[df["Country(team)"] == m].empty:
            v = df[df["Country(team)"] == m].index
            for t in v:
                player_details = dtf.iloc[t, 1:].to_string()
                display_popup_message(f"Details for {dtf.iloc[t, 0]}", player_details)
        else:
            display_popup_message("No player from the team exists from the top 10!!!")
    elif user_query == 7:
        display_graphical_representation(dtf, x_col="Player name", y_col="highest score", kind="bar")
    elif user_query == 8:
        best_or_least = input("Enter BEST or LEAST BEST according to your wish: ").upper()
        if best_or_least == "BEST":
            best_bowler_details = dtfm.iloc[0, :].to_string()
            display_popup_message("Details of the Best Bowler", f"Details of the best bowler:\n{best_bowler_details}")
        elif best_or_least == "LEAST BEST":
            least_best_bowler_details = dtfm.iloc[9, :].to_string()
            display_popup_message("Details of the Least Best Bowler", f"Details of the least best bowler:\n{least_best_bowler_details}")
    elif user_query == 9:
        display_graphical_representation(dtfm, x_col="Player name", y_col="Wickets", kind="bar")
    
    
        

        
    




        
        

