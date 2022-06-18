import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index(["FROM", "EDGE_ID"])

class SessionState:
    def __init__(self) -> None:
        self.n_potions = 0
        self.current_state = "T_I_1"

    def decide(self, option_num):
        self.current_state = edge_data.loc[(self.current_state, option_num), "TO"]
        
    def proc_input(self, in_str):

        if in_str == "Gimme potion":
            self.n_potions += 1

        return f"You have {self.n_potions} potions"