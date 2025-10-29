import pathlib


def piska(word, num, flag=False):
    if not flag:
        print("Иди в жопу")
    else:
        print(word, num)


def collect_files(target):
    files = []
    target_path = pathlib.Path(target)
    for obj in target_path.rglob("*.txt"):
        files.append(obj.name)
    return files


print(collect_files(r"C:\Users\TatyanaPC\Documents\Test_for_lab2"))
