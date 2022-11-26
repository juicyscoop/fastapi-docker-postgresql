run-db: 
	docker run --name test_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mypass -e POSTGRES_DB=test -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres