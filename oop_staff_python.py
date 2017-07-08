class Karyawan:


    jml_karyawan = 0 #Class variable

    #constructor
    def __init__(self,kid,nama,jabatan,pendidikan):

        self.kid = kid
        self.nama = nama
        self.jabatan = jabatan
        self.pendidikan = pendidikan
        Karyawan.jml_karyawan += 1

    #method
    def infoKaryawan(self):

        print ("Karyawan baru masuk")
        print ("===================")
        print ("ID : %s " % self.kid)
        print ("Nama : %s " % self.nama)
        print ("Jabatan : %s " % self.jabatan)
        print ("Pendidikan : %s " % self.pendidikan)


#cara mengakses/memakai class/membuat Object

obj = Karyawan("K001","Ganjar","Data Analyst","S1")
obj.infoKaryawan()

#tambah karyawan baru
obj2 = Karyawan("K002","Nadya","IT Support","D3")
obj2.infoKaryawan()

obj3 = Karyawan("K003", "Akbar", "Manager","S2")
obj3.infoKaryawan()

#tampilkan total Karyawan
print ("-----------------------------")
print ("Total Karyawan : %d " % Karyawan.jml_karyawan)
