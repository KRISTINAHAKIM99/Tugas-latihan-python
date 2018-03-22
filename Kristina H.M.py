from texttable import Texttable
table = Texttable ()
jawab = "y"
no = 0
nama = []
nim = []
nilai_tugas = []
nilai_uts = []
nilai_uas = []
while(jawab== "y") :
    nama.append(input("Masukkan Nama :"))
    nim.append(input("Masukkan Nim :"))
    nilai_tugas.append(input("Nilai Tugas :"))
    nilai_uts.append(input("Nilai Uts :"))
    nilai_uas.append(input("Nilai Uas :"))
    jawab = input("Tambah data (Y/T)?")
    no +=1
for i in range(no):
    nt = int(nilai_tugas[i])
    nu = int(nilai_uts[i])
    na = int(nilai_uas[i])
    akhir = (nt*30/100) + (nu*35/100) + (na*35/100)
    table.add_rows([['No','Nama','NIM','Tugas','UTS','UAS','Akhir'],[i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])
print (table.draw())
    
                           
    
    
