def konversi_suhu(suhu, dari, ke):
    def to_celsius(s, v):
        if s == "C": return v
        if s == "R": return v * 5/4
        if s == "F": return (v - 32) * 5/9
        if s == "K": return v - 273.15

    def from_celsius(s, v):
        if s == "C": return v
        if s == "R": return v * 4/5
        if s == "F": return v * 9/5 + 32
        if s == "K": return v + 273.15

    satuan = {"C", "R", "F", "K"}
    if dari not in satuan or ke not in satuan:
        return "Satuan tidak dikenali"
    c = to_celsius(dari, suhu)
    return from_celsius(ke, c)
