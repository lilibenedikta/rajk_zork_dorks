import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index(["FROM", "OPTION_NUM"])

class SessionState:
    def __init__(self) -> None:
        self.user_id = ""
        self.chapter = 1
        self.current_state = "T_I_1"
        self.current_number_of_state = 0
        self.onzo_pleaser = 0
        self.bika_nyuszi = 0
        self.szutykos_guru = 0
        self.naplopo_hajcsar = 0
        #self.elszivott_cigik = 0
        self.tarot = ""

    def decide(self, option_num):
        self.current_state = edge_data.loc[(self.current_state, option_num), "TO"]
        self.onzo_pleaser += edge_data.loc[(self.current_state, option_num), "ONZO_PLEASER"]
        self.bika_nyuszi += edge_data.loc[(self.current_state, option_num), "BIKA_NYUSZI"]
        self.bika_nyuszi += edge_data.loc[(self.current_state, option_num), "SZUTYKOS_GURU"]
        self.bika_nyuszi += edge_data.loc[(self.current_state, option_num), "NAPLOPO_HAJCSAR"]

    def choice_num(self, click_num):
        if click_num > 0:
            self.current_number_of_state += 1

    def next_chapter(self, n_clicks):
        if n_clicks:
            self.chapter += 1
