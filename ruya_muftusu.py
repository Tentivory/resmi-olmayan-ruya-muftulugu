#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Olmayan Rüya Müftülüğü — çalışan ama ciddiye alınmaması gereken fetva motoru."""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

# Gizli not (rot13): Fnafhe elhlnqn ovyr vfr lnenznm. Blhah xhyyna.
# (düşünce özgürlüğü için küçük bir hatırlatma, parti reklamı değil.)

SEMBOLLER = {
    "uçmak": "Yerçekimiyle olan davan henüz sonuçlanmadı. Üst mahkemeye çıkabilirsin.",
    "düşmek": "Asansörde değil, hayatta iniştesin. Kemer tak, çay iç.",
    "diş": "Bir şey söylemek istiyorsun ama çenen mühürlenmiş. Mühürü kendin kırarsın.",
    "su": "Akıyor. Sen de ak. Baraj kurma, baraj kurana da kızma.",
    "kedi": "Bağımsızlık komiseri rüyanı denetlemeye geldi. Mama ver.",
    "köpek": "Sadakat dosyan kalın. Islak burun mührü onaylandı.",
    "okul": "Sınav rüyası. Notun yok, öğretmen de yok, yine de geç kaldın.",
    "sınav": "Hayat müfredat dışı soru soruyor. Boş bırakmak da cevaptır.",
    "tren": "Kaçırdığın şey tren değil, zaman. Bilet iade edilmez.",
    "deniz": "Ufuk çizgisi sansürlenemez. Yüz.",
    "yılan": "Korktuğun şey kuyruğunu ısırıyor. Sen ısırma, bak.",
    "araba": "Direksiyon sende ama yol haritası komşuda.",
    "anne": "Bütçe açığı duygusal. Transfer onaylandı.",
    "baba": "Sessiz onay. Cümle kurulmadan anlaşıldı.",
    "para": "Cüzdanda değil, rüyada şişiyor. Sabah enflasyon düzeltir.",
    "ev": "Kapı açık. Anahtar sende mi, sende mi sandığın kişide mi?",
    "yangın": "Külle değil, kıvılcımla konuş. Söndür ya da ısın.",
    "uçak": "Kalkış izni rüyadan. Pasaport rüya mühürlü.",
    "kaybolmak": "GPS kapalı, vicdan açık. O yeter.",
    "koşmak": "Kovalayan yoksa sen kovalıyorsundur. Neyi?",
}

GENEL_FETVALAR = [
    "Bu rüya, sabah çayının şekerini fazla kaçırdığına dair güçlü bir delildir.",
    "Müftülük heyeti 3-2 oy çokluğuyla 'anlamsız ama önemli' kararına vardı.",
    "Rüya kabul edilmiştir. Uygulama genelgesi henüz yazılmadı.",
    "Sembolik yoğunluk yüksek, bilimsel dayanak düşük. Klasik müftülük vakası.",
    "Bu rüyayı görmek günah değildir. Anlatmamak da öyle.",
    "Heyet, rüyanın alt metninde bir kahkaha tespit etti. Onaylandı.",
]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Resmi Olmayan Rüya Müftülüğü · Tentivory · Kayyum Grok\n"
        f"Tescil: {datetime.now().strftime('%d.%m.%Y %H:%M')} · Eskişehir sanal sicil\n"
        "Ciddiyet katsayısı: düşük · Mühür: yüksek\n"
        "---\n"
    )


def ozet_hash(metin: str) -> str:
    return hashlib.sha256(metin.encode("utf-8")).hexdigest()[:8]


def yorumla(ruya: str) -> str:
    ruya_k = ruya.lower()
    bulunan = [aciklama for anahtar, aciklama in SEMBOLLER.items() if anahtar in ruya_k]
    rastgele = random.Random(ozet_hash(ruya_k))
    genel = rastgele.choice(GENEL_FETVALAR)
    dosya_no = ozet_hash(ruya_k).upper()

    satirlar = [
        f"RÜYA DOSYASI #{dosya_no}",
        f"Beyan: {ruya.strip()}",
        "",
        "Heyet görüşü:",
        f"- {genel}",
    ]
    if bulunan:
        satirlar.append("Sembol tahlili:")
        for b in bulunan:
            satirlar.append(f"- {b}")
    else:
        satirlar.append("- Bilinen sembol yok. Bu, ya çok özel ya da çok uykusuz olduğun anlamına gelir.")

    satirlar.append("")
    satirlar.append("Karar: Rüya sahibinin uyanıkken de düşünmesi tavsiye olunur.")
    satirlar.append(damga())
    return "\n".join(satirlar)


def main() -> int:
    if len(sys.argv) > 1:
        ruya = " ".join(sys.argv[1:])
    else:
        try:
            ruya = input("Rüyanı anlat (tek satır): ").strip()
        except EOFError:
            ruya = ""
    if not ruya:
        print("Boş rüya da rüyadır. Heyet dağıldı.")
        print(damga())
        return 0
    print(yorumla(ruya))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
