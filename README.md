# Judul Game

Apocalypse Dominator

# Deskripsi Game

Apocalypse Dominator adalah sebuah game first-person. Game ini dibuat menggunakan bahasa pemrograman Python dan library Pygame. Dalam game ini, pemain akan memerankan karakter Ghulwan, seorang prajurit uji coba yang berhasil dihidupkan kembali setelah ratusan tahun dibekukan. Ghulwan dan timnya diberi misi untuk mencari tahu penyebab terjadinya munculnya makhluk ganas yang telah menghancurkan hampir 80% kehidupan di bumi. Dalam perjalanan misinya, Tokoh utama harus berhadapan dengan berbagai macam makhluk ganas yang bisa mengubah manusia menjadi satu di antara mereka. Untuk menghadapinya, Tokoh utama akan dilengkapi dengan senjata yang digunakan untuk melalui pertarungan melawan beberapa makhluk yang telah diciptakan. Kami telah menerapkan beberapa konsep PBO pada game ini yaitu inheritance, abstraction, polymorphism, dan encapsulation untuk membuat gameplay yang menarik dan seru.

# Cara Menjalankan Game
## Installing Python On Windows

The preliminary step consists in installing
the Python interpreter (i.e., the "master program")
on your computer.

**Installing Python is a one-time operation.**
If you already installed Python in the past
(for example, to run a different program),
you do not need to install it again,
and you can skip to the next section.

### Step 0: Should I Get Python 2 Or Python 3?

At the time of writing (2017-01-01),
there are two main versions of Python:
**Python 2** (2.7.13) and **Python 3** (3.6.0).

Discussing the technical differences between these two versions
is beyond the scope of this guide.
It suffices to say that
some Python programs work with both versions of Python,
while other Python programs work only
with Python 2 but not with Python 3,
or vice versa.

**You should get the version of Python that the program
you are interested in recommends.**
If the latter does not specify a version,
get the latest Python 3 version available.
If you later discover that your Python program
does not work with the Python version you installed,
do not worry: just uninstall it, and install the other one!

In the rest of the guide we assume you need **Python 3**.

### Step 1: Download The Installer

First, open your Web browser and
go to [https://python.org/](https://python.org/):

![Python home page](imgs/010_pythonorg.png)

Click on the **Download > Latest Python 3.6.0** link.

You will get a page listing all the new features of Python 3.6.0:

![Python 3.6.0 download page](imgs/020_download.png)

Scroll down until you see the list of available downloads:

![Python 3.6.0 downloads](imgs/021_download.png)

If you have a recent Windows computer,
very likely it is a 64-bit machine,
so you should download the file labeled **Windows x86-64 executable installer**,
and save it on your Download folder or on your Desktop:

![Python 3.6.0 downloads](imgs/030_downloaded.png)

Downloading the file will take from few seconds to a few minutes,
depending on the bandwidth of your Internet connection.

(If you have an older PC that you know is a 32-bit computer,
download the **Windows x86 executable installer** instead.
You can tell whether your PC is a 32-bit or a 64-bit machine
by reading the **System Information** in the **Windows Control Panel**.)

### Step 2: Install Python

Double-click on the file you just downloaded
to start the installation wizard:

![Python 3.6.0 installer](imgs/040_installer.png)

By default, the **Add Python 3.6 to PATH** option is disabled,
but **you should select it**,
as it makes running Python programs much much easier.

Most users should click the **Install Now** button,
which installs Python with the default settings.
(If you want to personalize your installation
or you are told to enable some advanced features,
click on the **Customize installation** option instead.)

The installer might ask you for administrative privileges
or for confirmations like the following:

![Python 3.6.0 installer asking for confirmation](imgs/041_installer.png)

You can safely answer **Yes**.

A progress bar will appear:

![Python 3.6.0 installer progress bar](imgs/042_installer.png)

until the installation completes with the following message:

![Python 3.6.0 installer completed](imgs/043_installer.png)

Starting with Python 3.6.0,
it is recommended to click on
the **Disable path length limit** option,
before closing the installer.
If you do so, you will get a final confirmation dialog:

![Python 3.6.0 installer completed](imgs/044_installer.png)

You can terminate the installation by clicking the **Close** button.

Congratulations, you have **your first Python installation** under your belt!

# Cara Bermain

Kami menggunakan kontrol mouse dan keyboard sebagai penggerak sebagaimana umumnya game yang ada. Dengan menggunakan W untuk maju, A untuk bergerak ke arah kiri, S untuk bergerak mundur, D untuk bergerak kearah kanan, dan R untuk reload. Kami juga menggunakan mouse untuk interaksi antara karakter yang kami buat dengan user agar karakter bisa melihat 360°. Kami juga menggunakan tombol kanan untuk menembak. Untuk menyelesaikan game ini pemain diharuskan untuk mengalahkan seluruh musuh yang ada serta mengalahkan bos terakhir. Player juga bisa menambah HP dengan mengambil item yang heal yang telah disediakan.

# Dependensi paket (library) yang dibutuhkan untuk menjalankan aplikasi :

Pygame
System
Textwarp
Time
Math

## UML Class Diagram

![Contoh Gambar](DiagramUML.jpeg)

# Kontributor

| Nama                       | NIM       | Kontribusi                             |
| -------------------------- | --------- | -------------------------------------- |
| Ghulwan Shihabuddin (lead) | 121140164 | Story + Asset Game                     |
| Ihsan Triyadi              | 121140163 | Map + Asset Game                       |
| Andreas Sihotang           | 121140168 | Main Programmer                        |
| Ahmad Fadillah             | 121140173 | Project Manager + Secondary Programmer |
| M Daffa Fahreza            | 121140178 | Enemmy + Asset Game + PPT              |
| Daffa Abdurohman Jatmiko   | 121140181 | Secondary Programmer + UML             |
