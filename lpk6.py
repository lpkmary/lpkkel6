import streamlit as st
test=st.sidebar.selectbox("Navigation",['Home👩🏻‍🔬',"About Asam Kuat dan Basa Kuat🧪", "About Us"])
st.image('logos.jpg')

with st.sidebar.container():
 st.sidebar.markdown("RX-Labs - Balance Chemical Equations App")
 st.image('subheader.jpg')

if test == "Home👩🏻‍🔬":
    st.title(':blue[Penyetaraan reaksi antara asam kuat dengan basa kuat]')
    st.markdown('''Hai users, selamat datang di web kami.😊''')
    st.markdown('''Aplikasi ini dapat digunakan untuk meneyetarakan reaksi kimia dari suatu senyawa asam kuat dan basa kuat.''')

    tombol=st.button('OLEH KELOMPOK 6')
    if tombol:
        st.write('Kayla Alifa (2360154)')
        st.write('Mary Rianti Supriyanto (2360170)')
        st.write('Muhamad Renaldi Irawan (2360178)')
        st.write('Nasywaa Farida (2360203)')
        st.write('Punandita Denar Anggraini (2360224)')
    tab1,tab2,tab3=st.tabs(['Asam Kuat','Basa Kuat','Penyetaraan reaksi'])

    def cariHasilWithKurung(asamKuat, basaKuat):
        right_side = " + 2H2O"
        asam = asamKuat.split("H")[1]  # Br
        basa = basaKuat.split("(")[0]  # Ca
        number_of_basa = basaKuat.split(")")[1]
        left_side = f"{basa}({asam}){number_of_basa}"

        hasil = left_side + right_side
        temporary = f"2{asamKuat} + {basaKuat} → {hasil}"
        st.success(f"Hasil dari {asamKuat} + {basaKuat} -> {temporary}")

    def cariHasil(asamKuat, basaKuat):
        isThereIsOinAsamKuat = 0
        if "O" in asamKuat:
            isThereIsOinAsamKuat = 1
        
        count_asam_kuat_h = asamKuat.count("H")
        count_asam_kuat_o = asamKuat.count("O") - isThereIsOinAsamKuat
        count_basa_kuat_h = basaKuat.count("H")
        count_basa_kuat_o = basaKuat.count("O")

        totalH = count_asam_kuat_h + count_basa_kuat_h
        totalO = count_asam_kuat_o + count_basa_kuat_o

        right_side = " + "
        h_side = "H"
        o_side = "O"
        if totalH > 1:
            h_side = f"H{totalH}"

        if totalO > 1:
            o_side = f"O{totalO}"

        right_side += f"{h_side}{o_side}"

        asam = asamKuat.split("H")[1]
        basa = basaKuat.split("OH")[0]
        left_side = basa + asam
        hasil = left_side + right_side
        st.success(f'Hasil reaksi dari {asamKuat} + {basaKuat} -> {hasil}')

    with tab1:
        st.header('Contoh Asam Kuat', divider='rainbow')
        st.write('Asam kuat adalah asam yang dapat terionisasi sempurna di dalam air')
        st.write('beberapa contoh asam kuat adalah:')
        st.write('Asam klorida (HCL)')
        st.write('Asam nitrat (HNO3)')
        st.write('Asam sulfat (H2SO4)')
        st.write('Asam bromida (HBr)')
        st.write('Asam iodida (HI)')
        st.write('Asam klorat (HClO3)')
        st.write('Asam peklorat (HClO4)')

    with tab2:
        st.header('Contoh Basa Kuat', divider='rainbow')
        st.write('Basa kuat adalah basa yang dapat terionisasi sempurna di dalam air')
        st.write('beberapa contoh basa kuat adalah:')
        st.write('Litium hidroksida (LiOH)')
        st.write('Natrium hidroksida (NaOH)')
        st.write('Kalium hidroksida (KOH)')
        st.write('Kalsium hidroksida (Ca(OH)2)')
        st.write('Rubidium hidroksida (RbOH)')
        st.write('Stronsium hidroksida (Sr(OH)2)')
        st.write('Sesium hidroksida (CsOH)')
        st.write('Barium hidroksida (Ba(OH)2)')
        st.write('Magnesium hidroksida (Mg(OH)2)')
        st.write('Berilium hidroksida (Be(OH)2)')

    with tab3:
        st.header('Penyetaraan Reaksi', divider='rainbow')
        st.write('Reaksi antara asam kuat dengan basa kuat akan menghasilkan pH larutan yang dihasilkan bersifat netral atau pH = 7')
        options1=st.selectbox(
            'pilih senyawa asam kuat',
            ['HCl','HNO3','H2SO4','HBr','HI','HClO3','HClO4'])
        
        options2=st.selectbox(
            'pilih senyawa basa kuat',
            ['LiOH', 'NaOH','KOH','Ca(OH)2','RbOH','Sr(OH)2','CsOH','Ba(OH)2','Mg(OH)2','Be(OH)2'])

        tombol = st.button('Penyetaraan reaksi')
        if tombol:
            if(len(options2.split(")")) == 1):
                cariHasil(options1, options2)
            else:
                cariHasilWithKurung(options1, options2)
            st.balloons()

