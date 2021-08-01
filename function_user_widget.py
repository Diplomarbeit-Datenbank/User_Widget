"""

    -> Library for User Widget to create basic functions like Create a New User Interface and Open User with
       Password Interface

"""

__date__ = '21.07.2021'
__completed__ = '--.--.--'
__work_time__ = 'about -- Hours'
__author__ = 'Christof Haidegger'
__version__ = '1.0'
__licence__ = 'Common Licence'
__debugging__ = 'Christof Haidegger'

from PIL import Image as _Image
from tkinter import filedialog
from tkinter import messagebox
from lib import languages
import Ctkinter as Ctk
import tkinter as tk
import numpy as np
import random
import shutil
import cv2
import os


class CreateNewUser:
    """

        -> Class to create a new user

    """
    __is_open = False  # to make sure, this window is only once opened

    def __init__(self, language='english'):
        """

        :param language: language for the new user widget
        """
        if type(self).__is_open is True:
            return

        type(self).__is_open = True
        __Background__ = 'gray35'

        self.entry_list = list()
        self.profile_image_is_set = False
        self.add_profile_gif_button = None
        self.gif_file_path = None

        self.language = languages.Language('languages/languages.txt', language=language)
        self.new_user_window = tk.Toplevel()
        self.new_user_window.title(self.language.refactor('Add User'))
        self.new_user_window.resizable(False, False)
        self.new_user_window.protocol("WM_DELETE_WINDOW", self._set_is_open_to_false)
        self.new_user_window.bind('<Return>', lambda event: self._get_information(self.entry_list[0].get(),
                                                                                  self.entry_list[1].get()))
        self.new_user_window.geometry("450x250")
        self.new_user_window.config(bg=__Background__)

        # run functions
        self._create_add_profile_gif(bg='gray25', size=(180, 180), place0=(10, 0), place1=(15, 50))
        self._create_info_labels(place0=(200, 50), place1=(200, 140))
        self._create_text_widgets(place0=(220, 93), place1=(220, 183))
        self._create_logo_image(place=(335, 5))
        self._create_and_abort_button(place=(280, 222))

        self.new_user_window.mainloop()

    def _get_information(self, nik_name, password):
        """

        :param nik_name: nik name for the new user or user name
        :param password: password for the new user if given
        :return:         get and store the information in a new folder and file
        """
        check_available = open('Users/All_Users.txt', 'r+')
        user_name_list = check_available.read().split('\n')
        if nik_name == '':
            messagebox.showwarning(title=self.language.refactor('No Nik Name'),
                                   message=self.language.refactor('Please enter nik name before continue'))
            self.new_user_window.lift()
            return

        if password == '':
            yes_no = messagebox.askquestion(title=self.language.refactor('No Password'), message=self.language.
                                            refactor('Would you like to have a password for your account?'))
            self.new_user_window.lift()
            if yes_no == 'yes':
                return
            password = 'False'

        if nik_name in user_name_list:
            messagebox.showwarning(title=self.language.refactor('User already exist'),
                                   message=self.language.
                                   refactor('This user name is already taken please try another one'))
            check_available.close()
            self.new_user_window.lift()
            return
        else:
            check_available.write(nik_name + '\n')
            check_available.close()

        os.mkdir('Users/' + str(nik_name) + '/')
        properties_file = open('Users/' + str(nik_name) + '/properties.txt', 'w')
        to_write = [nik_name, password, str(self.profile_image_is_set), str(0), str(0)]

        for item in to_write:
            properties_file.write(item + '\n')

        properties_file.close()

        if self.gif_file_path is not None:
            gif_name = self.gif_file_path.split('/')[len(self.gif_file_path.split('/')) - 1]
            shutil.copy(self.gif_file_path, 'Users/' + str(nik_name) + '/')
            os.rename('Users/' + str(nik_name) + '/' + gif_name, 'Users/' + str(nik_name) + '/profile.gif')
        else:
            character = nik_name[0]
            (text_width, text_height) = cv2.getTextSize(character, cv2.FONT_ITALIC, 7, 8)[0]

            new_image = np.zeros([250, 250, 3], dtype=np.uint8)
            new_image[0: 250, 0: 250] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            cv2.putText(new_image, character, (int((250 - text_width) / 2), int((250 + text_height) / 2)),
                        cv2.FONT_ITALIC, 7, (255, 255, 255), 8, cv2.LINE_8)
            pil_array = _Image.fromarray(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
            pil_array.save(os.path.join('Users/' + str(nik_name), 'profile.gif'))

        check_available.close()

        self.new_user_window.destroy()

    def _create_and_abort_button(self, place):
        """

        :param place: place for the create and abort button
        :return:      place the create and abort button on the given coordinates
        """
        commands = [lambda: self._set_is_open_to_false(),
                    lambda: self._get_information(self.entry_list[0].get(), self.entry_list[1].get())]
        text_list = [self.language.refactor('Abort'), self.language.refactor('Create')]
        for place, text, command in zip([place, (place[0] + 85, place[1])], text_list, commands):
            button = Ctk.CButton(self.new_user_window, bg='gray12', highlight_color='gray40', pressing_color='gray80',
                                 width=83, height=25, text=text, font=('Helvetica', 12),
                                 fg='white', command=command, rounded_corners='angular')
            button.place(*place)

    def _set_is_open_to_false(self):
        """

        :return: destroy the window and set is open value which is on type to false
        """
        type(self).__is_open = False
        self.new_user_window.destroy()

    def _create_add_profile_gif(self, bg, size, place0, place1):
        """

        :param bg:     background for the add profile gif icon
        :param size:   size for the icon
        :param place0: place0 is the place for the info label
        :param place1: place1 is the place for the button
        :return:       place the info label and the button on the given place
        """
        info_label = Ctk.CLabel(self.new_user_window, bg=self.new_user_window['background'], size=(180, 40),
                                text=self.language.refactor('Profile Image'), fg='black', font=('Helvetica', 16),
                                corner='angular')
        info_label.place(*place0)
        self.add_profile_gif_button = Ctk.CButton(self.new_user_window, bg=bg, highlight_color='gray12',
                                                  pressing_color='gray80', width=size[0], height=size[1],
                                                  text='+', font=('Courier', 100), fg='white',
                                                  rounded_corners='rounded', command=self._add_profile_image)

        self.add_profile_gif_button.place(*place1)

    def _add_profile_image(self):
        """

            -> Add the Profile image if it is selected

        :return:
        """
        self.profile_image_is_set = True
        file_name = filedialog.askopenfilename(initialdir="/", title=self.language.refactor("Select GIF file"),
                                               filetypes=(("GIF files", "*.gif"),))
        if file_name == '':
            self.new_user_window.lift()
            return

        self.add_profile_gif_button.destroy()
        gif_canvas = Ctk.CCanvas(self.new_user_window, corners='angular', size=(180, 180),
                                       bg=self.new_user_window['background'])
        gif_canvas.create_gif(gif_path=file_name, corner='round', size=(175, 175), pos=(90, 90),
                                    transparent=True, speed='normal')
        gif_canvas.place(*(15, 50))

        self.gif_file_path = file_name

        self.new_user_window.lift()

    def _create_logo_image(self, place):
        """

        :param place: place for the PixelBoy logo
        :return:      place the PixelBoy Logo on the new_user_interface
        """
        self.logo_canvas = Ctk.CCanvas(self.new_user_window, bg=self.new_user_window['background'], size=(108, 22),
                                       corners='angular')
        self.logo_canvas.create_image(corner='angular', width=106, height=20, pos=(54, 11),
                                      image_path='images/logo.png',
                                      transparent=True)
        self.logo_canvas.place(*place)

    def _create_info_labels(self, place0, place1):
        """

        :param place0: place for the Enter Nik Name Label
        :param place1: place for the Enter Password Label
        :return:       place the Labels on the new user window
        """
        enter_nik_name = Ctk.CLabel(self.new_user_window, bg=self.new_user_window['background'], size=(150, 35),
                                    text=self.language.refactor('Enter Nik Name'), fg='white', font=('Helvetica', 14),
                                    corner='rounded')
        enter_nik_name.place(*place0)

        enter_password = Ctk.CLabel(self.new_user_window, bg=self.new_user_window['background'], size=(200, 35),
                                    text='*optional: ' + self.language.refactor('Password'), fg='white',
                                    font=('Helvetica', 14), corner='rounded')
        enter_password.place(*place1)

    def _create_text_widgets(self, place0, place1):
        """

        :param place0: place for the first background canvas
        :param place1: place for the first Entry widget
        :return:
        """
        for place in [place0, place1]:
            background_canvas = Ctk.CButton(self.new_user_window, bg='gray8', highlight_color='gray40',
                                            pressing_color='gray40', width=200, height=5, rounded_corners='round',
                                            command=lambda: self.new_user_window.focus_set())
            background_canvas.place(x=place[0] - 5, y=place[1] + 22)
            entry = tk.Entry(self.new_user_window, width=20, bg=self.new_user_window['background'],
                             font=('Helvetica', 14), bd=0)
            entry.place(x=place[0], y=place[1])

            self.entry_list.append(entry)


class OpenUser:
    """

        -> Class to open a user with password security and without

    """
    __is_open = False

    def __init__(self, user_name, func, language):
        """

        :param func: function to run, when the given password is correct
        :param user_name: user name which is to open
        :param language:  language for the selected user
        """
        self.user_name_information = dict()
        self.language = languages.Language(file_path='languages/languages.txt', language=language)
        self._get_user_name_information(user_name)

        # run functions
        self._get_user_name_information(user_name)
        if self.user_name_information.get('Password') != 'False':
            self._get_password_window(user_name=user_name, func=func)
        else:
            func()

    def _get_user_name_information(self, user_name):
        """

        :param user_name: user name which is to open
        :return:          get the information of the current user
        """
        data_to_find = ['UserName', 'Password', 'ProfileImage']
        user_name_file = open('Users/' + str(user_name) + '/properties.txt', 'r')
        user_name_data = user_name_file.read().split('\n')
        for item, data in zip(data_to_find, user_name_data):
            self.user_name_information[item] = data
        user_name_file.close()

    def _get_password_window(self, user_name, func):
        """

        :param user_name: user name to get the password from
        :return:          -> Create a Window to get the password
        """
        def _create_info_labels(nik_name):
            """

            :param nik_name: user name

            """
            info1 = Ctk.CLabel(password_window, bg=password_window['background'], size=(300, 40),
                               text=self.language.refactor('Enter Password for: ') + nik_name, fg='white',
                               font=('Helvetica', 15), corner='angular')
            info1.place(x=5, y=0)

            info2 = Ctk.CLabel(password_window, bg=password_window['background'], size=(300, 40),
                               text=self.language.refactor('Password:'), fg='white', font=('Helvetica', 15),
                               corner='angular')
            info2.place(x=5, y=60)

        def _create_continue_and_abort_button():
            """

                -> Create the tow buttons down on the interface
            """
            continue_button = Ctk.CButton(password_window, bg='gray15', highlight_color='gray50',
                                          pressing_color='gray12', width=250, height=30,
                                          text=self.language.refactor('Log In'),
                                          font=('Helvetica', 14), fg='white', command=_check_password)
            continue_button.place(x=250, y=149)

            continue_button = Ctk.CButton(password_window, bg='gray15', highlight_color='gray50',
                                          pressing_color='gray12', width=249.5, height=30,
                                          text=self.language.refactor('Cancel'),
                                          font=('Helvetica', 14), fg='white', command=_set_is_open_to_false)
            continue_button.place(x=0, y=149)

        def _create_entry():
            """

                -> Create the entry to give the password in
            """
            entry_widget = tk.Entry(password_window, bd=0, font=('Helvetica', 16), width=40,
                                    bg='gray15', fg='white', insertbackground='white')
            entry_widget.place(x=10, y=105)

            entry_widget.focus()

            return entry_widget

        def _create_logo():
            """

                -> Create the logo PixelBoy Icon
            """
            logo_canvas = Ctk.CCanvas(password_window, bg=password_window['background'], size=(108, 22),
                                           corners='angular')
            logo_canvas.create_image(corner='angular', width=106, height=20, pos=(54, 11),
                                          image_path='images/logo.png', transparent=True)
            logo_canvas.place(x=392, y=5)

        def _check_password():
            """

                -> To check if the password is right
            """
            if entry.get() == self.user_name_information['Password']:
                type(self).__is_open = False
                password_window.destroy()
                func()
            else:
                messagebox.showwarning(title=self.language.refactor('Wrong Password'),
                                       message=self.language.refactor('Wrong Password: Please try again'))
                password_window.lift()

        def _set_is_open_to_false():
            """

                -> when the window should be closed -> set type(self).__is_open to false
            """
            type(self).__is_open = False
            password_window.destroy()

        if type(self).__is_open is True:
            # when the window is already open, that the window is not opened twice return none
            return

        password_window = tk.Toplevel()
        type(self).__is_open = True
        password_window.protocol("WM_DELETE_WINDOW", _set_is_open_to_false)
        password_window.resizable(False, False)
        password_window.bind('<Return>', lambda event: _check_password())
        password_window.title(self.language.refactor('Enter Password'))
        password_window.config(bg='gray20')
        password_window.geometry('500x180')

        # run functions
        _create_info_labels(user_name)
        _create_continue_and_abort_button()
        entry = _create_entry()
        _create_logo()

        password_window.mainloop()


class User_Interface:
    """

        -> Class to create a Widget with User Icon, User Name, User Level and User Creations

            -> User Icon  ==> A Animated GIF or the First Letter of the User name
            -> User Name  ==> Just a Label with the name, nothing special
            -> User Level ==> Shows the Level of the User it increases by make creations and play with the Game Frame
            -> User Creat ==> Shows the number of Creations which are made by the User

    """
    def __init__(self, master, user_name, language='english'):
        """

        :param master:    Master, where the Widget should be placed
        :param user_name: Name of the User which should be the information on the Widget
        """
        self.language = languages.Language('languages/languages.txt', language=language)
        self.user_information = dict()
        self.UserInterface = Ctk.CCanvas(master=master, bg='gray25', size=(500, 250), corners='rounded', max_rad=35,
                                         outline=('white', 1))

        # run functions
        self._get_user_information(user_name=user_name)

        self._create_logo_image(place=(375, 8))
        self._create_profile_image(user_name, place=(20, 15))
        self._create_user_name_label(user_name, place=(8, 200))
        self._create_level_label(level=self.user_information.get('Level'), place0=(220, 50), place1=(290, 100))
        self._create_number_of_creations_label(creations=self.user_information.get('NumberOfCreations'),
                                               place0=(220, 150), place1=(290, 200))

    def _get_user_information(self, user_name):
        """

        :param user_name: User Name form __init__
        :return:          fill the User dict() with information
        """
        information = ['UserName', 'Password', 'ProfileImage', 'Level', 'NumberOfCreations']
        user_file = open('Users/' + str(user_name) + '/properties.txt', 'r')
        user_file_data = user_file.read().split('\n')
        user_file.close()
        for item, data in zip(information, user_file_data):
            self.user_information[item] = data

    def _create_profile_image(self, user_name, place):
        """

        :param user_name: User Name from __init()
        :param place:     Place for the profile image
        :return:          Place the Profile Image on teh Widget
        """
        profile_image_canvas = Ctk.CCanvas(master=self.UserInterface, bg=self.UserInterface['background'],
                                           size=(180, 180), corners='angular')
        profile_image_canvas.create_gif(gif_path='Users/' + user_name + '/profile.gif', corner='round', size=(179, 179),
                                        pos=(89, 89), transparent=True)
        profile_image_canvas.place(*place)

    def _create_user_name_label(self, user_name, place):
        """

        :param user_name: User Name from __init()
        :param place:     Place for the User Name Label on the Widget
        :return:          Place the Widget on the Widget
        """
        user_name_label = Ctk.CLabel(master=self.UserInterface, bg=self.UserInterface['background'], size=(200, 40),
                                     text=user_name, fg='white', font=('Helvetica', 20), corner='angular',
                                     anchor='CENTRE')
        user_name_label.place(*place)

    def _create_level_label(self, level, place0, place1):
        """

        :param level:  Level of the current user
        :param place0: place for the info label (Pixel Level:)
        :param place1: place for the Level Value
        :return:       -> Place the Ctk Objects on the Widget
        """
        self._create_arrow((place1[0] - 90, place1[1] + 8))
        info_label = Ctk.CLabel(master=self.UserInterface, bg='gray12', size=(260, 37),
                                text=self.language.refactor('Pix Level: '), fg='white', font=('Helvetica', 16),
                                corner='rounded', anchor='NW', text_place=(5, 8))
        info_label.place(*place0)

        level_label = Ctk.CLabel(master=self.UserInterface, bg=self.UserInterface['background'], size=(170, 37),
                                 text='Level: ' + str(level), fg='white', font=('Helvetica', 20), corner='angular',
                                 anchor='NW', text_place=(5, 2))
        level_label.place(*place1)

    def _create_logo_image(self, place):
        """

        :param place: place for the PixelBoy logo
        :return:      place the PixelBoy Logo on the new_user_interface
        """
        self.logo_canvas = Ctk.CCanvas(self.UserInterface, bg=self.UserInterface['background'], size=(108, 22),
                                       corners='rounded')
        self.logo_canvas.create_image(corner='angular', width=106, height=20, pos=(54, 11),
                                      image_path='images/logo.png',
                                      transparent=True)
        self.logo_canvas.place(*place)

    def _create_arrow(self, place):
        """

        :param place: place for the arrow on the widget
        :return:      -> Place the arrow image (png) on the given place
        """
        self.logo_canvas = Ctk.CCanvas(self.UserInterface, bg=self.UserInterface['background'], size=(108, 22),
                                       corners='angular')
        self.logo_canvas.create_image(corner='angular', width=70, height=60, pos=(54, 11),
                                      image_path='images/arrow.png',
                                      transparent=True)
        self.logo_canvas.place(*place)

    def _create_number_of_creations_label(self, creations, place0, place1):
        """

        :param creations: number of creations from the current user
        :param place0:    place for the info Label (Number of Creations: )
        :param place1:    place for the Creations Label
        :return:          -> Place the Ctk Objects on the Widget
        """
        self._create_arrow((place1[0] - 90, place1[1] + 8))
        info_label = Ctk.CLabel(master=self.UserInterface, bg='gray12', size=(260, 37),
                                text=self.language.refactor('Number of Creations: '), fg='white',
                                font=('Helvetica', 16), corner='rounded', anchor='NW', text_place=(5, 8))
        info_label.place(*place0)

        level_label = Ctk.CLabel(master=self.UserInterface, bg=self.UserInterface['background'], size=(200, 37),
                                 text=self.language.refactor('Creations: ') + str(creations), fg='white',
                                 font=('Helvetica', 20), corner='angular', anchor='NW', text_place=(5, 2))
        level_label.place(*place1)


def main():
    """

        -> Just to test the function and classes of this library

    """
    root = tk.Tk()
    root.config(bg='gray40')
    root.geometry('800x400')
    # OpenUser('Christof', lambda: print('Hallo'), 'german')
    inter = User_Interface(root, 'Christof')
    inter.UserInterface.place(x=10, y=10)

    root.mainloop()


if __name__ == '__main__':
    main()
