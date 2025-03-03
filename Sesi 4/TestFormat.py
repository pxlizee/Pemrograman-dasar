hello_template = "halo, nama saya %s , saya berusia %d tahun, dan saya tinggal di %s"
print(hello_template % ("ikbal hensem", 20, "Jakarta"))

template_2 = "halo, nama saya {nama}, saya berusia {umur} tahun, dan saya tinggal di {alamat}"
print(template_2.format(nama="ikbal hensem", umur=20, alamat="cianjur"))


