from Player import Player, Champ
from Result import Result


class Match:

    def __init__(self, player_list: list = None):

        if player_list == None:
            self.player_list = []
        else:
            self.player_list = player_list
        self.team1 = None
        self.team2 = None

    def __str__(self):
        cmd = ""
        for player, champ, score in self.player_list:
            cmd += f"{player.name}: {champ}- {score}\n"
        cmd += "\n\n"
        cmd += f"team1:{self.team1}\n team2:{self.team2}"
        return cmd

    def add_player(self, player: Player, champ: Champ, score: int, *args, **kwargs) -> Result:
        self.player_list.append((player, champ, score))
        return Result(error=Result.ErrorCode.ok)

    def remove_player(self, player: Player, *args, **kwargs) -> Result:
        self.player_list.remove(player)
        return Result(error=Result.ErrorCode.ok)

    def create_match(self, *args, **kwargs) -> Result:

        team1 = []
        team2 = []
        team1_score = 0
        team2_score = 0
        score_list = []
        for player, champ, score in self.player_list:
            score_list.append((player.name, score, champ))

        score_list = sorted(score_list, key=lambda x: x[1], reverse=True)
        for i, player in enumerate(score_list):
            if team1_score < team2_score:
                team1.append(player)
                team1_score += player[1]
            else:
                team2.append(player)
                team2_score += player[1]

        print(f"team1: {team1_score}, team2: {team2_score}")
        self.team1 = team1
        self.team2 = team2

        return Result(error=Result.ErrorCode.ok)


if __name__ == '__main__':
    import random
    import json
    import copy

    f = open('champs.json')
    # Read the JSON data
    json_data = f.read()
    f.close()
    champ_dict = json.loads(json_data)
    champ_dict_to_save = copy.copy(champ_dict)
    match = Match()
    players = ["yosef", "PT", "matanel", "ohad", "yonatan", "shalom"]

    for player in players:
        champ = random.choice(list(champ_dict.keys()))
        del champ_dict[champ]
        account_id = random.randint(0, 2000)
        player = Player(account_id=str(account_id), name=player, champ_dict=champ_dict_to_save)
        match.add_player(player=player, champ=champ, score=player.champ_dict[champ])

    result_obj = match.create_match()
    print(match)
