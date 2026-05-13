def eng_ko_p_takrorlangan_harf(satr):
    harflar = {}
    for harf in satr:
        if harf in harflar:
            harflar[harf] += 1
        else:
            harflar[harf] = 1
    return max(harflar, key=harflar.get)
```

```python
def eng_ko_p_takrorlangan_harf(satr):
    harflar = {}
    for harf in satr:
        harflar[harf] = harflar.get(harf, 0) + 1
    return max(harflar, key=harflar.get)
```

```python
def eng_ko_p_takrorlangan_harf(satr):
    harflar = {}
    for harf in satr:
        harflar[harf] = harflar.get(harf, 0) + 1
    return max(harflar, key=harflar.get)
