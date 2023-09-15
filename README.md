## Instructions comming soon

### Prepare your database container
1. Build a docker image from the `./db/Dockerfile` with `docker build -t finvero/postgres:1.0 -f db/Dockerfile ./db`
2. Run a container from our image: `docker run --name finvero-database-container -p 5432:5432 -e POSTGRES_PASSWORD=somepassword -d finvero/postgres:1.0`
3. To interact with the newly created DB run: `docker exec -it finvero-database-container psql -U postgres`
4. Now type `\c finvero_database` and you'll connect to *finvero_database* then you can list the tables with `\dt`
4. To quit from the psql client use `\q`

### Create environment variables
Create a file called `.env` in which you'll need to specify the next variables.
```.env
DATABASE_NAME=finvero_database
DATABASE_USER=postgres
DATABASE_PASSWORD=somepassword
DATABASE_HOST=localhost
DATABASE_PORT=5432

SECRET_KEY=somesecretkey
```

### Execute the code
1. Create the virtual environment `python -m venv .venv`
2. Activate the environment `source .venv/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
3. Run the followiing command `uvicorn main:app --reload --env-flie .env` to execute the project or just run the *run.sh* script
