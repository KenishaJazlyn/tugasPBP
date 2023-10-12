<details>
<summary><b> WEEK 06</b> </summary>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
   Asynchronous programming adalah approach programming yang tidak terikat pada protocol I/O. Secara singkatnya, asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain, sehingga proses dapat berjalan secara independent. Sementara itu, pada synchronous programming sebuah proses yang berjalan akan ditunggu sampai selesai tereksekusi sebelum berpindah ke proses selanjutnya.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    Event-driven programming adalah sebuah paradigma dimana sebuah alur program ditentukan oleh sebuah event (seperti klik pada mouse, press pada keyboard, dsb).
    Salah satu contoh event-driven programming pada program ini adalah ketika press button Add Item di modal, menggunakan attribute onclick untuk getElementbyID. 

##  Jelaskan penerapan asynchronous programming pada AJAX.
    Asynchronous programming pada AJAX membuat halaman web dapat diperbaharui secara asynchronous tanpa harus mereload seluruh halaman dengan transfer data ke server di balik layar. Ketika sebuah event terjadi di browser, maka objek XMLHttpRequest akan dibuat dan mengirimkan HttpRequest ke server lewat internet. Server kemudian memproses HTTPRequest, membuat sebuah respons dan mengirimkan data kembali ke browser lewat internet. Kemudian, browser akan memproses data yang dikirimkan menggunakan JavaScript dan memperbaharui halaman. 

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    Fetch API tidak memiliki fitur dan fungsionalitas yang banyak seperti jQuery, sehingga ukuran file lebih kecil. 
    jQuery dirancang untuk bekerja di bekerja di berbagai peramban web, sehingga jQuery dapat mengatasi perbedaan peramban dengan baik

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Menambahkan fungsi get_product_json dan add_product_ajax pada views.py
    - Melakukan routing untuk fungsi tersebut di urls.py
    - Menambahkan fungsi-fungsi JavaScript seperti getProducts() untuk mengambil semua data server, refreshProduct() untuk 
    - Menampilkan data menggunakan AJAX, dan addProduct() untuk menambahkan data dengan AJAX
    - Membuat modal yang digunakan untuk menambahkan item menggunakan AJAX
    - Menambahkan tombol Add Item
</details>


<details>
  <summary><b> WEEK 05</b> </summary>

  ## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
      Elemen selector -> tag HTML sebagai selector diakses dengan nama elemen 
      Cocok digunakan saat Anda ingin mengaplikasikan gaya atau perilaku yang sama pada semua elemen dengan tipe yang sama suatu halaman. 
      Contohnya adalah mengubah gaya teks pada semua paragraf (<p>) menjadi warna biru.
      
      Id selector -> menambahkan id di tag html, dan diakses dengan ##
      Digunakan ketika Anda ingin memberikan gaya atau perilaku yang unik pada elemen tertentu di halaman. Misalnya, mengubah latar belakang header dengan ID "header."

      Class selector -> menambahkan class di tag html, dan diakses dengan . 
      Cocok digunakan ketika Anda ingin memberikan gaya atau perilaku yang serupa pada beberapa elemen di halaman yang tidak harus unik. Contohnya adalah memberi elemen dengan class "button" latar belakang berwarna biru.


  ## Jelaskan HTML5 Tag yang kamu ketahui.
    <a> -> hyperlink
    <article> -> article
    <body> -> body of the document
    <footer> -> footer section
    <form> -> form for user input

  ## Jelaskan perbedaan antara margin dan padding.
      Margin:
      Margin adalah jarak di sekitar elemen HTML, yang berarti ruang antara elemen tersebut dan elemen-elemen lain di sekitarnya.
      Margin tidak memiliki latar belakang atau warna, mereka hanya mengontrol jarak antara elemen dan elemen lain di sekitarnya.
      Margin dapat digunakan untuk mengatur jarak antara elemen-elemen secara horizontal maupun vertikal.
      Margin dapat digunakan untuk mengendalikan tata letak keseluruhan elemen dan memberikan ruang di sekitarnya.
      Padding:
      Padding adalah jarak di sekitar konten elemen HTML, yang berarti ruang antara batas elemen dan kontennya sendiri.
      Padding dapat memiliki latar belakang atau warna yang berbeda dari elemen itu sendiri, sehingga memungkinkan untuk menciptakan efek visual yang berbeda.
      Padding digunakan untuk mengendalikan tata letak konten dalam elemen, seperti teks atau gambar di dalam elemen.
      Padding tidak memengaruhi jarak antara elemen dan elemen lain di sekitarnya; itu hanya memengaruhi jarak antara konten dan batas elemen itu sendiri.

  ## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
      - Bootstrap memiliki desain yang lebih berorientasi pada komponen. Tailwind adalah framework yang lebih berorientasi pada utility. Tailwind CSS adalah framework yang berorientasi pada utility. Tailwind memberikan sejumlah besar class CSS yang dapat ditambahkan langsung ke elemen HTML Anda untuk mengendalikan tampilan.
      - Bootstrap memiliki berbagai komponen dan gaya yang telah ditentukan, yang membuatnya memiliki ukuran yang lebih besar dalam hal berkas CSS.Tailwind lebih ringan dalam ukuran karena Anda hanya menggunakan class yang Anda butuhkan. Ini dapat membantu mengoptimalkan kinerja situs web Anda dengan lebih baik.
      - 

  ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
      1. Kustomisasi template HTML pada Tugas 4
        - Halaman login, register, create task
        - Menambahkan navbar, memberi warna pada page dengan CSS, dan  menggunakan elemen-elemen dari bootstrap
        - Todolist dengan cards
        - Menggunakan cards dari bootstrap di dalam for loop yang mengiterasi todolist
      2. Responsive
        - Menggunakan media query dan mengatur width untuk layar tertentu

  </details>

