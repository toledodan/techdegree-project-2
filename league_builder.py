import csv
import os

if __name__ == "__main__":

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    # Main function for building the roster
    def build_files():
        unsorted_file = open_csv(signup_list)
        sorted_file = sort_players(unsorted_file)
        teams = assign_players(sorted_file)
        write_teams(teams)


    # Open source file
    def open_csv(filename):
        player_list = []
        with open(filename, newline='') as source_csv:
            player_reader = csv.reader(source_csv)
            player_list = list(player_reader)
            return player_list


    # Sort players by experience
    def sort_players(playerlist):
        sorted_players = []
        for row in playerlist:
            if row[2].upper() == 'NO':
                sorted_players.insert(0, row)
            elif row[2].upper() == 'YES':
                sorted_players.insert(-1, row)
        return sorted_players


    # Assign sorted players to teams
    def assign_players(rawfile):
        sharks = []
        dragons = []
        raptors = []
        team = 1
        for row in rawfile:
            if team == 1:
                sharks.append(row)
                team += 1
            elif team == 2:
                dragons.append(row)
                team += 1
            elif team == 3:
                raptors.append(row)
                team = 1
        return sharks, dragons, raptors


    # Create teams roster file
    def write_teams(teamlist):
        with open('teams.txt', 'a') as newfile:
            # Write player details into file
            def write_players(team):
                for player in team:
                    # Don't include height
                    player.pop(1)
                    # Create welcome letter for parents
                    player_letter(player, teamname)
                    newfile.write(", ".join(player))
                    newfile.write("\n")
            # Add assigned players to teams.txt roster
            teamname = 'sharks'
            for team in teamlist:
                if teamname == 'sharks':
                    newfile.write("Sharks\n")
                    write_players(team)
                    teamname = 'dragons'
                elif teamname == 'dragons':
                    newfile.write("\nDragons\n")
                    write_players(team)
                    teamname = 'raptors'
                elif teamname == 'raptors':
                    newfile.write("\nRaptors\n")
                    write_players(team)
                    newfile.close()

    # Create a personalized letter for each players' parents
    def player_letter(playerinfo, teamname):
        with open('{}.txt'.format(playerinfo[0].replace(' ', '_').lower()), 'a') as playerletter:
            playerletter.write("Dear {},\n\nYour child {} has been assigned to team {} which will begin practice on May 1 at 7PM.\n\nSincerely,\n\nThe Coaching Staff\n\n".format(playerinfo[2],playerinfo[0],teamname.title()))


    while True:
        try:
            clear_screen()
            print('Welcome to the League Builder!')
            signup_list = input('\nPlease type the name of your signup list\nsource file, or "QUIT" to exit.\n\n** Please note **\nSource file must be in a .csv format\n\n>  ')
            if signup_list.upper() == 'QUIT':
                print('\nGoodbye!\n')
                break
            elif signup_list[-4:].lower() != '.csv':
                input("\nI'm sorry, '{}' is not in the correct format. Please try again.\n(Press ENTER to continue)".format(signup_list))
            else:
                build_files()
                successful_build = input('\n** Build complete **\n\nWould you like to create another roster? [Y/n]')
                if successful_build.upper() == 'N':
                    print('\nGoodbye!\n')
                    break
                else:
                    continue
        except FileNotFoundError:
            input("\nI'm sorry, '{}' does not exist. Please try again.\n(Press ENTER to continue)".format(signup_list))
