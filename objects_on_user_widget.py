"""

    Library with classes for the User Widget Objects like add new user button and available user icons

"""
import function_user_widget
from lib import languages
import Ctkinter as Ctk
import tkinter as tk
import shutil


__author__ = 'Christof Haidegger'
__date__ = '20.07.2021'
__completed__ = '--.--.----'
__work_time__ = 'about -- hours'
__version__ = '1.0'
__licence__ = 'opensource(common licenced)'


class New_user:
    """

        -> Class to create a icon to add new User for the Game Frame

    """
    def __init__(self, master, func, language='english'):
        """

        :param master: -> where the new User icon should be placed
        :param func:   -> function which should be run, when the New User Button is pressed
        """
        __BACKGROUND__ = 'gray20'
        __OUTLINE__ = ('white', 1.5)
        __SIZE__ = (180, 190)
        __CORNERS__ = 'rounded'
        __MAX_RAD__ = 30
        __PRESSING_COLOR__ = 'gray12'
        __HIGH_COLOR__ = 'gray50'
        __DASH__ = (15, 1)
        self.language = languages.Language('languages/languages.txt', language=language)

        self.new_user = Ctk.CButton(master, bg=__BACKGROUND__, highlight_color=__HIGH_COLOR__,
                                    pressing_color=__PRESSING_COLOR__, width=__SIZE__[0], height=__SIZE__[1],
                                    text=None, outline=__OUTLINE__, rounded_corners=__CORNERS__,
                                    command=func, max_rad=__MAX_RAD__, dash=__DASH__)

        # run functions
        self._info_labels(place0=(90, 40), place1=(90, 120))  # add_label -> place0, plus_label -> place1

    def _info_labels(self, place0, place1):
        """

        :param place0: place for the Add User Label
        :param place1: place for the + icon
        :return: place the labels on the new User Widget
        """
        self.new_user.get_canvas().create_text(place0[0], place0[1], fill='white', font=('Helvetica', 15),
                                               text=self.language.refactor('Add User'))

        self.new_user.get_canvas().create_text(place1[0], place1[1], fill='white', font=('Courier', 100),
                                               text='+')


