import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index(["FROM", "OPTION_NUM"])

class SessionState:
    def __init__(self) -> None:
        self.n_potions = 0
        self.current_state = "T_I_1"
        self.onzo_pleaser = 0
        self.bika_nyuszi = 0
        self.szutykos_guru = 0
        self.naplopo_hajcsar = 0
        self.elszivott_cigik = 0
        self.tarot = ""
        

    def decide(self, option_num):
        self.current_state = edge_data.loc[(self.current_state, option_num), "TO"]
        
    def proc_input(self, in_str):

        if in_str == "Gimme potion":
            self.n_potions += 1

        return f"You have {self.n_potions} potions"