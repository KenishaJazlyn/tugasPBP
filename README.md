# Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
  Django UserCreationForm adalah salah satu bentuk formulir (form) bawaan yang disediakan oleh Django. Form ini digunakan untuk membuat formulir pendaftaran atau registrasi pengguna pada aplikasi web yang dibangun menggunakan Django. UserCreationForm mengambil alih sebagian besar pekerjaan yang diperlukan untuk membuat dan mengelola pengguna dalam sistem Django.
  
  Kelebihan
  - Mudah digunakan
  - Memiliki validasi otomatis untuk memeriksa input user sesuai dengan persyratan yang diinginkan
  - Customizable
  - Dokumentasi yang baik 

  Kekurangan
  - Kurang fleksibel
  - Tampilan cukup standar, sehingga untuk mengubah tampilan butuh kode tambahan
  - Tidak memuat fitur-fitur lanjutan, seperti two-factor authentication, pendaftaran menggunakan email dan lain lain
#  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi
    proses verifikasi indentitas pengguna, dalam django autentikasi melibatkan hal hal berikut :
    - Memvalidasi pengguna berdasarkan kombinasi nama pengguna (username) dan kata sandi (password).
    - Memeriksa apakah pengguna telah berhasil masuk (authenticated) atau belum.
    - Menyediakan mekanisme untuk login dan logout pengguna.
    - Menangani fitur-fitur seperti reset kata sandi.

    Otorisasi
    Proses yang terjadi setelah autentikasi. Otorisasi berhubungan dengan mengontrol akses pengguna terhadap berbagai bagian dan fitur aplikasi
    
    Keduanya penting karena autentikasi dan otorisasi bersama-sama menjaga keamanan aplikasi dengan memastikan bahwa pengguna hanya dapat mengakses dan melakukan tindakan yang sesuai dengan peran dan izin mereka.

#  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Cookies adalah potongan kecil data yang disimpan di sisi client. Django, cookies sering digunakan untuk mengelola data sesi pengguna. Sesuatu yang disebut "session cookies" atau "session data" digunakan untuk menyimpan informasi khusus tentang sesi pengguna saat mereka berinteraksi dengan aplikasi web. Ini dapat mencakup informasi seperti:

# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
  Penggunaan cookies harus diwaspadai, ada beberapa risiko potensial seperti Cross-Site Scripting, Session Hijacking, Cookie Poisoning, Cookie Theft dan Tracking. 

#  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  - Membuat fungsi register, login_user, dan logout_user
  - Membuat file register.html dan login.html sebagai tampilan register dan login user
  - Membuat routing ke register.html dan login.html
  - Merestriksi akses halaman main agar halaman main dapat diakses setelah login

 ---------------------------------------------------------------------------
# Apa perbedaan antara form POST dan form GET dalam Django?
  - GET kurang aman dibanding POST karena data yang di kirim terlihat di URL, sedangkan POST lebih aman karena parameternya tidak disimpan pada history browser atau web server logs. 
  - POST mengolah data dalam jumlah yang lebih besar dibanding GET
# Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
  XML dan JSON digunakan untuk menyimpan dan mentransfer data dari server, HTML digunakan untuk membuat halaman web dan menampilkan konten di web browser. 
  XML  = menggunakan tag untuk mengidentifikasi elemen data, tidak memiliki aturan baku mengenai struktur data, lebih sulit untuk dibaca, support berbagai encoding
  JSON = menggunakan key dan value, mudah dibaca oleh manusia, mendukung struktur data string, support UTF-8 encoding 

# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
  - memiliki ukuran data yang lebih kecil sehingga membuat data transmission lebih cepat
  - lebih aman dibanding XML
  - lebih mudah dibaca oleh manusia
  - mendukung banyak bahasa pemrograman
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - membuat base.html sebagai template
   - membuat forms.py untuk menerima data produk baru
   - membuat fungsi add_product untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data disubmit
   - membuat create_product.html 
   - mengupdate main.html dengan menambahkan tabel yang berisi data yang dimport pada form
   - membuat fungsi show_xml, shos_json, show_xml_by_id, show_json_by_id, pada views.py dan membuat routing kepada masing-masing

HTML

<img width="669" alt="image" src="https://github.com/KenishaJazlyn/tugasPBP/assets/124899946/e3da67b3-bff6-4950-b7d0-f88e9e14c329">

XML

<img width="669" alt="image" src="https://github.com/KenishaJazlyn/tugasPBP/assets/124899946/7b72dc2c-61f6-45ee-9eaf-c1d3259603d7">

JSON

<img width="662" alt="image" src="https://github.com/KenishaJazlyn/tugasPBP/assets/124899946/1d675b9c-8682-443f-a338-32a2fb03e83b">

XML by ID

<img width="670" alt="image" src="https://github.com/KenishaJazlyn/tugasPBP/assets/124899946/1e8cd60d-fdaf-499f-ad2a-a405e7f3e246">

JSON by ID

<img width="668" alt="image" src="https://github.com/KenishaJazlyn/tugasPBP/assets/124899946/439745d9-1e52-46e5-9072-9585244b7244">



     
----------------------------------------------------------------------------
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
   
