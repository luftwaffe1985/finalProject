from datetime import datetime


def write_log(data):
    time = datetime.now().strftime('%H hours %M minutes %m.%d.%Y year')
    with open('C:\\Users\\Asus\\PycharmProjects\\finalProject\\log.csv', 'a', encoding="utf-8") as file:
        file.write('{};{}\n'.format(time, data))
