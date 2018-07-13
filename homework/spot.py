
class Spot:
    """
    Contains Spot Object + Rotation definition
    """

    def __init__(self, date, time, creative, views, spend, rotation):
        self.date = date
        self.time = time
        self.creative = creative
        self.views = int(views)
        self.spend = float(spend)
        self.rotation = rotation


# Define Header Fields better place to put this?
DATE = "Date"
TIME = "Time"
CREATIVE = "Creative"
SPEND = "Spend"
VIEWS = "Views"

SPOT_HEADER = [
    DATE, TIME, CREATIVE, SPEND, VIEWS
]

START = "Start"
END = "End"
NAME = "Name"

ROTATION_HEADER = [
    START, END, NAME
]
