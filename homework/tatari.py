from collections import defaultdict
from datetime import datetime

from homework.constant import *
from homework.io_csv import IOCsv
from homework.panda import *
from homework.spot import *


def populate_spots(csv_spots, rotations):
    """
    Populate a list of Spot Objects
    :param csv_spots: Dict Reader csv of Spots
    :param rotations: default dict of rotation hours
    :return: list of Spot Objects
    """
    results = []
    for spot in csv_spots:
        # Convert strings to dt
        spot_dt = datetime.strptime(
            "%s %s" % (spot['Date'], spot['Time']),
            " ".join(
                [DATE_FMT, TIME_FMT]
            )
        )

        # Rotations didn't cover 24H clock assign N/A to outside of main hours
        rotation = rotations.get(spot_dt.hour, ["N/A"])

        item = Spot(str(spot_dt.date()), str(spot_dt.time()), spot['Creative'], spot['Views'], spot['Spend'], rotation)
        results.append(item)
    return results


def populate_rotations(rotations_csv):
    """
    Rotations are on an hourly split put them in a hash/dict for quick lookup
    I'm sure there is a way to merge both data sets in pandas, didn't have time to tinker with it
    :param rotations_csv:
    :return:
    """
    rotations = defaultdict(list)
    for rotation in rotations_csv:
        start_dt = datetime.strptime(rotation["Start"], TIME_FMT)
        end_dt = datetime.strptime(rotation["End"], TIME_FMT)
        name = rotation["Name"]

        for dt in range(start_dt.hour, end_dt.hour + 1):
            rotations[dt].append(name)

    return rotations


def main():
    """
    A boring main func
    :return:
    """
    logger.info("Reading %s" % ROTATIONS_FILE)
    rotations_csv = IOCsv().read(ROTATIONS_FILE, ROTATION_HEADER)

    logger.info("Reading %s" % SPOTS_FILE)
    spots_csv = IOCsv().read(SPOTS_FILE, SPOT_HEADER)

    logger.info("Populating Rotations")
    rotations = populate_rotations(rotations_csv)
    logger.info("Populating Spots")
    spots = populate_spots(spots_csv, rotations)
    logger.info("Populating Spots")
    cpv = cpv_creatives(spots)
    cpv.to_csv("cpv_by_creative.csv")
    cpv_rotations = cpv_rotations_days(spots)
    cpv_rotations.to_csv("cpv_by_date_rotation.csv")


if __name__ == "__main__":
    """
    The Entry Point
    """
    main()
