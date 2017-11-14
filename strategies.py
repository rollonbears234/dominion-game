"""
Used to make my strategies testing in the play

Beginning strategies should default to buying a province if they have money -> get some convergence
"""

strategies = ["random", "max_actions", "max_money", "balance"]

working_cards = ["MOAT", "MERCHANT", "VASSAL", "VILLAGE",
            "GARDENS", "MILITIA", "MONEYLENDER", "SMITHY",
            "COUNCIL ROOM", "FESTIVAL", "LABORATORY", "MARKET"]


class Strategy():


    """
    will have an interface for decision making (buy or play or end)
    will differ those decisions based on the strategy name
    """

    def __init__(self, strategy_name = "random"):
        self.strategy_name = strategy_name
