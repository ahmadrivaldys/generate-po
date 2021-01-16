# Meng-import modul waktu
import datetime

# Membuat class
class GeneratePO:

	# Constructor
	def __init__(self, jenis_produk, kode_produk):
		self.jenis_produk = jenis_produk
		self.kode_produk  = kode_produk

	def generate_kode_PO(self):

		# --------- (1) Membuat Kode Jenis Produk
		# 
		# Catatan:
		# Variabel jenis_produk di bawah ini berbeda dengan self.jenis_produk
		# yang diperoleh dari constructor di atas

		# Membuat kode jenis produk dari jenis produk yang telah di-input user
		if(self.jenis_produk == "Makanan" or self.jenis_produk == "makanan"):
			jenis_produk = "MK"
		elif(self.jenis_produk == "Barang" or self.jenis_produk == "barang"):
			jenis_produk = "BG"
		elif(self.jenis_produk == "Jasa" or self.jenis_produk == "jasa"):
			jenis_produk = "JS"
		else:
			jenis_produk = "OO"


		# --------- (2) Membuat Kode Waktu
		# 
		waktu   = datetime.datetime.now() # Mengambil waktu saat ini
		tahun   = waktu.strftime("%y") # Membuat tahun dalam format dua digit angka saja, misal: 2020 menjadi 20
		bulan   = waktu.strftime("%m") # Membuat bulan dalam format angka
		tanggal = waktu.strftime("%d") # Membuat tanggal dalam format dua digit, misal '09' bukan '9'

		# Menggabungkan waktu hari ini untuk format kode produk nantinya
		kode_waktu = "{}{}{}".format(tahun, bulan, tanggal)


		# --------- (3) Membuat Kode Produk
		# 
		# Menambahkan 1 angka kode produk, misal kode yang di-input user adalah 7 maka menjadi 8
		kode_produk     = self.kode_produk + 1
		
		# Menghitung jumlah digit kode produk dengan mengubahnya terlebih dulu
		# ke string dengan fungsi str(), kemudian dihitung jumlah karakternya dengan fungsi len()
		jum_kode_produk = len(str(kode_produk))

		# Menambahkan digit 0 di depan kode produk
		if(jum_kode_produk == 1):
			kode_produk = "000{}".format(kode_produk)
		elif(jum_kode_produk == 2):
			kode_produk = "00{}".format(kode_produk)
		elif(jum_kode_produk == 3):
			kode_produk = "0{}".format(kode_produk)
		elif(jum_kode_produk == 4):
			kode_produk = kode_produk
		else:
			kode_produk = kode_produk


		# --------- (4) Membuat Kode Purchase Order (PO)
		# 
		# Menggabungkan semua format kode menjadi Kode PO
		kode_PO = "PO{}{}{}".format(jenis_produk, kode_waktu, kode_produk)
		

		# --------- (5) Mencetak Kode Purchase Order (PO)
		# 
		print("\n-- Berikut adalah kode yang sukses dihasilkan : " + kode_PO)


# Teks Pembuka
print("---------------------------------------------------------------------------")
print("|              Program Generate Purchase Order dengan Python              |")
print("---------------------------------------------------------------------------")
print("\n")

# Input yang diterima disimpan dulu ke dalam variabel
input_JP = input(">> Silakan masukkan jenis produk              : ")
input_KP = int(input(">> Silakan masukkan kode produk (hanya angka) : "))

# Masukkan input ke dalam constructor class GeneratePO
hasil    = GeneratePO(input_JP, input_KP)

# Jalankan fungsi generate
hasil.generate_kode_PO()
