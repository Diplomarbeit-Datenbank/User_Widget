# User_Widget

![image](https://user-images.githubusercontent.com/87471423/127841002-8bb174af-5eb8-4237-9c44-9c60aed3e5b4.png)

Ein Widget zum erstellen, oder auch einloggen eines Benutzers


# Aussehen:

 ## Erstellen eines Benutzers:
   ![image](https://user-images.githubusercontent.com/87471423/127814651-79c1358d-9921-4a16-802f-f3be4e330a03.png)

   
## Einloggen eines bestehenden Benutzers:
   ![image](https://user-images.githubusercontent.com/87471423/127816383-ecfd7441-5390-4399-8a98-3ff4f4d4c2e9.png)


## Benutzerprofil im eingeloggten Zustand
   ![image](https://user-images.githubusercontent.com/87471423/127816695-ec5c67aa-684b-41b6-b1d5-8b882f49afd9.png)


## Löschen eines bestehenden Benutzers:
   ![image](https://user-images.githubusercontent.com/87471423/127817146-5b4c6352-18bc-4dd1-a61d-3ad103d72bf2.png)


# Funktionen:
    o Erstellen von Benutzern
    o Einfache Platzierung der einzelnen Objekte wie zum Beispiel Benutzer Fenster
    o Löschen eines bestehenden Benutzers
    o Einloggen eines bestehenden Benutzers
    o Passwort Schutz für Benutzer, wenn gewünscht
    o Personalisierung durch einstellen eigener GIF Animationen als Profilbild


# Benötigte Librarys:
    o PILLOW:    -> Download via pip install PILLOW
                 -> Benötigt für die Bildanzeigen (GIFS) am tkinter Fenster
    o tkinter:   -> Für die Erzeugung der Interfaces
                 -> tkinter wird ebenso für Ctkinter benötigt
    o Ctkinter:  -> Für die Objekte am Interface
                 -> Erzeugung von runden Kanten und anzeigen, abspielen von GIFS 
    o languages: -> Für die Darstellung des Widgets in mehreren Sprachen
                 -> Beschreibung unter folgendem Link:
    o opencv:    -> Für die Bildbearbeitung
                 -> Abspielen der GIFS am Interface
    o shutil:    -> Verschieben und kopieren von Daten
                 -> Verschieben des Profilbildes in eigenem angelegten Ordner

   
  # Verwendung:
     o Durch anschauen der obigen Bilder ist gut ersichtlich, wie sich das User Widget als Benutzer verwenden lässt.
     o Für Entwickler gilt es sich die main im File objects_on_user_widget anzusehen, um zu verstehen, wie man die 
       einzelnen Objekte platziert
       
    Main:
    
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






