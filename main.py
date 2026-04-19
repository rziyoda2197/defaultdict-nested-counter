from collections import defaultdict

def harf_chastotasi(matn):
    harf_chastotasi = defaultdict(int)
    for harf in matn.lower():
        harf_chastotasi[harf] += 1
    return harf_chastotasi

matn = "Bu matn uchun harf chastotasi hisoblanadi."
print(harf_chastotasi(matn))
```

```python
from collections import defaultdict

def harf_chastotasi(matn):
    harf_chastotasi = defaultdict(int)
    for harf in matn.lower():
        harf_chastotasi[harf] += 1
    return harf_chastotasi

matn = "Bu matn uchun harf chastotasi hisoblanadi."
print(harf_chastotasi(matn))
