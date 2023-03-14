from Result import Result
from enum import Enum
import sys

sys.path.append('..')  # changing to root directory
import server.MongoDB_connection as server


class Champ(Enum):
    AATROX = "Aatrox"
    AHRI = "Ahri"
    AKALI = "Akali"
    ALISTAR = "Alistar"
    AMUMU = "Amumu"
    ANIVIA = "Anivia"
    ANNIE = "Annie"
    APHELIOS = "Aphelios"
    ASHE = "Ashe"
    AURELION_SOL = "Aurelion Sol"
    AZIR = "Azir"
    BARD = "Bard"
    BLITZCRANK = "Blitzcrank"
    BRAND = "Brand"
    BRAUM = "Braum"
    CAITLYN = "Caitlyn"
    CAMILLE = "Camille"
    CASSIOPEIA = "Cassiopeia"
    CHO_GATH = "ChoGath"
    CORKI = "Corki"
    DARIUS = "Darius"
    DIANA = "Diana"
    DR_MUNDO = "Dr. Mundo"
    DRAVEN = "Draven"
    EKKO = "Ekko"
    ELISE = "Elise"
    EVELYNN = "Evelynn"
    EZREAL = "Ezreal"
    FIDDLESTICKS = "Fiddlesticks"
    FIORA = "Fiora"
    FIZZ = "Fizz"
    GALIO = "Galio"
    GANGPLANK = "Gangplank"
    GAREN = "Garen"
    GNAR = "Gnar"
    GRAGAS = "Gragas"
    GRAVES = "Graves"
    HECARIM = "Hecarim"
    HEIMERDINGER = "Heimerdinger"
    ILLAOI = "Illaoi"
    IRELIA = "Irelia"
    IVERN = "Ivern"
    JANNA = "Janna"
    JARVAN_IV = "Jarvan IV"
    JAX = "Jax"
    JAYCE = "Jayce"
    JHIN = "Jhin"
    JINX = "Jinx"
    KAISA = "KaiSa"
    KALISTA = "Kalista"
    KARMA = "Karma"
    KARTHUS = "Karthus"
    KASSADIN = "Kassadin"
    KATARINA = "Katarina"
    KAYLE = "Kayle"
    KAYN = "Kayn"
    KENNEN = "Kennen"
    KHA_ZIX = "KhaZix"
    KINDRED = "Kindred"
    KLED = "Kled"
    KOG_MAW = "KogMaw"
    LEBLANC = "LeBlanc"
    LEE_SIN = "Lee Sin"
    LEONA = "Leona"
    LILLIA = "Lillia"
    LISSANDRA = "Lissandra"
    LUCIAN = "Lucian"
    LULU = "Lulu"
    LUX = "Lux"
    MALPHITE = "Malphite"
    MALZAHAR = "Malz"
    MAOKAI = "Maokai"
    MASTER_YI = "Master_yi"
    MISS_FORTUNE = "Miss_fortune"
    MORDEKAISER = "Mordekaiser"
    MORGANA = "Morgana"
    NAMI = "Nami"
    NASUS = "Nasus"
    NAUTILUS = "Nautilus"
    NEEKO = "Neeko"
    NIDALEE = "Nidalee"
    NOCTURNE = "Nocturne"
    NUNU_AND_WILLUMP = "NUNU_AND_WILLUMP"
    OLAF = "Olaf"
    ORIANNA = "Oriana"
    ORNN = "Ornn"
    PANTHEON = "Pantheon"
    POPPY = "Poppy"
    PYKE = "Pyke"
    QIYANA = "Qiyana"
    QUINN = "Quinn"


class Player:

    def __init__(self, name:str, *args, **kwargs) -> None:
        try:
            player_enum = server.Players[name.capitalize()]
            self.name = player_enum.name
            self.player = player_enum
            result_obj = self.update_champ_dict()
            if result_obj.error != Result.ErrorCode.ok:
                print("could not update %s dict" % player_enum.name)
                quit()
            self.champ_dict = result_obj.value
        except KeyError:
            print("%s is not a valid player name" % name)
            quit()

    def __str__(self):
        return "name: {self.name} ".format(self=self)

    def update_champ_dict(self, *args, **kwargs) -> Result:
        connection = server.MongoDBConnection()
        result_obj = connection.get_dictionary_champ(player_name=self.player)
        if result_obj.error != Result.ErrorCode.ok:
            msg = "could not connect the DB and get the player champion_dict"
            print(msg)
            return Result(error=Result.ErrorCode.error, error_msg=msg)

        return Result(error=Result.ErrorCode.ok, value=result_obj.value)

    def get_champ_score(self, champ: Champ, *args, **kwargs) -> Result:
        champ_name = champ.value
        score = self.champ_dict[champ_name]
        return Result(error=Result.ErrorCode.ok, value=score)


if __name__ == '__main__':
    player_enum = server.Players.Gelkop
    player = Player(player=player_enum)
    result_obj = player.update_champ_dict()
    if result_obj.error != Result.ErrorCode.ok:
        print("could not update champ dict %s" % player.name)
    print(player.champ_dict)
    champ = Champ.AHRI
    result_obj = player.get_champ_score(champ)
    if result_obj.error != Result.ErrorCode.ok:
        print("could not update champ dict %s" % player.name)
    print("%s with %s = %s" % (player, champ.name, result_obj.value))
