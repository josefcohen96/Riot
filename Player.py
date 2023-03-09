from Result import Result
import json
from enum import Enum


class Champ(Enum):  # (as of September 2021)
    AATROX = "AATROX"
    AHRI = "AHRI"
    AKALI = "AKALI"
    ALISTAR = "ALISTAR"
    AMUMU = "AMUMU"
    ANIVIA = "ANIVIA"
    ANNIE = "ANNIE"
    APHELIOS = "APHELIOS"
    ASHE = "ASHE"
    AURELION_SOL = "AURELION_SOL"
    AZIR = "AZIR"
    BARD = "BARD"
    BLITZCRANK = "BLITZCRANK"
    BRAND = "BRAND"
    BRAUM = "BRAUM"
    CAITLYN = "CAITLYN"
    CAMILLE = "CAMILLE"
    CASSIOPEIA = "CASSIOPEIA"
    CHO_GATH = "CHO_GATH"
    CORKI = "CORKI"
    DARIUS = "DARIUS"
    DIANA = "DIANA"
    DR_MUNDO = "DR_MUNDO"
    DRAVEN = "DRAVEN"
    EKKO = "EKKO"
    ELISE = "ELISE"
    EVELYNN = "EVELYNN"
    EZREAL = "EZREAL"
    FIDDLESTICKS = "FIDDLESTICKS"
    FIORA = "FIORA"
    FIZZ = "FIZZ"
    GALIO = "GALIO"
    GANGPLANK = "GANGPLANK"
    GAREN = "GAREN"
    GNAR = "GNAR"
    GRAGAS = "GRAGAS"
    GRAVES = "GRAVES"
    HECARIM = "HECARIM"
    HEIMERDINGER = "HEIMERDINGER"
    ILLAOI = "ILLAOI"
    IRELIA = "IRELIA"
    IVERN = "IVERN"
    JANNA = "JANNA"
    JARVAN_IV = "JARVAN_IV"
    JAX = "JAX"
    JAYCE = "JAYCE"
    JHIN = "JHIN"
    JINX = "JINX"
    KAISA = "KAISA"
    KALISTA = "KALISTA"
    KARMA = "KARMA"
    KARTHUS = "KARTHUS"
    KASSADIN = "KASSADIN"
    KATARINA = "KATARINA"
    KAYLE = "KAYLE"
    KAYN = "KAYN"
    KENNEN = "KENNEN"
    KHA_ZIX = "KHA_ZIX"
    KINDRED = "KINDRED"
    KLED = "KLED"
    KOG_MAW = "KOG_MAW"
    LEBLANC = "LEBLANC"
    LEE_SIN = "LEE_SIN"
    LEONA = "LEONA"
    LILLIA = "LILLIA"
    LISSANDRA = "LISSANDRA"
    LUCIAN = "LUCIAN"
    LULU = "LULU"
    LUX = "LUX"
    MALPHITE = "MALPHITE"
    MALZAHAR = "MALZAHAR"
    MAOKAI = "MAOKAI"
    MASTER_YI = "MASTER_YI"
    MISS_FORTUNE = "MISS_FORTUNE"
    MORDEKAISER = "MORDEKAISER"
    MORGANA = "MORGANA"
    NAMI = "NAMI"
    NASUS = "NASUS"
    NAUTILUS = "NAUTILUS"
    NEEKO = "NEEKO"
    NIDALEE = "NIDALEE"
    NOCTURNE = "NOCTURNE"
    NUNU_AND_WILLUMP = "NUNU_AND_WILLUMP"
    OLAF = "OLAF"
    ORIANNA = "ORIANNA"
    ORNN = "ORNN"
    PANTHEON = "PANTHEON"
    POPPY = "POPPY"
    PYKE = "PYKE"
    QIYANA = "QIYANA"
    QUINN = "QUINN"


class Player:

    def __init__(self, account_id: str, champ_dict: dict, name: str, *args, **kwargs):
        self.account_id = account_id
        self.name = name
        self.champ_dict = champ_dict

    def __str__(self):
        return "name: {self.name}, account id:{self.account_id}".format(self=self)

    def update_champ_dict(self, champ_dict: dict[Champ:int], *args, **kwargs) -> Result:
        self.champ_dict = champ_dict
        return Result(error=Result.ErrorCode.ok)

    def get_champ_score(self, champ: Champ, *args, **kwargs) -> Result:
        champ_name = champ.name
        score = self.champ_dict[champ_name]
        return Result(error=Result.ErrorCode.ok, value=score)


if __name__ == '__main__':
    f = open('champs.json')
    # Read the JSON data
    json_data = f.read()
    f.close()
    champ_dict = json.loads(json_data)

    player = Player(account_id="123", name="yosef", champ_dict=champ_dict)
    print(player.champ_dict)
    result_obj = player.update_champ_dict(champ_dict=champ_dict)
    if result_obj.error != Result.ErrorCode.ok:
        print("could not update champ dict %s" % champ_dict)
    print(player.champ_dict)
    champ = Champ.AHRI
    result_obj = player.get_champ_score(champ=champ)
    if result_obj.error != Result.ErrorCode.ok:
        print("coulnd get %s score" % champ)
    print(result_obj.value)
