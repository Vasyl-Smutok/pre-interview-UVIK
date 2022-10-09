import json


def read_and_group_csv_file(path_to_csv: str) -> dict:
    with open(path_to_csv, "r") as csv_file:
        all_country_and_people = csv_file.read().split("\n")[1:]

        return {
            country.split(",")[0]: {
                "people": [
                    people.split(",")[1]
                    for people in all_country_and_people
                    if people.split(",")[0] == country.split(",")[0]
                ],
                "count": len(
                    [
                        people.split(",")[1]
                        for people in all_country_and_people
                        if people.split(",")[0] == country.split(",")[0]
                    ]
                ),
            }
            for country in all_country_and_people
        }


if __name__ == "__main__":
    print(json.dumps(read_and_group_csv_file("data.csv"), indent=4))
