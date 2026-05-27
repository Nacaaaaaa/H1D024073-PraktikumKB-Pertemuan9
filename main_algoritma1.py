import random
import matplotlib.pyplot as plt

# 1. Metode Inisialisasi Populasi
def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    populasi = []
    for i in range(jumlah_populasi):
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)
    return populasi

# 2. Metode Evaluasi Fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]
            total_bobot += barang[i][2]
            
    if total_bobot > kapasitas_tas:
        return 0 # Penalti jika melebihi kapasitas tas
    return total_harga

# 3. Metode Seleksi (Roulette Wheel Selection)
def roulette_wheel_selection(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx

    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]
    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i
            
    return populasi[-1], len(populasi)-1

# 4. Metode Crossover (One-Point Crossover)
def one_point_crossover(parent1, parent2):
    titik_potong = random.randint(1, len(parent1)-1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2

# 5. Metode Mutasi (Swap Mutation)
def swap_mutation(kromosom):
    kromosom = list(kromosom)
    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)
    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
    return kromosom

# Data barang: (nama, nilai, berat)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 69, 11),
    ("Barang6", 70, 9),
    ("Barang7", 80, 15),
    ("Barang8", 90, 10),
    ("Barang9", 25, 3)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas_tas):
    jumlah_gen = len(barang)
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]

    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []

    best_individu = None
    best_fitness_overall = 0

    for generasi in range(jumlah_generasi):
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]

        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)

        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())

        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best]

        new_populasi = []
        used_indices = []

        while len(new_populasi) < jumlah_populasi:
            parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)
            used_indices.append(idx1)

            available_indices = [i for i in range(len(populasi)) if i not in used_indices]
            if not available_indices:
                used_indices = [idx1]
                available_indices = [i for i in range(len(populasi)) if i != idx1]
            
            parent2, _ = roulette_wheel_selection(
                [populasi[i] for i in available_indices], 
                [fitness_populasi[i] for i in available_indices]
            )

            if random.random() < prob_crossover:
                anak1, anak2 = one_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]

            if random.random() < prob_mutasi:
                anak1 = swap_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = swap_mutation(anak2)

            new_populasi.extend([anak1, anak2])

        populasi = new_populasi[:jumlah_populasi]

    # Menampilkan grafik fitness
    plt.figure(figsize=(12, 7))
    for i in range(jumlah_generasi):
        x = [i+1]*len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)

    plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi+1), worst_fitness_list, color='yellow', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi+1), avg_fitness_list, color='red', label='Fitness Rata-rata')
    plt.title('Perkembangan Nilai Fitness')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Menampilkan barang yang terpilih
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, kapasitas_tas)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

    print(f"Nilai Fitness Terbaik: {selected_value}")
    print(f"Total Bobot: {selected_weight}")
    print("Barang Terpilih:")
    for item in selected_items:
        print(f"  - {item}")

if __name__ == "__main__":
    run_ga(
        jumlah_generasi=50,
        jumlah_populasi=20,
        prob_crossover=0.5,
        prob_mutasi=0.1,
        kapasitas_tas=50
    )