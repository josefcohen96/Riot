from Player import Player, Champ, server
from Result import Result


class Match:

    def __init__(self, player_list: list = None):

        self.already_pick_champs = []
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

    def add_player(self, player: Player, *args, **kwargs) -> Result:
        """Adding player to self.player_list , and generate a random champ for the player"""
        playable_champion = player.champ_dict
        random_champion = random.choice(list(playable_champion.keys()))
        score = player.champ_dict[random_champion]
        self.already_pick_champs.append(random_champion)
        self.player_list.append((player, random_champion, score))
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

    players = ["yosef", "PT", "matanel", "ohad", "yonatan", "shalom"]

    yosef = Player(player=server.Players.Yosef)
    matanel = Player(player=server.Players.Matanel)
    ohad = Player(player=server.Players.Ohad)
    gelkop = Player(player=server.Players.Gelkop)
    piti = Player(player=server.Players.Piti)
    peretz = Player(player=server.Players.Peretz)

    match_obj = Match()
    match_obj.add_player(player=yosef)
    match_obj.add_player(player=matanel)
    match_obj.add_player(player=ohad)
    match_obj.add_player(player=gelkop)
    match_obj.add_player(player=piti)
    match_obj.add_player(player=peretz)
    match_obj.create_match()
    print(match_obj)
