import random
class Maplist:

    # initialize stages and modes using an infile.
    def __init__(self, infile = ""):
        self.game_modes = []
        self.stages = []

        if(infile != ""): # empty files will be treated as an empty maplist

            with open("./maps/" + infile + ".csv") as f:
                for line in f:
                    # each line in file is "GAMEMODE, STAGE"
                    linecontent = line.split(",")
                    currmode = linecontent[0].strip()
                    currstage = linecontent[1].strip()
                    # get index of currmode in game_modes
                    game_modes_index = self.game_modes.index(currmode) if currmode in self.game_modes else None
                    # game mode not in list yet
                    if(game_modes_index == None):
                        self.game_modes.append(currmode)
                        self.stages.append([])
                        game_modes_index = len(self.game_modes) - 1
                    self.stages[game_modes_index].append(currstage)

    def __str__(self):
        s = ""
        for i, mode in enumerate(self.game_modes):
            for stage in self.stages[i]:
                s += mode + " on " + stage + "\n"

        return s

    def randomMaps(self, nummaps):
        random_maps = []
        # initialize maplist as 2d array
        for i, mode in enumerate(self.game_modes):
            modestages = []
            for stage in self.stages[i]:
                modestages.append((mode, stage)) 
            random.shuffle(modestages)
            random_maps.append(modestages)

        num_modes = len(random_maps)
        # tick represents our current 
        tick = random.randint(0, num_modes - 1)
        final_maps = []
        for i in range(nummaps):
            final_maps.append(random_maps[tick].pop(0))
            # if last remaining map in , reset the ordering.
            if(len(random_maps[tick]) == 0):
                for stage in self.stages[tick]:
                    random_maps[tick].append((self.game_modes[tick], stage))
                random.shuffle(random_maps[tick])

            # increment, circle back to 0.
            tick = (tick + 1) % num_modes

        return final_maps

    
def test():
    test_maps = Maplist('inktv')
    print(test_maps)
    print(test_maps.randomMaps(10))
    test_empty_maps = Maplist()

def setup(bot):
    pass

if __name__ == "__main__":
    test()