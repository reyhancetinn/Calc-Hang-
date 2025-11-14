import random
import math
try:
    from colorama import Fore, Style, init
    init()
    KIRMIZI = Fore.RED
    YESIL = Fore.GREEN
    MAVI = Fore.BLUE
    SARI = Fore.YELLOW
    BEYAZ = Fore.WHITE
    RESET = Style.RESET_ALL
except ImportError:
 
    class FakeColors:
        def __getattr__(self, name):
            return ''
    KIRMIZI = YESIL = MAVI = SARI = BEYAZ = RESET = ''

ASMACA_GORSELLERI = [
    """
+---+  
|    
|    
|    
==========""",
    """
+---+  
|    |  
|    
|    
==========""",
    """
+---+  
|    |  
|    O  
|    
==========""",
    """
+---+  
|    |  
|    O  
|    |  
==========""",
    """
+---+  
|    |  
|    O  
|   /|  
==========""",
    """
+---+  
|    |  
|    O  
|   /|\\ 
==========""",
    """
+---+  
|    |  
|    O  
|   /|\\ 
|   /  
==========""",
    """
+---+  
|    |  
|    O  
|   /|\\ 
|   / \\ 
=========="""
]

KELIMELER = {
    "meyveler": ["elma", "armut", "cilek", "muz", "portakal", "mandalina", "kiraz", "karpuz"],
    "hayvanlar": ["kedi", "kopek", "aslan", "kaplan", "zurafa", "timsah", "penguen", "yunus"],
    "teknoloji": ["bilgisayar", "klavye", "fare", "monitor", "yazici", "tarayici", "tablet", "telefon"]
}

