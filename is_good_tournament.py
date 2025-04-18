'''
I appeared for a google mock interview. this was the question asked:

You are given a list of players rank 1 to N denoting their rank 1 being the top rank player and N being the worst ranked player. We are given a list.. say 1 2 3 4 5 6 7 8 (these are ranks of these 8 players). The rule is that whenever 2 players play. the one with the highest rank will always win. so the tournament will go like this. 1 plays 2 -> 1 wins 3 plays 4 -> 3 wins, 5 plays 6 -> 5 wins, 7 plays 8, 7 wins. now this will continue 1 will play 3 -> 1 wins, 5 plays 7 -> 5 wins. the 3rd round 1 plays 5 -> 1 wins and he is the winner. this is how the players will play.

1 2 3 4 5 6 7 8
1 3 5 7
1 5
1

We need to determine if a tournament is a good tournament or not? A good tournament is defined as a tournament in which in every round the best rank player from top plays the worst rank player from bottom.

the above tournament is not a good tournament. let me give u an example of good tournament.

8 1 4 5 2 7 3 6
1 4 2 3
1 2
1

in the 1st round 1 plays 8 (1 wins) 4 plays 5(4 wins) 2 plays 7 (2 wins) and 3 plays 6(3 wins). in the second round too the order is maintained 1 plays 4 (1 wins) 2 plays 3(2 wins) and in the 3rd round too 1 plays 2 and finally wins. this is an example of a good tournament.

we need to write a function which will take these ranks in the form of list. and return if a tournament is good or not.

## (0th player will play 1st .. 2nd will play 3rd and so on..... this is fixed rule)
'''


def is_good_tournament(players):

    while len(players) > 1:
        if len(players) % 2 != 0:
            return False  # 必須是偶數才能配對

        next_round = []
        n = len(players)
        best_player = min(players)
        worst_player = max(players)

        for i in range(0, n, 2):
            p1, p2 = players[i], players[i + 1]
            best, worst = min(p1, p2), max(p1, p2)
            winner = best

            if abs(best_player - best) != abs(worst_player - worst):
                return False

            next_round.append(winner)

        players = next_round

    return True


print(is_good_tournament([8, 1, 4, 5, 2, 7, 3, 6]))
