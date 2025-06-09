# github and tg - @sijeydev
#серверное приложение
import socket

"""Создание сокета"""
def start_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET(IPv4), AF_INET6(IPv6); SOCK_STREAM(TCP), SOCK_DGRAM(UPD)
	
	server_socket.bind(("localhost", 8080)) #привязка к адресу и порту
	server_socket.listen(5) #прослушивать до 5 входящих соединений
	print("Сервер ожидает соединения...")

	while True:
		client_socket, client_address = server_socket.accept() #сокет для общения с клиентом
		print(f"Установлено соединение с {client_address}")
		
		"""Отправка и получение данных"""
				
		client_socket.send(b"Hello, world!") #отправка данных клиенту (sendall - оиправить всем клиентам сразу)
		
		data = client_socket.recv(1024) #получение данных от клиента
		
		print(f"Получена информация от клиента: {data.decode()}")
		#client_socket.close() #закрытие сокетa
		
if __name__ == "__main__":
	start_server()