class CalcHangOyunu:
    def __init__(self):  
        self.kelime = ""
        self.kategori = ""
        self.tahmin_edilen_harfler = []
        self.acilan_harfler = []
        self.hata_sayisi = 0
        self.bonus_puan = 0
        self.toplam_puan = 0
        self.oyun_devam = True

    def kelime_sec(self):
        self.kategori = random.choice(list(KELIMELER.keys()))
        self.kelime = random.choice(KELIMELER[self.kategori])
        self.acilan_harfler = ["_"] * len(self.kelime)
        self.tahmin_edilen_harfler = []
        self.hata_sayisi = 0
        self.bonus_puan = 0
        self.toplam_puan = 0

    def ekrani_goster(self):
        print(f"\n{MAVI}=== Calc & Hang: Islem Yap, Harfi Kurtar! ==={RESET}")
        print(f"\n{BEYAZ}--- Yeni Tur ---{RESET}")
        print(f"{SARI}{ASMACA_GORSELLERI[self.hata_sayisi]}{RESET}")

        kelime_gosterim = " ".join(self.acilan_harfler)
        print(f"\n{BEYAZ}Kelime: {kelime_gosterim}{RESET}")

        tahmin_edilen = ", ".join(self.tahmin_edilen_harfler) if self.tahmin_edilen_harfler else "-"
        print(f"{BEYAZ}Tahmin edilen harfler: {tahmin_edilen}{RESET}")
        print(f"{BEYAZ}Bonus puan: {self.bonus_puan}{RESET}")
        print(f"{BEYAZ}Toplam puan: {self.toplam_puan}{RESET}")

    def secenekleri_goster(self):
        print(f"{BEYAZ}Secenekler: [H]arf tahmini | [I]slem coz | [P]ucu | [Q] cikis{RESET}")
        secim = input(f"{BEYAZ}Seciminiz: {RESET}").lower().strip()
        return secim

    def harf_tahmini(self):
        harf = input(f"{BEYAZ}Harf: {RESET}").lower().strip()

        if len(harf) != 1 or not harf.isalpha():
            print(f"{KIRMIZI}Gecersiz giris! Sadece bir harf girin.{RESET}")
            return

        if harf in self.tahmin_edilen_harfler:
            print(f"{SARI}Bu harfi zaten tahmin ettiniz!{RESET}")
            return

        self.tahmin_edilen_harfler.append(harf)

        if harf in self.kelime:
            for i, h in enumerate(self.kelime):
                if h == harf:
                    self.acilan_harfler[i] = harf
            self.toplam_puan += 10
            print(f"{YESIL}Dogru harf!{RESET}")
        else:
            self.hata_sayisi += 1
            self.toplam_puan = max(0, self.toplam_puan - 5)   
            print(f"{KIRMIZI}Yanlis harf: {harf} | kalan hata hakki: {7 - self.hata_sayisi}{RESET}")

    def islem_coz(self):
        islem_turu = input(f"{BEYAZ}Islem turu (toplama/cikarma/carpma/bolme) ya da 'iptal': {RESET}").lower().strip()

        if islem_turu == 'iptal':
            print(f"{SARI}Islem iptal edildi.{RESET}")
            return

        if islem_turu not in ['toplama', 'cikarma', 'carpma', 'bolme']:
            print(f"{KIRMIZI}Gecersiz islem turu!{RESET}")
            return

        try:
            sayi1 = input(f"{BEYAZ}1. sayi (iptal icin 'iptal'): {RESET}").strip()
            if sayi1 == 'iptal':
                print(f"{SARI}Islem iptal edildi.{RESET}")
                return
            sayi1 = float(sayi1)

            sayi2 = input(f"{BEYAZ}2. sayi (iptal icin 'iptal'): {RESET}").strip()
            if sayi2 == 'iptal':
                print(f"{SARI}Islem iptal edildi.{RESET}")
                return
            sayi2 = float(sayi2)
        except ValueError:
            print(f"{KIRMIZI}Gecersiz sayi!{RESET}")
            return

        if islem_turu == 'toplama':
            dogru_cevap = sayi1 + sayi2
            islem_metin = f"{sayi1} + {sayi2}"
        elif islem_turu == 'cikarma':
            dogru_cevap = sayi1 - sayi2
            islem_metin = f"{sayi1} - {sayi2}"
        elif islem_turu == 'carpma':
            dogru_cevap = sayi1 * sayi2
            islem_metin = f"{sayi1} × {sayi2}"
        elif islem_turu == 'bolme':
            if sayi2 == 0:
                print(f"{KIRMIZI}Bolen sifir olamaz! Hata sayisi artti.{RESET}")
                self.hata_sayisi += 1
                self.toplam_puan = max(0, self.toplam_puan - 10)
                return
            dogru_cevap = sayi1 / sayi2
            islem_metin = f"{sayi1} ÷ {sayi2}"

        try:
            cevap = float(input(f"{BEYAZ}Soru: {islem_metin} = ?\nCevabiniz: {RESET}"))
        except ValueError:
            print(f"{KIRMIZI}Gecersiz cevap! Hata sayisi artti.{RESET}")
            self.hata_sayisi += 1
            self.toplam_puan = max(0, self.toplam_puan - 10)
            return

 
        if math.isclose(cevap, dogru_cevap, abs_tol=1e-6):
            print(f"{YESIL}Dogru!{RESET}")
            self.bonus_puan += 1
            self.toplam_puan += 15

            acilacak_harfler = [i for i, h in enumerate(self.kelime) if self.acilan_harfler[i] == "_"]
            if acilacak_harfler:
                rastgele_index = random.choice(acilacak_harfler)
                acilan_harf = self.kelime[rastgele_index]
                self.acilan_harfler[rastgele_index] = acilan_harf
                print(f"{YESIL}Bonus: '{acilan_harf}' harfi acildi!{RESET}")

            print(f"{YESIL}Bonus puanin: {self.bonus_puan}{RESET}")
        else:
            print(f"{KIRMIZI}Yanlis! Dogru cevap: {dogru_cevap:.2f}{RESET}")
            self.hata_sayisi += 1
            self.toplam_puan = max(0, self.toplam_puan - 10)

    def ipucu_al(self):
        if self.bonus_puan < 1:
            print(f"{KIRMIZI}Yeterli bonus puaniniz yok!{RESET}")
            return

        self.bonus_puan -= 1
        self.toplam_puan = max(0, self.toplam_puan - 1)
        print(f"{MAVI}Ipucu: Kategori - {self.kategori}{RESET}")
        print(f"{MAVI}Kalan bonus puan: {self.bonus_puan}{RESET}")

    def oyun_kontrol(self):
        if "_" not in self.acilan_harfler:
            self.toplam_puan += 50
            print(f"\n{YESIL}=== Tebrikler! Kelime: {self.kelime} ==={RESET}")
            print(f"{YESIL}Toplam puan: {self.toplam_puan}{RESET}")
            return True

        if self.hata_sayisi >= 7:
            print(f"\n{KIRMIZI}=== Kaybettiniz! Dogru kelime: {self.kelime} ==={RESET}")
            print(f"{KIRMIZI}Toplam puan: {self.toplam_puan}{RESET}")
            return True

        return False

    def oyunu_baslat(self):
        self.kelime_sec()

        while self.oyun_devam:
            self.ekrani_goster()
            secim = self.secenekleri_goster()

 
            if secim in ['h', 'harf', '1']:
                self.harf_tahmini()
            elif secim in ['i', 'islem', '2']:   
                self.islem_coz()
            elif secim in ['p', 'pucu', 'ipucu', 'ip', '3']:
                self.ipucu_al()
            elif secim in ['q', 'cikis', 'c', '4']:
                print(f"{SARI}Oyun sonlandirildi.{RESET}")
                break
            else:
                print(f"{KIRMIZI}Gecersiz secenek! Lutfen H, I, P veya Q girin.{RESET}")
                continue

            if self.oyun_kontrol():
                self.oyun_devam = False


if __name__ == "__main__":  
    oyun = CalcHangOyunu()
    oyun.oyunu_baslat()
