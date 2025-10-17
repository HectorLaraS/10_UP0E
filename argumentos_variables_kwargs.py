def contacto_usuario(nombre: str, *args, **kwargs):
    print(f"Nombre: {nombre}, {args} Contact:{kwargs}")
    if "mail" in kwargs:
        print(f"mail: {kwargs.get("mail")}")
    if "phone" in kwargs:
        print(f"phone: {kwargs.get("phone")}")


contacto_usuario("Hector Lara", "Ingeniero", "Information Service"
                 , mail="hectorlaras.18@gmail.com", phone="8140207393")