if test == "About Asam Kuat dan Basa Kuat🧪":
    tab1,tab2=st.tabs(['Pengertian Asam dan Basa','Penyetaraan reaksi'])

    with tab1:
        st.title(':green[Apa itu Asam dan Basa?]')
        st.subheader('Pengertian Asam Basa', divider='blue')
        st.write('Asam dan basa adalah larutan elektrolit yang dikenal dengan ciri khasnya, seperti asam yang memiliki rasa masam dan basa yang memiliki rasa pahit. Asam dan basa pengertian menurut Kamus Besar Bahasa Indonesia (KBBI), asam adalah zat yang dapat memberikan proton, zat yang dapat membentuk ikatan kovalen dengan menerima sepasang elektron. Sedangkan, basa adalah senyawa yang cenderung menyumbangkan sepasang elektron untuk dipakai bersama-sama dan menerima proton. Sementara itu, istilah asam (acid) berasal dari bahasa Latin, yaitu acetum, yang artinya cuka. Lalu, basa (alkali) berasal dari Arab, yang artinya abu. Basa banyak dijumpai dalam pembuatan sabun, seperti yang kita ketahui di zaman dahulu banyak ibu rumah tangga yang menggunakan abu untuk mencuci piring.')
        st.image('Tabel.jpg')
        st.subheader('Teori Asam Basa', divider='blue')
        st.write('Ilmu pengetahuan yang semakin berkembang, membuat asam basa pun semakin diteliti lebih lanjut. Setidaknya, ada teori asam basa dari tiga ilmuwan populer yang perlu diketahui. Berikut penjelasannya:')
        
        st.subheader('Teori Arhenius')
        st.write('Asam basa Arrhenius menyatakan bahwa asam adalah zat yang apabila dilarutkan dalam air akan menghasilkan ion H+ dalam larutan dan basa adalah zat yang apabila dilarutkan dalam air akan menghasilkan ion OH– dalam larutan. Dari pengertian tersebut, bisa disebutkan ciri khas asam adalah apabila dalam pelarut air, zat akan mengion menjadi hidrogen dengan muatan positif dan ion yang bermuatan negatif tersebut adalah sisa asam. Lalu, ciri khas basa adalah apabila dalam pelarut air, zat akan mengion menjadi ion hidroksida yang muatannya negatif dan ion bermuatan positif disebut sisa basa.')
        
        st.subheader('Teori Bronsted Lowry')
        st.write('Teori asam basa menurut Bronsted Lowry didefinisikan berdasarkan kemampuan (donor) atau menerima (akseptor) proton (ion H+). Senyawa yang bertindak sebagai asam basa Bronsted Lowry disebut amfoter. Sementara itu, konsep asam basa Bronsted Lowry bisa dijelaskan bahwa asam adalah zat yang punya kecenderungan untuk menyumbang ion H+ pada zat lain dan basa adalah zat yang punya kecenderungan untuk menerima ion H+ dari zat lain. Bronsted Lowry juga mencetuskan teori asam basa konjugasi. Asam konjugasi adalah basa yang memperoleh ion hidrogen, sedangkan basa konjugasi adalah yang tersisa setelah asam memberikan proton dalam sebuah reaksi kimia. Kedua hal tersebut disebut pasangan asam basa konjugasi.')
        
        st.subheader('Teori Asam Basa Lewis')
        st.write('Asam basa Lewis menjelaskan terkait struktur dan ikatannya. Asam menurut Lewis adalah zat yang punya kecenderungan menerima pasangan elektron basa, sedangkan basa adalah zat yang memberikan pasangan elektron.')
        
        st.subheader('Klasifikasi Asam Basa', divider='blue')
        st.write('Asam basa diklasifikasikan menjadi dua, yaitu asam basa kuat dan asam basa lemah. Berikut ini penjelasannya:')

        st.subheader('Asam Kuat', divider='rainbow')
        st.write('Asam kuat adalah jenis asam yang dapat sepenuhnya terionisasi atau berdisosiasi dalam larutan air, menghasilkan ion hidrogen (H⁺) dalam jumlah besar.')
        st.write('Contoh Asam Kuat:')
        st.write('Asam Klorida (HCl): Merupakan gas yang larut dalam air membentuk larutan asam kuat. Asam Sulfat (H₂SO₄): Asam kuat ini digunakan secara luas dalam industri dan laboratorium.')
        st.write('Sifat-sifat Asam Kuat:')
        st.write('⚛ Ionisasi total dalam larutan air.')
        st.write('⚛ Memiliki kemampuan konduktivitas listrik yang tinggi.')
        st.write('⚛ Bereaksi dengan cepat dengan basa atau zat lainnya dalam larutan.')
        st.write('⚛ Rasa asam yang kuat.')
        st.write('⚛ Larut dengan baik dalam air.')
        st.write('  Asam kuat memainkan peran penting dalam berbagai industri karena sifat-sifatnya yang unik dan kemampuannya untuk berfungsi sebagai agen kimia yang kuat.  Asam kuat sering digunakan sebagai katalis atau reagen dalam berbagai reaksi kimia, seperti reaksi esterifikasi, hidrolisis, dan polimerisasi. Asam klorida (HCl), digunakan dalam proses pembersihan dan pelapisan logam untuk menghilangkan oksida, karat, dan kotoran lainnya dari permukaan logam. Asam sulfat (H₂SO₄) adalah bahan baku penting dalam industri pupuk, digunakan dalam produksi pupuk fosfat super, amonium sulfat, dan lainnya.     Asam kuat kadang-kadang digunakan dalam sintesis obat-obatan tertentu, serta dalam pembuatan bahan baku farmasi.  Asam kuat digunakan dalam proses pembersihan dan sterilisasi peralatan dan wadah dalam industri farmasi. Penggunaan asam kuat di industri menunjukkan keragaman aplikasi dan pentingnya zat kimia ini dalam berbagai proses produksi. Namun, penggunaannya juga memerlukan perhatian terhadap keselamatan, pengelolaan limbah, dan dampak lingkungan yang mungkin timbul.')
        
        
        st.subheader('Basa Kuat', divider='rainbow')
        st.write('Basa kuat adalah jenis basa yang dapat sepenuhnya terdisosiasi dalam larutan air, menghasilkan ion hidroksida (OH⁻) dalam jumlah besar.')
        st.write('Contoh Basa Kuat:')
        st.write('Natrium Hidroksida (NaOH): Basa kuat yang larut dalam air dan digunakan dalam berbagai aplikasi industri. Kalium Hidroksida (KOH): Basa kuat ini juga digunakan dalam berbagai proses industri.')
        st.write('Sifat-sifat Basa Kuat:')

        st.write('⚛ Ionisasi total dalam larutan air.')
        st.write('⚛ Memiliki kemampuan konduktivitas listrik yang tinggi.')
        st.write('⚛ Bereaksi dengan cepat dengan asam atau zat lainnya dalam larutan.')
        st.write('⚛ Rasa pahit atau licin pada konsentrasi tinggi.')
        st.write('⚛ Larut dengan baik dalam air.')
        st.write('Seperti halnya asam kuat, Basa Kuat memiliki peran penting dalam berbagai industri karena sifat-sifatnya yang kuat dan kemampuannya untuk berfungsi sebagai agen kimia yang efektif. Basa kuat, seperti natrium hidroksida (NaOH) atau kalium hidroksida (KOH), sering digunakan sebagai bahan aktif dalam pembersih rumah tangga, seperti pembersih lantai, pembersih oven, dan pembersih toilet. Basa kuat digunakan dalam pembuatan sabun, baik sabun cair maupun sabun batangan, sebagai bahan aktif untuk menghasilkan proses saponifikasi. Basa kuat digunakan dalam proses pembuatan pulp dan kertas untuk melarutkan lignin dari serat kayu dan memisahkannya dari selulosa. Basa kuat digunakan dalam proses pemisahan dan pemurnian berbagai komponen minyak bumi dan produk turunannya dalam industri petrokimia. Basa kuat juga digunakan untuk membersihkan pipa, tangki, dan peralatan lainnya dari residu minyak dan bahan kimia lainnya. Basa kuat juga digunakan untuk pembersihan dan sanitasi peralatan dan instalasi dalam industri makanan dan minuman.')

        st.subheader('Asam basa lemah', divider='rainbow')
        st.write('Asam lemah adalah senyawa yang dilarutkan dalam air akan sulit melepaskan ion H+ dan mengalami disosiasi pada larutan. Sedangkan, basa lemah adalah senyawa yang apabila dilarutkan di dalam air akan sulit melepaskan ion OH- dan mengalami disosiasi dalam larutan.')
    
    with tab2:
        st.title(':green[Pengertian Penyetaraan Persamaan Reaksi dalam Kimia]')
        st.image('reaksi.jpg')
        st.write('Penyetaraan reaksi kimia adalah proses mengatur koefisien stoikiometri dalam suatu persamaan kimia sehingga jumlah atom dari setiap unsur di sisi reaktan sama dengan jumlah atom dari setiap unsur di sisi produk. Tujuannya adalah untuk menjaga hukum kekekalan massa dan hukum kekekalan muatan dalam reaksi kimia. Dengan kata lain, penyetaraan reaksi kimia memastikan bahwa apa pun yang masuk ke dalam reaksi akan sama dengan apa pun yang keluar dari reaksi, dalam hal jumlah atom dari masing-masing unsur yang terlibat.')
        st.write('Langkah-langkah umum penyetaraan untuk persamaan reaksi kimia adalah sebagai berikut.')
        st.write(
        """
    1. Mengenali unsur-unsur yang terlibat di sisi reaktan dan produk persamaan reaksi.
    2. Menentukan jumlah atom setiap unsur di sisi reaktan dan produk.
    3. Ubah koefisien stoikiometri untuk salah satu unsur, sehingga jumlah atom unsur tersebut sama di kedua sisi persamaan reaksi.
    4. Setelah selesai dengan unsur pertama, lanjutkan ke unsur berikutnya hingga seluruh unsur telah disetarakan.
    5. Pastikan bahwa seluruh koefisien stoikiometri dalam persamaan reaksi adalah bilangan bulat terkecil yang mungkin.
    6. Jika perlu, faktorkan kelipatan persekutuan terkecil (FPB) dari koefisien tersebut untuk mendapatkan hasil yang lebih sederhana.
    """
     )
        st.subheader('Penerapan Reaksi Asam Basa', divider='rainbow')  
        st.write(
        """
        Tanpa kita sadari, reaksi asam basa ini cukup sering digunakan dalam kehidupan sehari-hari, seperti pada makanan, obat, dan produk-produk perawatan tubuh. Berikut adalah beberapa contoh penerapan reaksi asam basa ini.
        1. Obat asam lambung,
        Asam lambung adalah suatu kondisi ketika asam lambung naik ke kerongkongan sehingga menimbulkan rasa yang tidak nyaman pada perut.
        Seperti yang namanya, asam lambung (HCl) termasuk asam kuat sehingga untuk menetralkannya dibutuhkan obat yang mengandung basa. Salah satunya adalah magnesium hidroksida (Mg(OH)2).
        Dengan adanya, kandungan magnesium hidroksida ini asam lambung yang naik ke kerongkongan pun dapat dinetralkan sehingga gejala asam lambung dapat mereda. Ini merupakan salah satu bentuk penerapan reaksi asam basa dalam obat-obatan.
        2. Pasta gigi,
        Salah satu kandungan dalam pasta gigi adalah natrium fluorida termasuk dalam kelompok basa lemah. Mengapa digunakan kandungan yang bersifat basa dalam pasta gigi?
        Hal ini dikarenakan, pH yang tinggi pada senyawa basa dapat mengontrol pH asam dalam mulut sehingga keadaan mulut pun menjadi netral. Selain itu, bakteri lebih suka tinggal pada lingkungan yang asam. Jadi, kalau mulut kamu asam, maka bakteri akan lebih mudah berkembang biak di dalam mulut.
        3. Kesuburan Tanah,
        Reaksi asam basa juga dimanfaatkan dalam bidang pertanian. Salah satunya adalah untuk menyuburkan tanah.
        Keasaman tanah berkaitan erat dengan kesuburan. Semakin asam tanah tersebut, semakin berkurang kesuburannya.
        Tanah yang asam ini dapat disuburkan kembali dengan cara menetralkannya ')
            """)
if test == "About Us":
    st.title(':green[Apa itu RX-Labs - Balance Chemical Equations App?]')
    st.subheader("Hello, to all user :wave:")
    st.write("Rx Labs adalah sebuah web aplikasi yang di design untuk menyetarakan reaksi asam kuat basa kuat dan mengenal lebih dalam apa itu asam kuat dan basa kuat.")
    st.write("---")
    st.header("Apa yang Rx-Labs lakukan")
    st.write("##")
    st.write('Di Web Aplikasi pH Analisis ini, kita akan menyediakan untuk orang-orang yang:')
    st.write(
    """
    Di Web Aplikasi pH Analisis ini, kita menyediakan bagi kamu yang:
    - Ingin belajar tentang asam kuat dan basa kuat
    - Penyetaraan reaksi asam kuat dengan basa kuat

    Share web ini jika menarik dan bermanfaat bagi Anda 👍
    """
    )

