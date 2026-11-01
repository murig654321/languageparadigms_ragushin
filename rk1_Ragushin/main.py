from operator import itemgetter


class Program:

    def __init__(self, id, title, size, comp_id):
        self.id = id
        self.title = title
        self.size = size 
        self.comp_id = comp_id


class Comp:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProgramComp:

    def __init__(self, comp_id, prog_id):
        self.comp_id = comp_id
        self.prog_id = prog_id


comps = [
    Comp(1, "ПК-Лабораторный 1"),
    Comp(2, "Сервер Разработки"),
    Comp(3, "Административный ПК"),
]

progs = [
    Program(1, "Adobe Photoshop", 3500, 1),
    Program(2, "AutoCAD", 5000, 1),
    Program(3, "Antivirus Kaspersky", 800, 2),
    Program(4, "Blender 3D", 1200, 2),
    Program(5, "Archiver WinRAR", 10, 3),
]

progs_comps = [
    ProgramComp(1, 1),
    ProgramComp(1, 2),
    ProgramComp(2, 3),
    ProgramComp(2, 4),
    ProgramComp(3, 5),
    ProgramComp(3, 1),  
]


def main():

    one_to_many = [
        (p.title, p.size, c.name)
        for c in comps
        for p in progs
        if p.comp_id == c.id
    ]

    many_to_many_temp = [
        (c.name, pc.comp_id, pc.prog_id)
        for c in comps
        for pc in progs_comps
        if c.id == pc.comp_id
    ]

    many_to_many = [
        (p.title, p.size, comp_name)
        for comp_name, comp_id, prog_id in many_to_many_temp
        for p in progs
        if p.id == prog_id
    ]

    print("Задание В1:")
    res_v1 = [
        (p_title, comp_name)
        for p_title, _, comp_name in one_to_many
        if p_title.startswith("A") or p_title.startswith("А")
    ]
    print(res_v1)

    print("\nЗадание В2:")
    res_v2_unsorted = []
    for c in comps:
        c_progs = list(filter(lambda item: item[2] == c.name, one_to_many))
        if len(c_progs) > 0:
            c_sizes = [size for _, size, _ in c_progs]
            min_size = min(c_sizes)
            res_v2_unsorted.append((c.name, min_size))

    res_v2 = sorted(res_v2_unsorted, key=itemgetter(1))
    print(res_v2)

    print("\nЗадание В3:")
    res_v3 = sorted(many_to_many, key=itemgetter(0))
    print(res_v3)


if __name__ == "__main__":
    main()