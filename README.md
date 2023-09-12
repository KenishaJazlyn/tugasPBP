# Link aplikasi adaptable
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

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola desain arsitektur yang sering digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi berbasis web dan aplikasi berbasis antarmuka pengguna (UI). 
--Pengertian Model & View--
    Model: 
        Bertanggung jawab untuk mengelola data dan bisnis logic aplikasi. Ini adalah bagian yang merepresentasikan struktur data dan aturan aplikasi.
    View:
        Bertanggung jawab untuk menampilkan data kepada pengguna dan mengatur antarmuka pengguna. Ini adalah bagian yang mengatur tampilan dan tata letak elemen-elemen UI.
 
    1. MVC (Model-View-Controller):
        Controller:
        Bertanggung jawab untuk mengatur interaksi antara Model dan View. Ini menerima input dari pengguna, memprosesnya, dan mengirimkan perintah ke Model atau View yang sesuai.

    2. MVT (Model-View-Template):
        Template: 
        Template adalah lapisan yang bertanggung jawab untuk mengatur tampilan antarmuka pengguna dalam MVT. Template merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view.

    3. MVVM (Model-View-ViewModel):
        ViewModel: Lapisan baru yang memisahkan presentasi dan logika tampilan dari View. ViewModel menghubungkan Model dengan View dan mengelola state serta operasi yang berkaitan dengan tampilan.

    -- Perbedaan --
    MVC = Terdapat pemisahan antara Model, View, dan Controller yang jelas. Ini memungkinkan perubahan dalam satu bagian untuk tidak    mempengaruhi secara langsung bagian lainnya.
    MVT = MVT biasanya digunakan dalam kerangka kerja (framework) web seperti Django, yang memiliki lapisan Template tambahan untuk mengelola tampilan dinamis. Ini membuat MVT mirip dengan MVC, namun dengan pendekatan berbeda dalam mengatur tampilan.
    MVVM = MVVM dirancang khusus untuk pengembangan aplikasi antarmuka pengguna (UI) yang dinamis, seperti aplikasi berbasis Xamarin atau Angular. Ini memberikan pemisahan yang jelas antara logika tampilan (ViewModel) dan tampilan (View).
   