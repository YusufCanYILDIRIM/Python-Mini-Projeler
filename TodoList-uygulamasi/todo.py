# boş to do list dizisi
to_do_list = []

# kullanıcıdan görev alma
def add_task(to_do_list):
    task = input("görevinizi ekleyiniz :")
    to_do_list.append(task)
    print("görev basarıyla eklendi")

# eklenen görevleri gösterme   
def show_task(to_do_list):
    print("yapilacak görevler :")
    for show in to_do_list:
        print("-", show)

# görevleri silme
def delete_task(to_do_list):
    task = input("silmek istediginiz görevleri yaziniz :")
    if task in to_do_list:
        to_do_list.remove(task)
        print("görev basariyla silindi")
    else:
        print("görev bulunamadi")

# ana döngüler        
while True:
    print("ToDoList Uygulamasi")
    print("1- görev ekleme ")
    print("2- görevleri listeleme ")
    print("3- görevleri silme ")

    choice = input("birini seçiniz (1/2/3) : ")

    if choice == '1':
        add_task(to_do_list)
    elif choice == '2':
        show_task(to_do_list)
    elif choice == '3':
        delete_task(to_do_list)
        break
    else:
        print("yanlis tuslama yaptiniz")



