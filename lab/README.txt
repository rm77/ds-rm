requirements:
- linux (tested)
- docker-compose
- docker


* menjalankan lab
	- pastikan docker dapat berjalan , cek dengan docker ps --all (jika ada masalah permission, chmod 777 /var/run/docker.sock)
	- pastikan ada file docker-compose.yml
	- pastikan docker-compose dapat berjalan (dek dengan docker-compose ps)
	- jalankan docker-compose up -d

* telah disediakan 5 mesin, masing-masing dilengkapi python editor berbasis web (jupyter), semua mesin ini berjalan di komputer local
  memanfaatkan linux container sebagai server/mesin/node
	- ds-mesin-1 172.16.16.101
	- ds-mesin-2 172.16.16.102
	- ds-mesin-3 172.16.16.103
	- ds-mesin-4 172.16.16.104
	- ds-mesin-5 172.16.16.105

* mengakses mesin/node
- buka firefox/chrome, arahkan url ke daftar berikut ini
	x ds-mesin-1 http://172.16.16.101:8888
	x ds-mesin-2 http://172.16.16.102:8888
	x ds-mesin-3 http://172.16.16.103:8888
	x ds-mesin-4 http://172.16.16.104:8888
	x ds-mesin-5 http://172.16.16.105:8888
- didalam mesin yang diakses, terdapat folder work, folder ini merupakan folder yang tersambung di folder work seperti yang ada dalam direktori yang sama dengan docker-compose.yml

* NETWORK mode
- agar dapat diakses dari internet, gunakan docker-compose-host.yml
- docker-compose -f docker-compose-host.yml up -d
- mesin akan dijalankan dengan url sebagai berikut
	x ds-mesin-1 http://0.0.0.0:34001
	x ds-mesin-2 http://0.0.0.0:34002
	x ds-mesin-3 http://0.0.0.0:34003
	x ds-mesin-4 http://0.0.0.0:34004
	x ds-mesin-5 http://0.0.0.0:34005
