import math

RES = WITDH, HEIGHT = 1920, 1080
HALF_WITDH = WITDH // 2
HALF_HEIGHT = HEIGHT //2
FPS = 60

PLAYER_POS = 1.5 , 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_SIZE_SCALE = 10
PLAYER_MAX_HP = 100

MOUSE_SENS = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WITDH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WITDH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WITDH / math.tan(HALF_FOV)
SCALE = WITDH // NUM_RAYS

TEXTURE_SIZE = 512
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

SET_VOLUME = .5

dialog_data = []
dialog_data_prologue = [
    {
        "text": "Pada Tahun 20XX, Bumi mengalami kekacauan dengan datangnya monster-monster yang ingin mendominasi Bumi",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Para monster sudah menyebar terlalu banyak sehingga populasi manusia saat ini hanya berkisar 20%",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Masih menjadi misteri darimana monster tersebut tetapi diduga ada beberapa orang mencurigakan terlibat",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Manusia yang tersisa bersembunyi di dalam bunker yang dihuni beberapa warga dan ilmuwan",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Para ilmuwan sudah menyiapkan beberapa prajurit uji coba yang sudah dibekukan sebelum bencana terjadi",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Para prajurit tersebut telah di cairkan untuk melawan monster yang sudah mulai menginvasi bumi",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Uhh...dimana ini?",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Sudah waktunya bangun ghulwan, dunia sekarang dilanda kekacauan",
        "chara": "David",
        "character_image": "textures\chara\david.png",
    },
    {
        "text": "David!? Jadi begitu, jelaskan rinciannya!",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "David menjelaskan keadaan bumi dan bagaimana dia sudah dibangunkan",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Bagaimana dengan prajurit lain?",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Mereka sudah menjalani proses pencairan dan sedang menunggu di luar",
        "chara": "David",
        "character_image": "textures\chara\david.png",
    },
    {
        "text": "Baiklah ayo kita temui mereka",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Wah lihat siapa yang baru terbangun",
        "chara": "Ihsan",
        "character_image": "textures\chara\ihsan.png",
    },
    {
        "text": "Sekarang akhirnya kita lengkap",
        "chara": "Jatmiko",
        "character_image": "textures\chara\jatmiko.png",
    },
    {
        "text": "Haha sepertinya kalian baik-baik saja ya",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Waktunya bertugas kah?",
        "chara": "David",
        "character_image": "textures\chara\david.png",
    },
    {
        "text": "Santai dulu ga sih?",
        "chara": "Jatmiko",
        "character_image": "textures\chara\jatmiko.png",
    },
    {
        "text": "Iya, selama kita di bunker pasti akan ama-",
        "chara": "Ihsan",
        "character_image": "textures\chara\ihsan.png",
    },
    {
        "text": "Tiba-tiba terdengar suara ledakan dan sirine berbunyi diiringi para tentara dan beberapa monster menerobos bunker",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Hahaha...Akhirnya kutemukan, para tentara serang mereka!",
        "chara": "Andre",
        "character_image": "textures\chara\omandre.png",
    },
    {
        "text": "Dia kan Professor Andre, ilmuwan terbaik sebelum kita dibekukan",
        "chara": "Ihsan",
        "character_image": "textures\chara\ihsan.png",
    },
    {
        "text": "Kudengar dia hilang secara misterius",
        "chara": "Jatmiko",
        "character_image": "textures\chara\jatmiko.png",
    },
    {
        "text": "Sepertinya kita tahu alasannya, dan harus menghentikannya",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Waduh tapi kita belum makan sama sekali",
        "chara": "Ihsan",
        "character_image": "textures\chara\ihsan.png",
    },
    {
        "text": "MAKAN TIDAK PERLU, TARUNG NOMOR SATU!!!",
        "chara": "David",
        "character_image": "textures\chara\david.png",
    },
    {
        "text": "Ayo maju!",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
]

dialog_data_epilog = [
    {
        "text": "Huft...Apakah sudah selesai?",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Dimana Prof. Andre?",
        "chara": "Jatmiko",
        "character_image": "textures\chara\jatmiko.png",
    },
    {
        "text": "HAHAHA...Akhirnya kudapatkan hal yang dibutuhkan!",
        "chara": "Andre",
        "character_image": "textures\chara\omandre.png",
    },
    {
        "text": "Dengan ini karya terbaikku akan tercipta...Adios para prajurit!",
        "chara": "Andre",
        "character_image": "textures\chara\omandre.png",
    },
    {
        "text": "Waduhh...dia kabur",
        "chara": "David",
        "character_image": "textures\chara\david.png",
    },
    {
        "text": "Setidaknya kita tahu kalau dialah yang menciptakan monster",
        "chara": "Jatmiko",
        "character_image": "textures\chara\jatmiko.png",
    },
    {
        "text": "Mau tidak mau kita harus keluar bunker kah...",
        "chara": "Ihsan",
        "character_image": "textures\chara\ihsan.png",
    },
    {
        "text": "Perjalanan kita masih panjang",
        "chara": "Ghulwan",
        "character_image": "textures\chara\ghulwan.png",
    },
    {
        "text": "Para prajurit berhasil mengalahkan musuh-musuh yang menyerang bunker mereka",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Tetapi, Prof.Andre berhasil kabur dengan membawa sesuatu untuk niat jahatnya",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "Para prajurit akan memulai petualangan mereka menghadapi musuh yang lebih berbahaya",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
    {
        "text": "TO BE CONTINUED",
        "chara": "Watcher",
        "character_image": "textures\chara\watcher.png",
    },
]
dialog_data.append(dialog_data_prologue)
dialog_data.append(dialog_data_epilog)

