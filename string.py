# STRING
string0 = "MUHAMMAD FARHAN" #Nama
string1 = "5054241018" #NRP
string2 = "Grobogan" # asal daerah

# Print string
print("Nama Saya adalah" , string0)
print("NRP saya " , string1)
print("Asal saya dari daerah " , string2)

# Acces Character in string 
print("Inisial saya", string0[0]+string0[9])

# Slicing
print("Nama Awal Saya",string0[0:8])
print("Nama Belakang Saya",string0[9:15])
print("Nama Panggilan Saya",string0[9:15])

# Reverse String 
print("Reverse dari NRP saya", string1[::-1])

string3 = "Saya Mahasiswa RKA"
list3 = list(string3)
list3[4] = " Bukan "
string4 = ''.join(list3)
string5 = string4[0:20] + " RPL "
print(string5)


# #Tugas inplementasi

#1 Deleting a character dari kota asal
delet = string2[:5] + string2[7:] # menghilangkan huruf ke 5 -6
print(delet)  

#2. Escape Sequencing in Python + Example
# - print Farhan menggunakan octal escape sequance 
String6 = "\106\141\162\150\141\156"
print(String6)
# Menggunakan escape sequence hexadecimal untuk "Muhammad Farhan"
String7 ="\x4D\x75\x68\x61\x6D\x6D\x61\x64\x20\x46\x61\x72\x68\x61\x6E"
print(String7)
#  'r' Raw String untuk Mengabaikan Escape Sequences pada Hexadecimal
String8 = r"\x4D\x75\x68\x61\x6D\x6D\x61\x64\x20\x46\x61\x72\x68\x61\x6E"
print(String8)
# penggunaan escape sequance untuk Newline '\n'
print ("Hello\nWorld")
# penggunaan escape sequance untuk tab '\t'
print ("Hello\tWorld")
# penggunaan escape sequance untuk backlash '\' dengan '\\'
print("backslash: \\")
#  penggunaan escape sequance untuk tanda petik ganda 
print("\"Hello World\"")

#3 Python String Formating (Example 1, 2, 3, 4)
# Example 1 string {} berfungsi menyimpan nilai  untuk melihat posisi deklarasi string
name = "Farhan"
age = 20
# Menggunakan f-string
string = f"My name is {name} and I am {age} years old."
print(string)
# Default order
String1 = "{} {} {}".format('Negara', 'Republik', 'Indonesia')
print("urutan default: ")
print(String1)
# Keyword Formatting
String2 = "{a} {b} {c} {d}".format(c='artifisial', b='kecerdasan', a='rekayasa', d='(RKA)')
print("\n berdasarkan Kata Kunci: ")
print(String2)
#Positional Formatting
String3 = "{1} {2} {0} {4} {3}".format('Sepuluh', 'Institut', 'Teknologi', 'Surabaya', 'Nopember' )
print("\nPrint urutan Posisi: ")
print(String3)

# Example 2 formating bilangan bulat (integer) dan bilangan pecahan9float)
# Rounding off (Pembulatan)
r = 5
a = 3.14 * r **2
String4 = f"Luas lingkaran dengan jari jari {r} adalah sekitar {a:.2f}."
print(String4)
# Mengubah bilangan bulat menjadi bentuk heksadesimal.
String5 = "{0:x}".format(255)
print("Representasi heksadesimal dari 255 (huruf kecil): ")
print(String5)
#  (Angka dengan Nol Awal)
String6 = "{0:05d}".format(86)
print("Angka 86 dengan nol di depan: ")
print(String6)
# Mengubah bilangan bulat menjadi bentuk biner.
String7 = "{0:b}".format(112)
print("Representasi biner dari 112: ")
print(String7)
# Mengubah bilangan bulat menjadi bentuk oktal.
String8 = "{0:o}".format(52)
print("Representasi oktal dari 52: ")
print(String8)

# Example 3 penentu format untuk menyelaraskan string ke kiri, kanan, atau tengah dalam bidang yang lebarnya ditentukan.
# Menyelaraskan ke kiri dengan pengisi underscore (_):
String9 = "{:_<10}".format("Farhan")
print("String disejajarkan ke kiri dengan '_': ")
print(String9)
#Menyelaraskan ke kanan dengan pengisi titik (.):
String10 = "{:.>10}".format("Farhan")
print("String disejajarkan ke kiri dengan '.': ")
print(String10)
#Menyelaraskan ke tengah dengan pengisi bintang (*):
String10 = "{:.^10}".format("Python")
print("String disejajarkan ke tengah dengan '.': ")
print(String10)
#To demonstrate aligning of spaces
String11 = "\n{0:15} lahir di tahun {1:^4}.".format("Muhammad Farhan", 2006)
print(String11)
# penggunaan old-style formatting di Python menggunakan operator %
# Format integer
umur = 19
print("Umur Saya %d Tahun." % umur)
# format float
pi = 3.14159
print("penulisan lain dari 22/7 adalah %.2f." % pi)
# Format String
nama = "Muhammad Farhan"
print("Nama saya %s." % nama)
#Memformat Bilangan oktal dan Heksadesimal
number = 255
# Bilangan dalam heksadesimal
print("The number in hexadecimal is: %x." % number)
# Bilangan dalam oktal
print("The number in octal is: %o." % number)



#Konten yang berbeda dari contoh di geekforgeek mendapat nilai tambahan