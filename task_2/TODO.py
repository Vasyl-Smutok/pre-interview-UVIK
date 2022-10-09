import csv
import os
from datetime import datetime


FIELDS = ["create_at", "item", "is done", "done_at"]


def add_items() -> None:
    with open(f"data.csv", "a") as file:
        writer = csv.writer(file)

        if os.stat("data.csv").st_size == 0:
            writer.writerow(FIELDS)

        item = input("Please enter item, if you want to stop press q ")

        while item != "q":
            writer.writerow([datetime.now().date(), item, False, "-"])

            item = input("Please enter item, if you want to stop press q ")


def red_all_data(path_to_data: str = "data.csv") -> None:
    with open(path_to_data, "r") as csv_file:
        print(csv_file.read())


def read_items(path_to_data: str = "data.csv") -> None:
    with open(path_to_data, "r") as csv_file:
        reader_obj = csv.DictReader(csv_file)
        print([item["item"] for item in reader_obj])


def remove_items() -> None:
    item_to_delete = input("Please enter item to delete, if you want to stop press q")
    while item_to_delete != "q":
        with open("data.csv", 'r+') as in_file:
            rows = [row for row in csv.reader(in_file) if item_to_delete not in row]
            in_file.seek(0)
            in_file.truncate()
            writer = csv.writer(in_file)
            writer.writerows(rows)

        item_to_delete = input("Please enter item to delete, if you want to stop press q")


def done_item() -> None:
    item_to_done = input("Please enter item to done, if you want to stop press q")

    while item_to_done != "q":
        r = csv.reader(open('data.csv'))
        lines = list(r)
        for line in lines:
            if line[1] == item_to_done:
                line[2] = "True"
                line[3] = datetime.now().date()

        item_to_done = input("Please enter item to delete, if you want to stop press q")

        writer = csv.writer(open('data.csv', 'w'))
        writer.writerows(lines)


if __name__ == '__main__':
    add_items()
    read_items()
    done_item()
    red_all_data()



