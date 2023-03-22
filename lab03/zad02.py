import pygad
import numpy

S = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
     [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
     [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
     [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
     [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
     [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# definiujemy parametry chromosomu
# geny to liczby: 0 lub 1
gene_space = [0, 1, 2, 3]  # 0 - prawo, 1 - lewo, 2 - dol, 3 - gora

# definiujemy funkcję fitness


def jest_w_macierzy(lista, macierz):
    if len(macierz) == 0:
        return False
    for i in macierz:
        if numpy.array_equal(i, lista):
            return True
    return False


def fitness_func(solution, solution_idx):
    start = numpy.array([1, 1])
    koniec = numpy.array([10, 10])
    ruchy = 0
    uderzenia = 0
    odwiedzone = []
    cofniecia = 0
    for i in solution:
        if jest_w_macierzy(start, odwiedzone) == False:
            odwiedzone.append(start)
        else:
            cofniecia += 1
        if numpy.array_equal(start, koniec):
            return 0-ruchy-uderzenia-cofniecia

        if i == 0:
            id = numpy.array([start[0], start[1]+1])
            next = S[id[0]][id[1]]
            if next == 0:
                start = id
                ruchy += 1

            else:
                ruchy += 1
                uderzenia += 1

        if i == 1:
            id = numpy.array([start[0], start[1]-1])
            next = S[id[0]][id[1]]
            if next == 0:
                start = id
                ruchy += 1
            else:
                ruchy += 1
                uderzenia += 1

        if i == 2:
            id = numpy.array([start[0]+1, start[1]])
            next = S[id[0]][id[1]]
            if next == 0:
                start = id
                ruchy += 1

            else:
                ruchy += 1
                uderzenia += 1

        if i == 3:
            id = numpy.array([start[0]-1, start[1]])
            next = S[id[0]][id[1]]
            if next == 0:
                start = id
                ruchy += 1
            else:
                ruchy += 1
                uderzenia += 1

    return -(abs(start[0]-koniec[0])+abs(start[1]-koniec[1])+uderzenia+cofniecia+ruchy)


def mapowanie(s):
    aktualne_pole = [1, 1]
    sciezka = []
    for i in s:
        sciezka.append(aktualne_pole)
        if numpy.array_equal(aktualne_pole, [10, 10]):
            return [sciezka, len(sciezka)]
        elif i == 0 and S[aktualne_pole[0]][aktualne_pole[1]+1] == 0:
            aktualne_pole = [aktualne_pole[0], aktualne_pole[1]+1]
        elif i == 1 and S[aktualne_pole[0]][aktualne_pole[1]-1] == 0:
            aktualne_pole = [aktualne_pole[0], aktualne_pole[1]-1]
        elif i == 2 and S[aktualne_pole[0]+1][aktualne_pole[1]] == 0:
            aktualne_pole = [aktualne_pole[0]+1, aktualne_pole[1]]
        elif i == 3 and S[aktualne_pole[0]-1][aktualne_pole[1]] == 0:
            aktualne_pole = [aktualne_pole[0]-1, aktualne_pole[1]]
    return [sciezka, len(sciezka)]


fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 500
num_genes = 30

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 250
num_generations = 800
keep_parents = 30

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 4

# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_0.0"])

# uruchomienie algorytmu
ga_instance.run()

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze parametry wybrane przez algorytm: {solution}".format(
    solution=solution))
print("Najlepsza wartość fitness wybrana przez algorytm: {solution_fitness}".format(
    solution_fitness=solution_fitness))

kroki = mapowanie(solution)[0]
ilosc_krokow = mapowanie(solution)[1]
print(kroki)
print("Liczba kroków: " + str(ilosc_krokow))

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
