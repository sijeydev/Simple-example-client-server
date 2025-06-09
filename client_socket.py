# github and tg - @sijeydev
#клиент
import socket

"""Создание сокета"""
def start_клиент():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET(IPv4), AF_INET6(IPv6); SOCK_STREAM(TCP), SOCK_DGRAM(UPD)
	
	client_socket.connect(("localhost", 8080)) #подключение к серверу по адресу

	while True:
		
		
		"""Отправка и получение данных"""
		data = client_socket.recv(1024) #получение данных от сервера
		client_socket.send(b"Hello, world!") #отправка данных серверу
		
		print(f"Получена информация от сервера: {data.decode()}")
		#client_socket.close() #закрытие сокетa
		
if __name__ == "__main__":
	start_клиент()