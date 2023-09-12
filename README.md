# Link applikasi adaptable
https://tugaspbp1.adaptable.app

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat fungsi pada views.py untuk mengambil model dan mereturn HTML
        - Mengimport fungsi render dari django.shortcuts
        - Mengimport class Item dari models
        - Mendefinisikan function dengan parameter request
        - Membuat fungsi mereturn fungsi render dengan parameter request, main.html dan context (data yang diambil)

    2. Membuat routing
        Untuk menampilkan apa yang diminta di tugas2pbpnaz.herokuapp.com/main:
        - Menambahkan path /main di main/urls.py pada array urlpatterns dan include(main.urls) -> routing ke aplikasi main
        - Mengimport show_main dari main.views di main/urls.py dan menambahkan path ''  pada array urlpatternn da passing functions show_main

    3. Memetakan data yang diambil ke HTML
        - Data yang ada di variabel context pada parameter function render dapat digunakan dalam template HTML. 
        - Di bawah nama, ditambahkan text bold <b> {{name}} </b>, dimana nama yang merupakan key di dictionary context akan mereturn value yang bersesuaian. 

    4. Melakukan deployment ke adaptable agar aplikasi dapat dilihat di internet
         - Membuat aplikasi di adaptable


# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    https://drive.google.com/file/d/1TVLLRZlJUmTPMGW8OFcG9GWs7_ygGAoe/view?usp=sharing

# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Untuk memisahkan project django dengan project yang lain, sehingga tidak terjadi overlapping.

