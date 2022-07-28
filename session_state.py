import pandas as pd
import boto3

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIASJIEFZIWUUY5K5DG',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
)

RAJK_ZORK_edges_from_AWS_server = client.get_object(
    Bucket = 'szovegek',
    Key = 'RAJK_ZORK_edges.csv'
)
edge_data = pd.read_csv(RAJK_ZORK_edges_from_AWS_server['Body']).set_index(["FROM", "OPTION_NUM"])


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
        self.user_id = ""

    def decide(self, option_num):
        self.current_state = edge_data.loc[(self.current_state, option_num), "TO"]
        
    def proc_input(self, in_str):

        if in_str == "Gimme potion":
            self.n_potions += 1

        return f"You have {self.n_potions} potions"


class Starting_SessionState:
    def __init__(self) -> None:
        self.current_state = "T_I_1"