<h1><b>FEATURE DOCUMENTATION</b></h1>

<h2><b>ISPU</b></h2>

<b>periode_data</b> : Menunjukkan rentang waktu pelaporan data<br>
<b>tanggal</b> : Tanggal pengambilan sampel data kualitas udara<br>
<b>stasiun</b> : Lokasi atau ID stasiun pemantau kualitas udara (SPKU) di Jakarta<br>
<b>pm_sepuluh</b> : Konsentrasi Particulate Matter (PM_10), yaitu partikel udara yang berukuran lebih kecil dari 10 mikrometer<br>
<b>pm_duakomalima</b> : Konsentrasi Particulate Matter (PM_2.5), partikel halus berukuran < 2.5 mikrometer<br>
<b>sulfur_dioksida</b> : Konsentrasi Sulfur Dioksida (SO_2), gas yang biasanya dihasilkan dari pembakaran bahan bakar fosil yang mengandung belerang<br>
<b>karbon_monoksida</b> : Konsentrasi Karbon Monoksida (CO), gas tidak berwarna dan tidak berbau hasil pembakaran tidak sempurna (terutama kendaraan bermotor)<br>
<b>ozon</b> : Konsentrasi Ozon Permukaan (O_3), polutan sekunder yang terbentuk akibat reaksi kimia antara polutan lain di bawah sinar matahari<br>
<b>nitrogen_dioksida</b> : Konsentrasi Nitrogen Dioksida (NO_2), gas yang dihasilkan dari proses pembakaran suhu tinggi, seperti pada mesin kendaraan dan industri<br>
<b>max</b> : Nilai indeks tertinggi di antara seluruh parameter pencemar yang diukur pada hari dan lokasi tersebut<br>
<b>parameter_pencemar_kritis</b> : Nama parameter (misal: PM_2.5 atau O_3) yang memiliki nilai indeks paling tinggi dan menentukan nilai max<br>
<b>kategori</b> : Target Label (Variabel Dependen)<br>

---

<h2><b>NDVI</b></h2>
<b>tanggal</b> : Merupakan waktu pengambilan data indeks vegetasi.<br>
<b>stasiun_id</b> : Identitas unik atau kode stasiun pemantau kualitas udara.<br>
<b>ndvi (Normalized Difference Vegetation Index)</b> : Nilai numerik yang menunjukkan tingkat kerapatan vegetasi di sekitar stasiun<br>

---

<h2><b>cuaca-harian</b></h2>
<b>time</b> : Tanggal pencatatan data cuaca yang dapat disinkronkan dengan data ISPU<br>
<b>temperature_2m (max, min, mean)</b> : Suhu udara pada ketinggian 2 meter di atas permukaan tanah (maksimum, minimum, dan rata-rata) dalam derajat Celcius (°C)<br>
<b>precipitation (sum, hours)</b> : Total curah hujan harian (mm) dan durasi terjadinya hujan dalam sehari (jam)<br>
<b>wind_speed_10m (max, mean, min)</b> : Kecepatan angin pada ketinggian 10 meter (maksimum, rata-rata, dan minimum) dalam km/jam<br>
<b>wind_direction_10m_dominant & winddirection_10m_dominant</b> : Arah angin dominan dalam derajat (°)<br>
<b>wind_gusts_10m (max, mean, min)</b> : Kecepatan hembusan angin mendadak (maksimum, rata-rata, dan minimum)<br>
<b>shortwave_radiation_sum</b> : Total radiasi matahari gelombang pendek (MJ/m²)<br>
<b>relative_humidity_2m (mean, max, min)</b> : Kelembapan relatif udara (rata-rata, maksimum, dan minimum) dalam persen (%)<br>
<b>cloud_cover (mean, max, min)</b> : Persentase tutupan awan (rata-rata, maksimum, dan minimum)<br>
<b>surface_pressure (mean, max, min)</b> : Tekanan udara di permukaan (rata-rata, maksimum, dan minimum) dalam hPa<br>

---

<h2><b>jumlah-penduduk</b></h2>
<b>periode_data & tahun</b> : Menunjukkan waktu pendataan penduduk untuk melihat tren pertumbuhan demografi secara berkala<br>
<b>nama_provinsi, kabupaten_kota, kecamatan, & kelurahan</b> : Hierarki wilayah administratif di Jakarta<br>
<b>usia</b> : Kelompok umur penduduk<br>
<b>jenis_kelamin</b> : laki-laki atau perempuan<br>
<b>jumlah_penduduk</b> : Total jiwa pada kategori wilayah dan kelompok tertentu<br>

---

<h2><b>kualitas-air-sungai</b></h2>
<b>periode_data</b> : Menunjukkan tahun pelaporan data<br>
<b>periode_pemantauan</b> : Siklus atau tahap pengambilan sampel dalam satu tahun<br>
<b>bulan_sampling</b> : Angka yang menunjukkan bulan saat sampel air diambil<br>
<b>titik_sampel</b> : Kode identifikasi lokasi spesifik pengambilan sampel di sungai<br>
<b>nama_sungai</b> : Nama aliran sungai tempat data diambil<br>
<b>alamat</b> : Lokasi fisik atau keterangan jalan terdekat dari titik pengambilan sampel<br>
<b>latitude</b> : Koordinat garis lintang untuk pemetaan posisi geografis<br>
<b>longitude</b> : Koordinat garis bujur untuk pemetaan posisi geografis<br>
<b>jenis_parameter</b> : Kategori pengujian yang dilakukan, seperti kimia, fisika, atau biologi<br>
<b>parameter</b> : Unsur spesifik yang diukur nilainya<br>
<b>baku_mutu</b> : Nilai standar atau ambang batas maksimal yang ditetapkan oleh regulasi lingkungan<br>
<b>hasil_pengukuran</b> : Angka riil hasil pengujian di lapangan yang akan dibandingkan dengan baku mutu<br>

---

<h2><b>libur-nasional</b></h2>
<b>tanggal</b><br>
<b>is_holiday_nasional</b> : Indikator biner (1 atau 0) yang menandakan apakah hari tersebut merupakan hari libur nasional resmi<br>
<b>nama_libur</b> : nama resmi dari hari raya atau hari besar yang diperingati<br>
<b>is_weekend</b> : Indikator biner (1 atau 0) yang menandakan apakah hari tersebut adalah hari Sabtu atau Minggu<br>
<b>day_name</b> : Nama hari dalam seminggu (contoh: Senin, Selasa, dst)<br>