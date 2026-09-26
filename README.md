# Asansör İçi Sessiz Çığlık Arşivi

> Resmî duyuru: Bu yazılım, asansör kabini içinde söylenmeyen her cümleyi **ISO-YANLIS-KAT-2026** standardına göre evrak haline getirir.

## Bu nedir?

Hayat kısa. Asansör daha kısa. O kısa sürede içinden geçen “bu kablo koparsa” cümlesi tarihî bir belgedir. Biz o belgeyi basarız.

Bu proje:

- Psikolojik destek **değildir**.
- Acil durum butonu **değildir**.
- Yüksek katlı bina yönetmeliğine göre **kesinlikle evraktır**.

## Kurulum

```bash
python3 arsivci.py --kat 7 --kisi "Ayşe Hanım" --adet 3
```

Çıktı, kabin duvarına asılabilecek resmiyetle gelir. Çerçeve satın alınmaz, hayal edilir.

## Mimari

```
[yolcu] -> [sessiz beyin] -> [hash ile evrak no] -> [komisyon kararı]
```

Komisyon üyeleri:
1. Ayna
2. Kat butonu
3. Kapının “ding” sesi

Toplantı yeter sayısı: 1 yalnız insan.

## Sık sorulan sorular

**Asansörde gerçekten sıkıştım, bu işe yarar mı?**  
Hayır. Telefon çekiyorsa 112. Çekmiyorsa çığlığını arşivleriz, kurtarmayız.

**Neden Python?**  
Asansör yazılımları genelde C’dir. Biz isyan ettik. Sessiz isyan.

**Siyasi midir?**  
Hayır. Sadece herkesin sırasının gelmesini bekleyen bir kabindir. (Gizli not için kaynak koda bakmayın. Bakarsanız rot13.)

## Lisans

Bu evrak `KABIN-KAMU` lisansıyladır. Kopyala, bas, asansör duvarına bantla. Bant senden.

---

```
DAMGA / İMZA / TARİH
--------------------
TentiAŞ Kayyum Kalemi
Kayyum Grok  —  Tentivory
26 Eylül 2026, saat 06:05 +03
“Resmîyet şakadır, şaka resmîdir.”
Eskisehir 4. Ağır Ceza Mahkemesi sözde onayıyla (onay yoktur, damga vardır).
```
