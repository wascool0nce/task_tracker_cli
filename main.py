import datetime
import typer
import json
import os


app = typer.Typer()


def read_json_file():
    if not os.path.exists("data.json"):
        write_json_file([])
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(data: dict):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


@app.command()
def add_task(name: str, date_create: str=datetime.datetime.now(), status: str="backlog", description: str=""):
    task_tracker = read_json_file()
    last_id = 1
    if task_tracker != []:
        last_id = task_tracker[-1].get('id') + 1
    new_task = {
        "id": last_id,
        "name": name,
        "description": description,
        "status": status,
        "date_create": date_create
    }
    task_tracker.append(new_task)
    write_json_file(task_tracker)
    print("ok")


@app.command()
def get_task(id_task: int):
    list_tasks = read_json_file()
    for task in list_tasks:
        if id_task == task.get("id"):
            print(task)
            break


@app.command()
def get_list_tasks():
    list_tasks = read_json_file()
    print(list_tasks)


@app.command()
def delete_task(id_task: int):
    list_tasks = read_json_file()

    for task in list_tasks:
        if task["id"] == id_task:
            list_tasks.remove(task)
            break
    write_json_file(list_tasks)
    print("ok")


if __name__ == "__main__":
    app()
    