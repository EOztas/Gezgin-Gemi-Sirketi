from tkinter import ttk
import tkinter
from tkinter import messagebox
import sqlite3


class ContainerShipInfoForm: # Konteyner gemi bilgileri formunu oluşturan sınıf
    def __init__(self, notebook):
        self.frame = tkinter.Frame(notebook) # Form için bir çerçeve oluşturur
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Konteyner gemisi bilgileri için etiketli bir çerçeve oluşturur
        self.ship_info_frame = tkinter.LabelFrame(self.frame, text="Container Ship Information")
        self.ship_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Çeşitli gemi özellikleri için etiketler ve giriş alanları oluşturur
        # Her bir etiket-giriş alanı çifti için bir etiket ve bir giriş alanı oluşturur
        self.serial_number_label = tkinter.Label(self.ship_info_frame, text="Serial Number")
        self.serial_number_entry = tkinter.Entry(self.ship_info_frame)
        self.serial_number_label.grid(row=0, column=0)
        self.serial_number_entry.grid(row=0, column=1)

        self.name_label = tkinter.Label(self.ship_info_frame, text="Name")
        self.name_entry = tkinter.Entry(self.ship_info_frame)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        self.weight_label = tkinter.Label(self.ship_info_frame, text="Weight")
        self.weight_entry = tkinter.Entry(self.ship_info_frame)
        self.weight_label.grid(row=2, column=0)
        self.weight_entry.grid(row=2, column=1)

        self.year_built_label = tkinter.Label(self.ship_info_frame, text="Year Built")
        self.year_built_entry = tkinter.Entry(self.ship_info_frame)
        self.year_built_label.grid(row=3, column=0)
        self.year_built_entry.grid(row=3, column=1)

        self.container_capacity_label = tkinter.Label(self.ship_info_frame, text="Container Capacity")
        self.container_capacity_entry = tkinter.Entry(self.ship_info_frame)
        self.container_capacity_label.grid(row=4, column=0)
        self.container_capacity_entry.grid(row=4, column=1)

        self.max_weight_label = tkinter.Label(self.ship_info_frame, text="Max Weight")
        self.max_weight_entry = tkinter.Entry(self.ship_info_frame)
        self.max_weight_label.grid(row=5, column=0)
        self.max_weight_entry.grid(row=5, column=1)
        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.ship_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=1, column=0, sticky="news", padx=20, pady=10)
        # Form çerçevesi, not defterine eklenir ve "Konteyner Gemi Bilgileri" sekmesi altında gösterilir
        notebook.add(self.frame, text="Container Ship Information")

    # Veri girişi fonksiyonu
    def enter_data(self):
        # Gerekli tüm veriler alınır
        serial_number = self.serial_number_entry.get()
        name = self.name_entry.get()
        weight = self.weight_entry.get()
        year_built = self.year_built_entry.get()
        container_capacity = self.container_capacity_entry.get()
        max_weight = self.max_weight_entry.get()
        # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
        if serial_number and name and weight and year_built and container_capacity and max_weight:
            print("Serial Number:", serial_number)
            print("Name:", name)
            print("Weight:", weight)
            print("Year Built:", year_built)
            print("Container Capacity:", container_capacity)
            print("Max Weight:", max_weight)
            print("------------------------------------------")

            conn = sqlite3.connect('data.db') # Veritabanına bağlanır
            # Tablo oluşturulması için sorgu
            table_create_query = '''CREATE TABLE IF NOT EXISTS Conteiner_ship_data 
                                (serial_number INT, name TEXT, weight INT, year_built INT, container_capacity TEXT, 
                                max_weight INT)
                        '''
            conn.execute(table_create_query)
            # Veri ekleme sorgusu ve değerleri
            data_insert_query = '''INSERT INTO Conteiner_ship_data (serial_number, name, 
                                weight, year_built, container_capacity, max_weight) VALUES 
                                (?, ?, ?, ?, ?, ?)'''
            # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
            data_insert_tuple = (serial_number, name, weight,
                                 year_built, container_capacity, max_weight)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
            conn.commit() # Veritabanı değişikliklerini kaydeder
            conn.close()  # Veritabanı bağlantısını kapatır

            conn.close()

        # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        serial_number = self.serial_number_entry.get() # Seri numarası alınır
        # Seri numarası var ise veritabanına bağlanır
        if serial_number:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen seri numarasına sahip kayıt silinir
            cursor.execute("DELETE FROM Conteiner_ship_data WHERE serial_number=?", (serial_number,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer seri numarası girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter a Serial Number to delete.")

class PetrolTankerForm: # Petrol tankeri formunu oluşturan sınıf
    def __init__(self, notebook):
        self.frame = tkinter.Frame(notebook) # Form için bir çerçeve oluşturur
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Petrol tankeri bilgileri için etiketli bir çerçeve oluşturur
        self.ship_info_frame = tkinter.LabelFrame(self.frame, text="Petrol Tanker Information")
        self.ship_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Petrol tanker bilgileri giriş alanları ve etiketleri
        self.serial_number_label = tkinter.Label(self.ship_info_frame, text="Serial Number")
        self.serial_number_entry = tkinter.Entry(self.ship_info_frame)
        self.serial_number_label.grid(row=0, column=0)
        self.serial_number_entry.grid(row=0, column=1)

        self.name_label = tkinter.Label(self.ship_info_frame, text="Name")
        self.name_entry = tkinter.Entry(self.ship_info_frame)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        self.weight_label = tkinter.Label(self.ship_info_frame, text="Weight")
        self.weight_entry = tkinter.Entry(self.ship_info_frame)
        self.weight_label.grid(row=2, column=0)
        self.weight_entry.grid(row=2, column=1)

        self.year_built_label = tkinter.Label(self.ship_info_frame, text="Year Built")
        self.year_built_entry = tkinter.Entry(self.ship_info_frame)
        self.year_built_label.grid(row=3, column=0)
        self.year_built_entry.grid(row=3, column=1)

        self.petrol_capacity_label = tkinter.Label(self.ship_info_frame, text="Petrol Capacity")
        self.petrol_capacity_entry = tkinter.Entry(self.ship_info_frame)
        self.petrol_capacity_label.grid(row=4, column=0)
        self.petrol_capacity_entry.grid(row=4, column=1)

        self.max_weight_label = tkinter.Label(self.ship_info_frame, text="Max Weight")
        self.max_weight_entry = tkinter.Entry(self.ship_info_frame)
        self.max_weight_label.grid(row=5, column=0)
        self.max_weight_entry.grid(row=5, column=1)

        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.ship_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=1, column=0, sticky="news", padx=20, pady=10)
        # Form çerçevesi, not defterine eklenir ve "Petrol Tanker Bilgileri" sekmesi altında gösterilir
        notebook.add(self.frame, text="Petrol Tanker Information")

    # Veri girişi fonksiyonu
    def enter_data(self):
        # Gerekli tüm veriler alınır
        serial_number = self.serial_number_entry.get()
        name = self.name_entry.get()
        weight = self.weight_entry.get()
        year_built = self.year_built_entry.get()
        petrol_capacity = self.petrol_capacity_entry.get()
        max_weight = self.max_weight_entry.get()
        # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
        if serial_number and name and weight and year_built and petrol_capacity and max_weight:
            print("Serial Number:", serial_number)
            print("Name:", name)
            print("Weight:", weight)
            print("Year Built:", year_built)
            print("Petrol Capacity:", petrol_capacity)
            print("Max Weight:", max_weight)
            print("------------------------------------------")

            conn = sqlite3.connect('data.db') # Veritabanına bağlanır
            # Tablo oluşturulması için sorgu
            table_create_query = '''CREATE TABLE IF NOT EXISTS Petrol_ship_data 
                                            (serial_number INT, name TEXT, weight INT, year_built INT, petrol_capacity TEXT, 
                                            max_weight INT)
                                    '''
            conn.execute(table_create_query)
            # Veri ekleme sorgusu ve değerleri
            data_insert_query = '''INSERT INTO Petrol_ship_data (serial_number, name, 
                                            weight, year_built, petrol_capacity, max_weight) VALUES 
                                            (?, ?, ?, ?, ?, ?)'''
            # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
            data_insert_tuple = (serial_number, name, weight,
                                 year_built, petrol_capacity, max_weight)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
            conn.commit() # Veritabanı değişikliklerini kaydeder
            conn.close()  # Veritabanı bağlantısını kapatır

            conn.close()

        # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        serial_number = self.serial_number_entry.get() # Seri numarası alınır
        # Seri numarası var ise veritabanına bağlanır
        if serial_number:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen seri numarasına sahip kayıt silinir
            cursor.execute("DELETE FROM Petrol_ship_data WHERE serial_number=?", (serial_number,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer seri numarası girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter a Serial Number to delete.")

class PassengerShipForm: # Yolcu gemisi bilgileri formunu oluşturan sınıf
    def __init__(self, notebook):
        self.frame = tkinter.Frame(notebook) # Form için bir çerçeve oluşturur
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Yolcu gemisi bilgileri için etiketli bir çerçeve oluşturur
        self.ship_info_frame = tkinter.LabelFrame(self.frame, text="Passenger Ship Information")
        self.ship_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Yolcu gemisi bilgileri giriş alanları ve etiketleri
        self.serial_number_label = tkinter.Label(self.ship_info_frame, text="Serial Number")
        self.serial_number_entry = tkinter.Entry(self.ship_info_frame)
        self.serial_number_label.grid(row=0, column=0)
        self.serial_number_entry.grid(row=0, column=1)

        self.name_label = tkinter.Label(self.ship_info_frame, text="Name")
        self.name_entry = tkinter.Entry(self.ship_info_frame)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        self.weight_label = tkinter.Label(self.ship_info_frame, text="Weight")
        self.weight_entry = tkinter.Entry(self.ship_info_frame)
        self.weight_label.grid(row=2, column=0)
        self.weight_entry.grid(row=2, column=1)

        self.year_built_label = tkinter.Label(self.ship_info_frame, text="Year Built")
        self.year_built_entry = tkinter.Entry(self.ship_info_frame)
        self.year_built_label.grid(row=3, column=0)
        self.year_built_entry.grid(row=3, column=1)

        self.passenger_capacity_label = tkinter.Label(self.ship_info_frame, text="Passenger Capacity")
        self.passenger_capacity_entry = tkinter.Entry(self.ship_info_frame)
        self.passenger_capacity_label.grid(row=4, column=0)
        self.passenger_capacity_entry.grid(row=4, column=1)
        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.ship_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=1, column=0, sticky="news", padx=20, pady=10)
        # Form çerçevesi, not defterine eklenir ve "Yolcu Gemisi" sekmesi altında gösterilir
        notebook.add(self.frame,text="Passenger Ship")


    # Veri girişi fonksiyonu
    def enter_data(self):
        # Gerekli tüm veriler alınır
        serial_number = self.serial_number_entry.get()
        name = self.name_entry.get()
        weight = self.weight_entry.get()
        year_built = self.year_built_entry.get()
        passenger_capacity = self.passenger_capacity_entry.get()
        # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
        if serial_number and name and weight and year_built and passenger_capacity:
            print("Serial Number:", serial_number)
            print("Name:", name)
            print("Weight:", weight)
            print("Year Built:", year_built)
            print("Passenger Capacity:", passenger_capacity)
            print("------------------------------------------")

            conn = sqlite3.connect('data.db') # Veritabanına bağlanır
            # Tablo oluşturulması için sorgu
            table_create_query = '''CREATE TABLE IF NOT EXISTS Passanger_ship_data 
                                                        (serial_number INT, name TEXT, weight INT, year_built INT, passenger_capacity INT)
                                                '''
            conn.execute(table_create_query)
            # Veri ekleme sorgusu ve değerleri
            data_insert_query = '''INSERT INTO Passanger_ship_data (serial_number, name, 
                                                        weight, year_built, passenger_capacity) VALUES 
                                                        (?, ?, ?, ?, ?)'''
            # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
            data_insert_tuple = (serial_number, name, weight,
                                 year_built, passenger_capacity)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
            conn.commit() # Veritabanı değişikliklerini kaydeder
            conn.close()  # Veritabanı bağlantısını kapatır

            conn.close()
        # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        serial_number = self.serial_number_entry.get() # Seri numarası alınır
        # Seri numarası var ise veritabanına bağlanır
        if serial_number:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen seri numarasına sahip kayıt silinir
            cursor.execute("DELETE FROM Passanger_ship_data WHERE serial_number=?", (serial_number,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer seri numarası girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter a Serial Number to delete.")

class PortInfoForm:  # Liman bilgileri formunu oluşturan sınıf
    def __init__(self, master):
        self.master = master
        # Ana çerçeve oluşturulur ve ana pencereye yerleştirilir
        self.frame = tkinter.Frame(master)
        self.frame.pack()
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Liman bilgileri için etiketli bir çerçeve oluşturur
        self.port_info_frame = tkinter.LabelFrame(self.frame, text="Port Information")
        self.port_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Liman bilgileri giriş alanları ve etiketleri
        self.port_name_label = tkinter.Label(self.port_info_frame, text="Port Name")
        self.port_name_entry = tkinter.Entry(self.port_info_frame)
        self.port_name_label.grid(row=0, column=0)
        self.port_name_entry.grid(row=0, column=1)

        self.country_label = tkinter.Label(self.port_info_frame, text="Country")
        self.country_entry = tkinter.Entry(self.port_info_frame)
        self.country_label.grid(row=1, column=0)
        self.country_entry.grid(row=1, column=1)

        self.population_label = tkinter.Label(self.port_info_frame, text="Population")
        self.population_entry = tkinter.Entry(self.port_info_frame)
        self.population_label.grid(row=2, column=0)
        self.population_entry.grid(row=2, column=1)

        self.requires_passport_label = tkinter.Label(self.port_info_frame, text="Requires Passport")
        self.requires_passport_var = tkinter.BooleanVar()
        self.requires_passport_check = tkinter.Checkbutton(self.port_info_frame, text="Yes",
                                                           variable=self.requires_passport_var)
        self.requires_passport_label.grid(row=3, column=0)
        self.requires_passport_check.grid(row=3, column=1)

        self.docking_fee_label = tkinter.Label(self.port_info_frame, text="Docking Fee")
        self.docking_fee_entry = tkinter.Entry(self.port_info_frame)
        self.docking_fee_label.grid(row=4, column=0)
        self.docking_fee_entry.grid(row=4, column=1)
        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.port_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=1, column=0, sticky="news", padx=20, pady=10)



    # Veri girişi fonksiyonu
    def enter_data(self):
        # Gerekli tüm veriler alınır
        port_name = self.port_name_entry.get()
        country = self.country_entry.get()
        population = self.population_entry.get()
        requires_passport = "Yes" if self.requires_passport_var.get() else "No"
        docking_fee = self.docking_fee_entry.get()
        # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
        if port_name and country and population and docking_fee:
            print("Port Name:", port_name)
            print("Country:", country)
            print("Population:", population)
            print("Requires Passport:", requires_passport)
            print("Docking Fee:", docking_fee)
            print("------------------------------------------")

            conn = sqlite3.connect('data.db') # Veritabanına bağlanır
            # Tablo oluşturulması için sorgu
            table_create_query = '''CREATE TABLE IF NOT EXISTS Port_Information_data 
                                                                    (port_name TEXT, country TEXT, population INT, requires_passport TEXT, docking_fee INT)
                                                            '''
            conn.execute(table_create_query)
            # Veri ekleme sorgusu ve değerleri
            data_insert_query = '''INSERT INTO Port_Information_data (port_name, country, 
                                                                    population, requires_passport, docking_fee) VALUES 
                                                                    (?, ?, ?, ?, ?)'''
            # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
            data_insert_tuple = (port_name, country, population,
                                 requires_passport, docking_fee)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
            conn.commit() # Veritabanı değişikliklerini kaydeder
            conn.close() # Veritabanı bağlantısını kapatır

            conn.close()
        # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        port_name = self.port_name_entry.get() # Liman adı alınır
        # Liman adı boş değil ise veritabanına bağlanır
        if port_name:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen liman adına sahip kayıt silinir
            cursor.execute("DELETE FROM Port_Information_data WHERE port_name=?", (port_name,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer Liman adı girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter a Port Name to delete.")

class ShipVoyageForm: # Gemi seferi bilgileri formunu oluşturan sınıf
    def __init__(self, master):
        self.master = master

        # Ana çerçeve oluşturulur ve ana pencereye yerleştirilir
        self.frame = tkinter.Frame(master)
        self.frame.pack()
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Sefer bilgileri için etiketli bir çerçeve oluşturur
        self.user_info_frame = tkinter.LabelFrame(self.frame, text="Voyage Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Gemi seferi bilgileri giriş alanları ve etiketleri
        self.id_label = tkinter.Label(self.user_info_frame, text="ID Number")
        self.id_entry = tkinter.Entry(self.user_info_frame)
        self.id_label.grid(row=0, column=0)
        self.id_entry.grid(row=0, column=1)

        self.departure_date_label = tkinter.Label(self.user_info_frame, text="Departure Date")
        self.departure_date_entry = tkinter.Entry(self.user_info_frame)
        self.departure_date_label.grid(row=1, column=0)
        self.departure_date_entry.grid(row=1, column=1)

        self.return_date_label = tkinter.Label(self.user_info_frame, text="Return Date")
        self.return_date_entry = tkinter.Entry(self.user_info_frame)
        self.return_date_label.grid(row=2, column=0)
        self.return_date_entry.grid(row=2, column=1)

        self.departure_port_label = tkinter.Label(self.user_info_frame, text="Departure Port")
        self.departure_port_entry = tkinter.Entry(self.user_info_frame)
        self.departure_port_label.grid(row=3, column=0)
        self.departure_port_entry.grid(row=3, column=1)
        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    # Veri girişi fonksiyonu
    def enter_data(self):
        # Gerekli tüm veriler alınır
        id_number = self.id_entry.get()
        departure_date = self.departure_date_entry.get()
        return_date = self.return_date_entry.get()
        departure_port = self.departure_port_entry.get()
        # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
        if id_number and departure_date and return_date and departure_port:
            print("ID Number:", id_number)
            print("Departure Date:", departure_date)
            print("Return Date:", return_date)
            print("Departure Port:", departure_port)
            print("------------------------------------------")

            conn = sqlite3.connect('data.db')  # Veritabanına bağlanır
            # Tablo oluşturulması için sorgu
            table_create_query = '''CREATE TABLE IF NOT EXISTS Voyage_Information_data 
                                                                                (id_number INT, departure_date INT, return_date INT, departure_port TEXT)
                                                                        '''
            conn.execute(table_create_query)
            # Veri ekleme sorgusu ve değerleri
            data_insert_query = '''INSERT INTO Voyage_Information_data (id_number, departure_date, 
                                                                                return_date, departure_port) VALUES 
                                                                                (?, ?, ?, ?)'''
            # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
            data_insert_tuple = (id_number, departure_date, return_date,
                                 departure_port)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
            conn.commit() # Veritabanı değişikliklerini kaydeder
            conn.close() # Veritabanı bağlantısını kapatır

            conn.close()
        # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        id_number = self.id_entry.get() # Kimlik numarası alınır
        # Kimlik numarası var ise veritabanına bağlanır
        if id_number:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen kimlik numarasına sahip kayıt silinir
            cursor.execute("DELETE FROM Voyage_Information_data WHERE id_number=?", (id_number,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer kimlik numarası girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter an ID Number to delete.")

class CaptainForm: # Kaptan bilgileri formunu oluşturan sınıf
    def __init__(self, master):
        self.master = master
        # Ana çerçeve oluşturulur ve ana pencereye yerleştirilir
        self.frame = tkinter.Frame(master)
        self.frame.pack()
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Kaptan bilgileri için etiketli bir çerçeve oluşturur
        self.user_info_frame = tkinter.LabelFrame(self.frame, text="Captain Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Kaptan bilgileri giriş alanları ve etiketleri
        self.id_label = tkinter.Label(self.user_info_frame, text="ID Number")
        self.id_entry = tkinter.Entry(self.user_info_frame)
        self.id_label.grid(row=0, column=0)
        self.id_entry.grid(row=0, column=1)

        self.first_name_label = tkinter.Label(self.user_info_frame, text="First Name")
        self.first_name_entry = tkinter.Entry(self.user_info_frame)
        self.first_name_label.grid(row=1, column=0)
        self.first_name_entry.grid(row=1, column=1)

        self.last_name_label = tkinter.Label(self.user_info_frame, text="Last Name")
        self.last_name_entry = tkinter.Entry(self.user_info_frame)
        self.last_name_label.grid(row=2, column=0)
        self.last_name_entry.grid(row=2, column=1)

        self.birthdate_label = tkinter.Label(self.user_info_frame, text="Birthdate")
        self.birthdate_entry = tkinter.Entry(self.user_info_frame)
        self.birthdate_label.grid(row=3, column=0)
        self.birthdate_entry.grid(row=3, column=1)

        self.nationality_label = tkinter.Label(self.user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(self.user_info_frame,
                                                 values=["Africa", "Antarctica", "Asia", "Europe", "North America",
                                                         "Oceania", "South America"])
        self.nationality_label.grid(row=4, column=0)
        self.nationality_combobox.grid(row=4, column=1)

        self.start_date_label = tkinter.Label(self.user_info_frame, text="Start Date")
        self.start_date_entry = tkinter.Entry(self.user_info_frame)
        self.start_date_label.grid(row=5, column=0)
        self.start_date_entry.grid(row=5, column=1)

        self.license_label = tkinter.Label(self.user_info_frame, text="Captain's License")
        self.license_var = tkinter.BooleanVar()
        self.license_check = tkinter.Checkbutton(self.user_info_frame, text="Yes", variable=self.license_var)
        self.license_label.grid(row=6, column=0)
        self.license_check.grid(row=6, column=1)
        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır

        self.terms_frame = tkinter.LabelFrame(self.frame, text="Terms & Conditions")
        self.terms_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = tkinter.Checkbutton(self.terms_frame, text="I accept the terms and conditions.",
                                               variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=0, column=0)
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Veri girişi fonksiyonu
    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            # Gerekli tüm veriler alınır
            id_number = self.id_entry.get()
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            birthdate = self.birthdate_entry.get()
            nationality = self.nationality_combobox.get()
            start_date = self.start_date_entry.get()
            has_license = "Yes" if self.license_var.get() else "No"
            # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
            if id_number and firstname and lastname and birthdate and nationality and start_date:
                print("ID Number:", id_number)
                print("First name:", firstname)
                print("Last name:", lastname)
                print("Birthdate:", birthdate)
                print("Nationality:", nationality)
                print("Start Date:", start_date)
                print("Captain's License:", has_license)
                print("------------------------------------------")

                conn = sqlite3.connect('data.db') # Veritabanına bağlanır
                # Tablo oluşturulması için sorgu
                table_create_query = '''CREATE TABLE IF NOT EXISTS Captain_Information_data 
                                                                                                (id_number INT, firstname TEXT, lastname TEXT, birthdate INT, nationality TEXT, start_date INT, has_license TEXT)
                                                                                        '''
                conn.execute(table_create_query)
                # Veri ekleme sorgusu ve değerleri
                data_insert_query = '''INSERT INTO Captain_Information_data (id_number, firstname, 
                                                                                                lastname, birthdate, nationality, start_date, has_license) VALUES 
                                                                                                (?, ?, ?, ?, ?, ?, ?)'''
                # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
                data_insert_tuple = (id_number, firstname, lastname,
                                     birthdate, nationality, start_date, has_license)

                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
                conn.commit() # Veritabanı değişikliklerini kaydeder
                conn.close() # Veritabanı bağlantısını kapatır

                conn.close()

            # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
            else:
                tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")
        # Eğer kullanıcı şartları kabul etmediyse uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        id_number = self.id_entry.get() # Kimlik numarası alınır
        # Kimlik numarası var ise veritabanına bağlanır
        if id_number:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen kimlik numarasına sahip kayıt silinir
            cursor.execute("DELETE FROM Captain_Information_data WHERE id_number=?", (id_number,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer kimlik numarası girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter an ID Number to delete.")

class CrewForm: # Mürettebat bilgileri formunu oluşturan sınıf
    def __init__(self, master):
        self.master = master
        # Ana çerçeve oluşturulur ve ana pencereye yerleştirilir
        self.frame = tkinter.Frame(master)
        self.frame.pack()
        # Veri silme işlemini gerçekleyebilmek için bir buton oluşturur
        self.delete_button = tkinter.Button(self.frame, text="Delete data", command=self.delete_data)
        self.delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        # Mürettebat bilgileri için etiketli bir çerçeve oluşturur
        self.user_info_frame = tkinter.LabelFrame(self.frame, text="Crew Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        # Mürettebat bilgileri giriş alanları ve etiketleri
        self.id_label = tkinter.Label(self.user_info_frame, text="ID Number")
        self.id_entry = tkinter.Entry(self.user_info_frame)
        self.id_label.grid(row=0, column=0)
        self.id_entry.grid(row=0, column=1)

        self.first_name_label = tkinter.Label(self.user_info_frame, text="First Name")
        self.first_name_entry = tkinter.Entry(self.user_info_frame)
        self.first_name_label.grid(row=1, column=0)
        self.first_name_entry.grid(row=1, column=1)

        self.last_name_label = tkinter.Label(self.user_info_frame, text="Last Name")
        self.last_name_entry = tkinter.Entry(self.user_info_frame)
        self.last_name_label.grid(row=2, column=0)
        self.last_name_entry.grid(row=2, column=1)

        self.birthdate_label = tkinter.Label(self.user_info_frame, text="Birthdate")
        self.birthdate_entry = tkinter.Entry(self.user_info_frame)
        self.birthdate_label.grid(row=3, column=0)
        self.birthdate_entry.grid(row=3, column=1)

        self.nationality_label = tkinter.Label(self.user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(self.user_info_frame,
                                                 values=["Africa", "Antarctica", "Asia", "Europe", "North America",
                                                         "Oceania", "South America"])
        self.nationality_label.grid(row=4, column=0)
        self.nationality_combobox.grid(row=4, column=1)

        self.position_label = tkinter.Label(self.user_info_frame, text="Position")
        self.position_combobox = ttk.Combobox(self.user_info_frame,
                                              values=["Chief mate/first mate", "Second mate", "Third mate", "Deckhand",
                                                      "Able seaman", "Boatswain (or bosun)", "Chief engineer",
                                                      "Second engineer", "Third engineer", "Fourth engineer", "Oiler",
                                                      "Wiper", "Electrical engineer/electrician", "Chief steward",
                                                      "Cook", "Steward's assistant", "Radio officer", "Ship’s doctor",
                                                      "Pilot"])
        self.position_label.grid(row=5, column=0)
        self.position_combobox.grid(row=5, column=1)
        # Çerçeve içindeki tüm bileşenlerin aralığı ve boşlukları ayarlanır
        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5) # Yatay boşluk 10 piksel,dikey boşluk 5 piksel olarak ayarlanmıştır
        # "Veri Girişi" düğmesi oluşturulur
        self.button = tkinter.Button(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    # Veri girişi fonksiyonu
    def enter_data(self):
        # Gerekli tüm veriler alınır
        id_number = self.id_entry.get()
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        birthdate = self.birthdate_entry.get()
        nationality = self.nationality_combobox.get()
        position = self.position_combobox.get()
        # Eğer tüm gerekli alanlar doldurulmuşsa veriler ekrana yazdırılır
        if id_number and firstname and lastname and birthdate and nationality and position:
            print("ID Number:", id_number)
            print("First name:", firstname)
            print("Last name:", lastname)
            print("Birthdate:", birthdate)
            print("Nationality:", nationality)
            print("Position:", position)
            print("------------------------------------------")

            conn = sqlite3.connect('data.db') # Veritabanına bağlanır
            # Tablo oluşturulması için sorgu
            table_create_query = '''CREATE TABLE IF NOT EXISTS Crew_Information_data 
                                                                                         (id_number INT, firstname TEXT, lastname TEXT, birthdate INT, nationality TEXT, position TEXT)
                                                                                                    '''
            conn.execute(table_create_query)
            # Veri ekleme sorgusu ve değerleri
            data_insert_query = '''INSERT INTO Crew_Information_data (id_number, firstname, 
                                                                                             lastname, birthdate, nationality, position) VALUES 
                                                                                                (?, ?, ?, ?, ?, ?)'''
            # Veritabanına eklenecek veriler, bir demet olarak oluşturulur
            data_insert_tuple = (id_number, firstname, lastname,
                                 birthdate, nationality, position)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple) # Verileri veritabanına ekler
            conn.commit() # Veritabanı değişikliklerini kaydeder
            conn.close() # Veritabanı bağlantısını kapatır

            conn.close()
        # Gerekli tüm alanlar doldurulmadığında kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please fill in all required fields.")

    # Veriyi silme fonksiyonu
    def delete_data(self):
        id_number = self.id_entry.get() # Kimlik numarası alınır
        # Kimlik numarası var ise veritabanına bağlanır
        if id_number:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            # Veritabanından belirtilen kimlik numarasına sahip kayıt silinir
            cursor.execute("DELETE FROM Crew_Information_data WHERE id_number=?", (id_number,))
            conn.commit()
            conn.close()
            print("deleted successfully.") # Ekrana başarı mesajı yazdırır
        # Eğer kimlik numarası girilmemişse kullanıcıya uyarı mesajı gösterilir
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please enter an ID Number to delete.")

class MainApplication:
    def __init__(self, master):
        self.master = master
        # Pencere başlığı ayarlanır
        self.master.title("DATABASE MANAGEMENT SYSTEM")
        # Bir sekme arayüzü oluşturulur
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)
        # her bir form için sekme oluşturulur
        self.container_ship_info_form = ContainerShipInfoForm(self.notebook)
        self.notebook.add(self.container_ship_info_form.frame, text="Container Ship Information")

        self.petrol_tanker_form = PetrolTankerForm(self.notebook)
        self.notebook.add(self.petrol_tanker_form.frame, text="Petrol Tanker Information")

        self.passenger_ship_form = PassengerShipForm(self.notebook)
        self.notebook.add(self.passenger_ship_form.frame, text="Passenger Ship")

        self.port_info_form = PortInfoForm(self.notebook)
        self.notebook.add(self.port_info_form.frame, text="Port Information")

        self.ship_voyage_form = ShipVoyageForm(self.notebook)
        self.notebook.add(self.ship_voyage_form.frame, text="Ship Voyage")

        self.captain_form = CaptainForm(self.notebook)
        self.notebook.add(self.captain_form.frame, text="Captain Information")

        self.crew_form = CrewForm(self.notebook)
        self.notebook.add(self.crew_form.frame, text="Crew Member")
        # Çıkış düğmesi eklenir
        self.exit_button = tkinter.Button(master, text="Exit", command=self.exit_application)
        self.exit_button.pack()

    def exit_application(self): # Uygulamadan çıkış yapma fonksiyonu
        self.master.destroy()

# Ana uygulama fonksiyonu,Tkinter penceresini başlatır.
def main():
    root = tkinter.Tk()
    app = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main() # main fonksiyonunu çağırarak programı başlatır