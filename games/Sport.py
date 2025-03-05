class Sport:
    '''Clase para representar un deporte'''
    def __init__(self, name:str, players:int, league:str):
        """Constructor de Sport"""
        self.name = name
        if insinstance(players) != int:
            self.players = int(players)
        self.league = league
        
    def __str__(self):
        return f"Sport: {self.name}, {self.players}, {self.league}"        
    def __repr__(self)->str:
        """ Representación en string Sport """
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    def to_json(self)->dict:
        """ Convertir Sport a JSON"""
        return {"name":self.name, "players":self.players, "league": self.league}
    