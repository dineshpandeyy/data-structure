class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        play = 0
        train = 0
        result = 0

        while play < len(players) and train < len(trainers):
            if trainers[train] >=  players[play]:
                result += 1
                play += 1
            train += 1
        return result
        