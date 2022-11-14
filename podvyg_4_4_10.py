CURRENT_OS = 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(*args, *kwargs)
        elif CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(*args, *kwargs)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        obj = WindowsFileDialog(title, path, exts)
        return obj

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        obj = LinuxFileDialog(title, path, exts)
        return obj


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg)



