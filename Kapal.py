
from abc import ABC, abstractmethod

class KapalAbstract(ABC):
    
    @property
    @abstractmethod
    def kapal_property(self):
        pass
    
    @abstractmethod
    def simpan_data(self):
        pass

class KapalInterface(KapalAbstract):

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi):
        self.cleats = cleats
        self.haluan = haluan
        self.lambung = lambung
        self.deck = deck
        self.buritan = buritan
        self.lunas_kapal = lunas_kapal
        self.kulit_kapal = kulit_kapal
        self.jangkar = jangkar
        self.kemudi = kemudi

    def simpan_data(self):
        """simpan data ke database"""
        print ('data disimpan')
        

class PerahuMotor(KapalInterface):

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, 
        kemudi, lampu_navigasi):

        KapalInterface.__init__(cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi)

        self.__lampu_navigasi = lampu_navigasi
    
    def get_properties(self):
        properties = {
            'lampu_navigasi': self.__lampu_navigasi
        }
        return properties
    
    def simpan_data(self):
        print ('data perahu motor disimpan')


class PerahuLayar(KapalInterface):
    linggi: str
    tiang_layar: str
    layar: str

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal,
                kemudi, linggi, tiang_layar, layar):

        KapalInterface.__init__(cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi)
        
        self.__linggi = linggi
        self.__tiang_layar = tiang_layar
        self.__layar = layar
    
    def get_properties(self):
        properties = {
            'linggi': self.__linggi,
            'tiang_layar': self.__tiang_layar,
            'layar': self.__layar           
        }
        return properties

    def simpan_data(self):
        print ('data perahu layar disimpan')


class KapalPesiar(KapalInterface):

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi,
                anjungan, bak, sekat_pelanggaran, lampu_navigasi, gunwales, mesin):
        
        KapalInterface.__init__(cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi)
        
        self.__anjungan = anjungan
        self.__bak = bak
        self.__sekat_pelanggaran = sekat_pelanggaran
        self.__lampu_navigasi = lampu_navigasi
        self.__gunwales = gunwales
        self.__mesin = mesin
    
    def set__anjungan(self, anjungan):
        self.__anjungan = anjungan

    def set__bak(self, bak):
        self.__bak = bak

    def set__sekat_pelanggaran(self, sekat_pelanggaran):
        self.sekat_pelanggaran = sekat_pelanggaran

    def set__lampu_navigasi(self, lampu_navigasi):
        self.__lampu_navigasi = lampu_navigasi

    def set__gunwales(self, gunwales):
        self.__gunwales = gunwales

    def set__mesin(self, mesin):
        self.__mesin = mesin
    
    def get__anjungan(self, anjungan):
        return self.__anjungan

    def get__bak(self, bak):
        return self.__bak

    def get__sekat_pelanggaran(self, sekat_pelanggaran):
        self.sekat_pelanggaran = sekat_pelanggaran

    def get__lampu_navigasi(self, lampu_navigasi):
        return self.__lampu_navigasi

    def get__gunwales(self, gunwales):
        return self.__gunwales

    def get__mesin(self, mesin):
        return self.__mesin
    
    def get_all_properties(self):
        properties = {
            'anjungan': self.__anjungan,
            'bak': self.__bak,
            'sekat_pelanggaran': self.__sekat_pelanggaran,
            'lampu_navigasi': self.__lampu_navigasi,
            'gunwales': self.__gunwales,
            'mesin': self.__mesin
        }
        return properties

    def simpan_data(self):
        print ('data Kapal Pesiar disimpan')


# perahu_motor_obj = PerahuMotor()