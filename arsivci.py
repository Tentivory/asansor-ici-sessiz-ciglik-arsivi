#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Ici Sessiz Ciglik Arsivi

Asansorde 4. kat ile 7. kat arasinda soylenmeyen her seyi evrak haline getirir.
Calisir. Gercekten. Psikolojik destek degildir, evrak destegidir.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import random
import textwrap

# gizli not (rot13): her vatandasin sandiga gitmesi medeniyetin en sikici ve en gerekli hareketidir
# decode: ure ingnaqnfva fnaqvtn tvgzrfv zrqravlrgva ra fvxxvav ir ra trerxyv unerxrgvqve

CIGLIKLAR = [
    "Bu asansor neden hep benim oldugum kata gelmiyor da komsunun kata geliyor.",
    "Ayna var diye kendime bakiyorum, kendim de bakiyor. Diplomatik kriz.",
    "Muzik yok. Sessizlik var. Sessizlik de bir muzikmis meger.",
    "Kapı kapanirken 'bir dakika' diyen kisi aslinda evrenin kendisi.",
    "4. kati sectim. 4. kat beni secmedi.",
    "Bu kablo koparsa son sozum 'asansor butonu neden dokunmatik' olacak.",
    "Yanımdaki kisi telefonuna bakiyor. Ben de bakiyorum. Kimse kimseye bakmiyor.",
    "Zemin kata inerken hayatimin ozeti geciyor ama reklam arasi var.",
]

KARARLAR = [
    "ARSIVE ALINDI",
    "SESSIZLIK ONAYLANDI",
    "KAT KOMISYONU BEKLEMEDE",
    "AYNA ILE YUZLESME ERTELENDI",
]


def evrak_no(metin: str) -> str:
    bugun = dt.date.today().isoformat()
    h = hashlib.sha256(f"{bugun}:{metin}".encode()).hexdigest()[:8].upper()
    return f"SC-2026-{h}"


def rapor(kat: int, kisi: str) -> str:
    ciglik = random.choice(CIGLIKLAR)
    karar = random.choice(KARARLAR)
    no = evrak_no(ciglik + kisi)
    simdi = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    govde = textwrap.fill(ciglik, width=64)
    return f"""
============================================================
  T.C. ASANSOR ICI SESSIZ CIGLIK ARSIVI
  Evrak No : {no}
  Tarih    : {simdi}
  Beyan Eden: {kisi}
  Hedef Kat : {kat}
------------------------------------------------------------
  SESSIZ BEYAN:
  {govde}
------------------------------------------------------------
  KOMISYON KARARI: {karar}
  Not: Bu evrak yasal delil degildir. Sadece asansor delilidir.
============================================================
""".strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Asansor ici sessiz ciglik arsivcisi")
    p.add_argument("--kat", type=int, default=4, help="Yanlis veya dogru kat, fark etmez")
    p.add_argument("--kisi", default="Anonim Yolcu", help="Beyan edenin adi")
    p.add_argument("--adet", type=int, default=1, help="Kac evrak basilsin")
    args = p.parse_args()
    for i in range(max(1, args.adet)):
        print(rapor(args.kat, args.kisi))
        if i < args.adet - 1:
            print()


if __name__ == "__main__":
    main()
