10 soal latihan

Dasar (input, output, kondisi)

Konverter suhu: input suhu Celsius, tampilkan Fahrenheit dan Kelvin.
Ganjil atau genap: input sebuah bilangan, tampilkan apakah ganjil atau genap, positif, negatif, atau nol.
Kalkulator sederhana: input dua angka dan satu operator (+ - * /), tampilkan hasilnya. Tangani pembagian dengan nol.

Perulangan
4. Tabel perkalian: input angka N, tampilkan tabel perkalian N dari 1 sampai 10.
5. FizzBuzz: cetak 1 sampai 100. Kelipatan 3 tampil “Fizz”, kelipatan 5 tampil “Buzz”, kelipatan keduanya tampil “FizzBuzz”.
6. Segitiga bintang: input tinggi N, cetak pola segitiga dari karakter *.

Array / List
7. Statistik angka: input beberapa angka (berhenti saat input 0), tampilkan jumlah, rata-rata, nilai terbesar, dan terkecil.
8. Balik string dan cek palindrom: input kata, tampilkan versi terbaliknya, lalu cek apakah palindrom (contoh: “katak”).

Fungsi / method
9. Cek bilangan prima: buat fungsi IsPrima(n), lalu tampilkan semua bilangan prima dari 1 sampai 100.
10. Game tebak angka: komputer memilih angka acak 1-100, user menebak. Beri petunjuk “terlalu besar/kecil” dan hitung jumlah tebakan.

Catatan C++ ke C# (supaya cepat)
Hal	C++	C#
Output	cout << x << endl;	Console.WriteLine(x);
Input	cin >> x;	string s = Console.ReadLine();
Konversi ke angka	otomatis lewat cin	int.Parse(s) atau int.TryParse(s, out int x)
String format	printf	$"Halo {nama}"
Array dinamis	vector<int>	List<int>
Angka acak	rand()	new Random().Next(1, 101)
Memori	manual	otomatis (tidak perlu delete)

Beberapa hal yang sering bikin orang dari C++ bingung: tidak ada pointer di penggunaan sehari-hari, tidak ada header file, string dan bool ditulis huruf kecil tapi tetap tipe bawaan, dan semua kode harus berada di dalam class atau memakai top-level statements seperti di Program.cs kamu sekarang.
