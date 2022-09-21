requirements:
- linux (tested)
- docker-compose
- docker


* telah disediakan 5 mesin, masing-masing dilengkapi python editor berbasis web (jupyter)
- ds-mesin-1 172.16.16.101
- ds-mesin-2 172.16.16.102
- ds-mesin-3 172.16.16.103
- ds-mesin-4 172.16.16.104
- ds-mesin-5 172.16.16.105


* menjalankan lab
- pastikan docker dapat berjalan , cek dengan docker ps --all (jika ada masalah permission, chmod 777 /var/run/docker.sock)
- pastikan ada file docker-compose.yml
- pastikan docker-compose dapat berjalan (dek dengan docker-compose ps)
- jalankan docker-compose up -d


* mengakses mesin/node
- buka firefox/chrome, arahkan url ke daftar berikut ini
	x ds-mesin-1 http://172.16.16.101:8888
	x ds-mesin-1 http://172.16.16.102:8888
	x ds-mesin-1 http://172.16.16.103:8888
	x ds-mesin-1 http://172.16.16.104:8888
	x ds-mesin-1 http://172.16.16.105:8888
- didalam mesin yang diakses, terdapat folder work, folder ini merupakan folder yang tersambung di folder work seperti yang ada dalam direktori yang sama dengan docker-compose.yml

