# Dokumentasi Praktikum Algoritma Genetika 1

**Identitas Mahasiswa:**
* Nama: Nalendra Wicaksana
* NIM: H1D024073
* Shift Lama: E
* Shift Baru: F

## 1. Tujuan Penugasan
Memahami, merancang, dan mengimplementasikan dasar-dasar pemecahan masalah optimasi menggunakan pendekatan evolusioner Algoritma Genetika (Algen). Fokus utama pada pertemuan ini adalah mengeksekusi model komputasi untuk menuntaskan studi kasus Knapsack Problem, yakni menemukan persentase konfigurasi maksimal pemuatan 9 variasi barang bawaan yang menghasilkan total keuntungan utilitas terbesar tanpa melampaui limitasi bobot kapasitas wadah sebesar 50 unit.

## 2. Struktur Repositori
- main.py : Berisi baris kode pemrograman Python utama.
- README.md : Berisi panduan teknis dan analisis operasional sistem.

## 3. Penjelasan Kerja Kode dan Dampak Output

### Kode Pemuatan Inisialisasi Populasi:
- kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
- populasi.append(kromosom)
#### Penjelasan Kode:
Fungsi inisialisasi ini membangun daftar sampel kumpulan susunan kromosom awal melalui pembentukan angka biner secara acak terdistribusi (nilai 0 atau 1) dengan memperhitungkan indeks unit parameter panjang gen (merepresentasikan 9 keping barang). 
#### Dampak Output:
Membentuk struktur matriks array populasi mentah perawan yang menandakan kemungkinan barang mana saja yang akan dibawa (1 berarti terpilih, 0 berarti ditinggal), untuk selanjutnya dievaluasi ke dalam model.

### Kode Evaluasi Fungsi Kelayakan (Fitness):
- if total_bobot > kapasitas_tas:
      return 0
- return total_harga
#### Penjelasan Kode:
Kalkulator penilaian kualitas individu iterasi (kromosom). Prosedurnya menghitung total akumulasi nilai margin dan beban barang yang tercetak memiliki penanda biner '1'. Pemeriksaan kelayakan (fitness constraints) memastikan bahwa jika total beban melampaui pagu toleransi tas kapasitas maksimal (50 unit bobot), secara seketika akan dikenakan sanksi diskualifikasi poin nol (0) agar solusi tersebut tereliminasi dari gen unggul.
#### Dampak Output:
Terbentuk peringkat skor evaluasi pada masing-masing individu untuk menyoroti solusi yang secara spesifik menjanjikan keseimbangan optimum pemecahan masalah.

### Kode Proses Seleksi (Roulette Wheel Selection):
- probabilitas = [fitness / total_fitness for fitness in fitness_populasi]
- for i, kum_prob in enumerate(kumulatif_prob):
      if r <= kum_prob:
          return populasi[i], i
#### Penjelasan Kode:
Fase transisi pemilihan individu tangguh penentu regenerasi menggunakan pendekatan analogi Roda Putar (Roulette Wheel). Probabilitas matematis bagi kromosom untuk maju sebagai tetua dihitung lewat komparasi nisbi (proporsional) total akumulasi nilai fitnessnya atas seluruh peserta di dalam populasinya.
#### Dampak Output:
Pola ini menjamin skema kompetisi persaingan yang sehat, di mana kromosom berlaba teratas memiliki preferensi lebih mendominasi pewarisan struktur gen selanjutnya tanpa mengikis habis sisa kesempatan individu inferior yang bisa jadi membawa struktur susunan DNA potensial adaptif.

### Kode Persilangan Kromosom (One-Point Crossover):
- titik_potong = random.randint(1, len(parent1)-1)
- anak1 = parent1[:titik_potong] + parent2[titik_potong:]
#### Penjelasan Kode:
Fungsi pengerjaan hibridisasi biologis rekaan (rekombinasi). Dua individu leluhur (parent) hasil seleksi Roda Putar dipenggal secara sejajar mendatar di satu titik koordinat potongan tak tentu, yang lantas untaian kepingan ekornya dipertukarkan untuk melahirkan cetak biru individu turunan independen.
#### Dampak Output:
Dua buah kromosom genetik subyek baru tercipta untuk dieksplorasi kembali, meningkatkan luas penampang rentang pencarian titik ekstrem ruang solusi permasalahan algoritma.

### Kode Mutasi Genetik (Swap Mutation):
- posisi1, posisi2 = random.sample(range(len(kromosom)), 2)
- kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
#### Penjelasan Kode:
Metode injeksi variasi acak sebagai mekanisme pelestarian entropi keragaman kromosom untuk mencegah homogenisasi fatal (konvergensi lokal buatan). Modifikasi dipicu dengan pertukaran rotasi penempatan gen biner secara saling silang terhadap dua indeks lokasi tak berhubungan.
#### Dampak Output:
Muncul anomali struktur solusi individu pada populasi pasca operasi reproduksi genetik yang merombak kebosanan stabilitas, memberikan dorongan inovasi optimasi pencarian.

### Kode Pelaksanaan Pelatihan (Generational Loop):
- plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', label='Fitness Tertinggi')
#### Penjelasan Kode:
Penanganan siklus iteratif berkelanjutan yang mengulang seluruh fase algoritma reproduksi genetika mulai dari seleksi, penyilangan, hingga mutasi secara berulang sampai kriteria generasi penghenti konstan 50 epoch terpenuhi. Setiap jejak rekam nilai efisiensi disimpan menggunakan fungsi visual grafik `matplotlib.pyplot`.
#### Dampak Output:
Menghadirkan grafik dua dimensi (2D) dinamika proses penemuan perbaikan nilai optimum. Serta menyajikan teks informasi ringkas di antarmuka eksekusi layar yang menyebutkan secara eksplisit himpunan jenis barang yang ideal direkomendasikan beserta parameter utilisasinya.