class Open_user:
    """

        -> Class to open the actually user name with all functions that are needed

    """
    def __init__(self, master, func, user_name, language='english'):
        """

        :param master:    master where it should be placed
        :param func:      function which should be run, when the user icon is pressed
        :param user_name: name of the user which should be opened
        :param language:  language for the user -> default is english
        """
        __BACKGROUND__ = 'gray20'
        __OUTLINE__ = ('white', 1.5)
        __SIZE__ = (180, 190)
        __CORNERS__ = 'rounded'
        __MAX_RAD__ = 30
        __PRESSING_COLOR__ = 'gray12'
        __HIGH_COLOR__ = 'gray50'

        self.__USER_PATH__ = 'Users'

        self.language = languages.Language('languages/languages.txt', language=language)

        self.open_user = Ctk.CButton(master, bg=__BACKGROUND__, highlight_color=__HIGH_COLOR__,
                                     pressing_color=__PRESSING_COLOR__, width=__SIZE__[0], height=__SIZE__[1],
                                     text=None, outline=__OUTLINE__, rounded_corners=__CORNERS__,
                                     command=lambda: function_user_widget.
                                     OpenUser(user_name=user_name, language=language, func=func), max_rad=__MAX_RAD__)

        # run functions
        self._items_on_open_user_object(user_name=user_name)

    def _items_on_open_user_object(self, user_name):
        """

        :param user_name: user name from __init__
        :return:          draw the items on the open user widget
        """
        self._create_user_icon(user_name=user_name)
        self._create_user_name(user_name=user_name)
        self._create_delete_button(place=(150, 10), user_name=user_name)

    def _create_delete_button(self, place, user_name):
        """

        :param place:     place for the delete button
        :param user_name: user name which should be deleted when it is pressed
        :return:          draw the delete button on the given place
        """
        delete_button = Ctk.CButton(self.open_user, bg=None,
                                    highlight_color='gray50',
                                    pressing_color='gray50', width=20, height=20,
                                    text=None, courser="pirate", rounded_corners='angular',
                                    image=('images/trash.png', 'angular', (11, 10), (20, 20)),
                                    command=lambda: self._delete_user(user_name))
        self.open_user.set_button_atributes(delete_button.get_canvas(), delete_button.polygon, set_command=False)
        delete_button.place(*place)

    def _delete_user(self, user_name):
        """

        :param user_name: user which is to delete
        :return:          delete the user from the /Users Folder and All_users.txt file
        """
        self.open_user.destroy()
        shutil.rmtree('Users/' + str(user_name))
        all_users_file = open(self.__USER_PATH__ + '/All_Users.txt', 'r')
        users = all_users_file.read().split('\n')
        all_users_file.close()
        users.remove(user_name)
        all_users_file = open(self.__USER_PATH__ + '/All_Users.txt', 'w')
        for user in users:
            if user == '':
                continue
            all_users_file.write(user + '\n')
        all_users_file.close()

    def _create_user_icon(self, user_name, place=(30, 50)):
        """

        :param user_name: name of the user
        :param place:     place for the icon
        :return:          place the icon on the given place
        """
        user_icon_path = self.__USER_PATH__ + '/' + user_name + '/profile.gif'
        user_icon_canvas = Ctk.CCanvas(self.open_user, corners='angular', size=(120, 120),
                                       bg=self.open_user['background'])

        self.open_user.set_button_atributes(user_icon_canvas.get_canvas(), user_icon_canvas.outline)
        user_icon_canvas.create_gif(gif_path=user_icon_path, corner='round', size=(118, 118), pos=(59, 59),
                                    transparent=True, speed='normal')
        user_icon_canvas.place(*place)

    def _create_user_name(self, user_name, place=(5, 8)):
        """

        :param user_name: name of the user
        :param place:     place for the user name on the icon
        :return:          place the user name on the open user widget
        """
        user_name_label = Ctk.CLabel(self.open_user, bg=self.open_user['background'], size=(170, 30), text=user_name,
                                     fg='white', font=('Helvetica', 14), anchor='CENTRE', corner='angular')
        self.open_user.set_button_atributes(user_name_label.get_canvas(), user_name_label.CLabel.outline)
        user_name_label.place(*place)


def create_user_widget(master, place, user_name):
    """

        -> Note: This function is may only a demonstration and not really need in outer scope

    :param user_name: User Name for the User Widget
    :param master: master to place the User widget
    :param place:  place to place on the master widget
    :return:       -> Place the User widget on the master
    """

    user_widget = function_user_widget.User_Interface(master, user_name, language='german')
    user_widget.UserInterface.place(*place)


def main():
    """

        -> Just to test the function and classes of this library

    """
    root = tk.Tk()
    root.config(bg='gray40')
    root.geometry('1200x600')

    new_user = New_user(root, lambda: function_user_widget.CreateNewUser(language='german'), language='german')
    new_user.new_user.place(x=40, y=40)

    open_user = Open_user(root, lambda: create_user_widget(root, (650, 250), 'Christof'),
                          user_name='Christof', language='german')
    open_user.open_user.place(x=240, y=40)

    open_user = Open_user(root, lambda: create_user_widget(root, (650, 250), 'Elias'),
                          user_name='Elias', language='german')
    open_user.open_user.place(x=440, y=40)

    open_user = Open_user(root, lambda: create_user_widget(root, (650, 250), 'Simon'),
                          user_name='Simon', language='german')
    open_user.open_user.place(x=640, y=40)

    open_user = Open_user(root, lambda: create_user_widget(root, (650, 250), 'Andreas'),
                          user_name='Andreas', language='german')
    open_user.open_user.place(x=240, y=260)

    open_user = Open_user(root, lambda: create_user_widget(root, (650, 250), 'Nik'),
                          user_name='Nik', language='english')
    open_user.open_user.place(x=440, y=260)

    root.mainloop()


if __name__ == '__main__':
    main()
