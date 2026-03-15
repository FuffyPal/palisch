import pytest
from src.converter import convert_text

def test_convert_r():
    assert convert_text("R") == "W"
    assert convert_text("r") == "w"
    assert convert_text("River") == "Wivew"

def test_convert_s_sh():
    assert convert_text("S") == "Sch"
    assert convert_text("s") == "sch"
    assert convert_text("Ş") == "Sch"
    assert convert_text("ş") == "sch"
    assert convert_text("Şeker") == "Scheqew"

def test_convert_z():
    assert convert_text("Z") == "Tz"
    assert convert_text("z") == "tz"
    assert convert_text("Zebra") == "Tzebwa"

def test_convert_k():
    assert convert_text("K") == "Q"
    assert convert_text("k") == "q"
    assert convert_text("Kedi") == "Qedi"

def test_convert_g():
    assert convert_text("G") == "C"
    assert convert_text("g") == "c"
    assert convert_text("Gül") == "Cüly"

def test_convert_l():
    assert convert_text("L") == "Ly"
    assert convert_text("l") == "ly"
    assert convert_text("Lale") == "Lyalye"

def test_no_conversion():
    assert convert_text("ABC") == "ABC"
    assert convert_text("123") == "123"
    assert convert_text("") == ""

def test_full_sentence():
    # R -> W, S/Ş -> Sch, Z -> tz, K -> Q, G -> C, L -> Ly
    input_text = "Rıza Şekerci Gelirken Leblebi Getirdi"
    # Rıza -> Wıtza (R->W, z->tz)
    # Şekerci -> Scheqewci (Ş->Sch, k->q, r->w)
    # Gelirken -> Celyiwqen (G->C, l->ly, r->w, k->q)
    # Leblebi -> Lyeblyebi (L->Ly, l->ly)
    # Getirdi -> Cetiwdi (G->C, r->w)
    expected = "Wıtza Scheqewci Celyiwqen Lyeblyebi Cetiwdi"
    assert convert_text(input_text) == expected
