
from abc import ABC, abstractmethod

class KapalAbstract(ABC):
    
    @property
    @abstractmethod
    def kapal_property(self):
        pass
    
    @abstractmethod
    def simpan_data(self):
        pass

class Kapal(KapalAbstract):

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi):
        self.__cleats = cleats
        self.__haluan = haluan
        self.__lambung = lambung
        self.__deck = deck
        self.__buritan = buritan
        self.__lunas_kapal = lunas_kapal
        self.__kulit_kapal = kulit_kapal
        self.__jangkar = jangkar
        self.__kemudi = kemudi

    def simpan_data(self):
        """simpan data ke database"""
        print ('data disimpan')
        

class PerahuMotor(Kapal):

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi, lampu_navigasi):

        Kapal.__init__(cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi)

        self.__lampu_navigasi = lampu_navigasi
    
    def get_properties(self):
        properties = {
            'lampu_navigasi': self.__lampu_navigasi
        }
        return properties
    
    def simpan_data(self):
        print ('data perahu motor disimpan')


class PerahuLayar(Kapal):
    linggi: str
    tiang_layar: str
    layar: str

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi, linggi, tiang_layar, layar):

        Kapal.__init__(cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi)
        
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


class KapalPesiar(Kapal):

    def __init__(self, cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi, anjungan, bak, sekat_pelanggaran, lampu_navigasi, gunwales, mesin):
        
        Kapal.__init__(cleats, haluan, jangkar, lambung, deck, buritan, lunas_kapal, kulit_kapal, kemudi)
        
        self.__anjungan = anjungan
        self.__bak = bak
        self.__sekat_pelanggaran = sekat_pelanggaran
        self.__lampu_navigasi = lampu_navigasi
        self.__gunwales = gunwales
        self.__mesin = mesin
    
    def get_properties(self):
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