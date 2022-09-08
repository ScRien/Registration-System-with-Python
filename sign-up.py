username = input("Bir Kullanıcı Adı Giriniz: ")
password = input("Bir Şifre Giriniz: ")
if username != "" or password != "":
    if len(username) < 4 or len(username) > 24:
        print("Lütfen Minimum 4 Maksimum 24 Karakterli bir kullanıcı adı giriniz!")
    elif int(len(password)) < 8 or int(len(password)) > 26:
        print("Lütfen Minimum 8 Maksimum 26 Karakterli bir şifre giriniz!")
    else: print("Başarıyla Kayıt oldunuz! Şimdi giriş yapacaksınız!")
    LoginUsername = input("Kullanıcı Adınızı Giriniz: ")
    LoginPassword = input("Şifrenizi Giriniz: ")
    if LoginUsername != username or LoginPassword != password:
        print("Hatalı Giriş!")
    else: print("Giriş Yapıldı!")
else:print("Lütfen Gerekli Alanları Doldurun!")