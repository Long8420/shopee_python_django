step build run docker
    - colima start
    - docker-compose build 
    - docker-compose up -d
    - docker-compose run djangoapp
python django
    - docker-compose run djangoapp runserver
    - docker-compose run djangoapp makemigrations
    - docker-compose run djangoapp migrate
Delete all volumes (database on docker)
    - docker-compose down --volumes   
run db treen docker container app 
    - docker exec -it djangoapp bash
    - python src/manage.py makemigrations
    - python src/manage.py migrate
check db
     >>from django import db
     >>print( db.connections.databases)
Stop environment
    - deactivate (venv)
    - source venv/bin/activate
create superUser 
    - docker-compose run web python  manage.py createsuperuser
Kiểm tra quyền của database postgres mình tạo bỏ vào (username)
    - psql -l
Kiem tra dabase quyen postgres 
    - psql -U postgres
Create database bang tay
    - psql -U postgres
    - >> CREATE USER myprojectuser WITH PASSWORD 'mypassword';
    - >> CREATE DATABASE myprojectdb WITH OWNER myprojectuser;
Close all port 5432
    - sudo kill -kill $(sudo lsof -t -i :5432)