<details>
<summary><b> WEEK 04</b> </summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
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
##  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi
    proses verifikasi indentitas pengguna, dalam django autentikasi melibatkan hal hal berikut :
    - Memvalidasi pengguna berdasarkan kombinasi nama pengguna (username) dan kata sandi (password).
    - Memeriksa apakah pengguna telah berhasil masuk (authenticated) atau belum.
    - Menyediakan mekanisme untuk login dan logout pengguna.
    - Menangani fitur-fitur seperti reset kata sandi.

    Otorisasi
    Proses yang terjadi setelah autentikasi. Otorisasi berhubungan dengan mengontrol akses pengguna terhadap berbagai bagian dan fitur aplikasi
    
    Keduanya penting karena autentikasi dan otorisasi bersama-sama menjaga keamanan aplikasi dengan memastikan bahwa pengguna hanya dapat mengakses dan melakukan tindakan yang sesuai dengan peran dan izin mereka.

##  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Cookies adalah potongan kecil data yang disimpan di sisi client. Django, cookies sering digunakan untuk mengelola data sesi pengguna. Sesuatu yang disebut "session cookies" atau "session data" digunakan untuk menyimpan informasi khusus tentang sesi pengguna saat mereka berinteraksi dengan aplikasi web. Ini dapat mencakup informasi seperti:

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
  Penggunaan cookies harus diwaspadai, ada beberapa risiko potensial seperti Cross-Site Scripting, Session Hijacking, Cookie Poisoning, Cookie Theft dan Tracking. 

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  - Membuat fungsi register, login_user, dan logout_user
  - Membuat file register.html dan login.html sebagai tampilan register dan login user
  - Membuat routing ke register.html dan login.html
  - Merestriksi akses halaman main agar halaman main dapat diakses setelah login
</details>

<details>
<summary><b> WEEK 03</b> </summary>
## Apa perbedaan antara form POST dan form GET dalam Django?
  - GET kurang aman dibanding POST karena data yang di kirim terlihat di URL, sedangkan POST lebih aman karena parameternya tidak disimpan pada history browser atau web server logs. 
  - POST mengolah data dalam jumlah yang lebih besar dibanding GET
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
  XML dan JSON digunakan untuk menyimpan dan mentransfer data dari server, HTML digunakan untuk membuat halaman web dan menampilkan konten di web browser. 
  XML  = menggunakan tag untuk mengidentifikasi elemen data, tidak memiliki aturan baku mengenai struktur data, lebih sulit untuk dibaca, support berbagai encoding
  JSON = menggunakan key dan value, mudah dibaca oleh manusia, mendukung struktur data string, support UTF-8 encoding 

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
  - memiliki ukuran data yang lebih kecil sehingga membuat data transmission lebih cepat
  - lebih aman dibanding XML
  - lebih mudah dibaca oleh manusia
  - mendukung banyak bahasa pemrograman
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

</details>    

<details>
<summary><b> WEEK 02</b> </summary>
Link aplikasi adaptable
https://tugaspbp1.adaptable.app

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    https://drive.google.com/file/d/1TVLLRZlJUmTPMGW8OFcG9GWs7_ygGAoe/view?usp=sharing

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Untuk memisahkan project django dengan project yang lain, sehingga tidak terjadi overlapping.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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
   
</details>