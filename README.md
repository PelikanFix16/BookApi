# FastApi books api
<br/>
<br/>

---
## __Configuration__
<br/>

### ***Docker***
<br/>

*Setting up mysql database*

    docker compose up -d
<br/>

Default **connecting** string to database: `mysql+pymysql://root:passwordroot@localhost/db`


**Connection credentials can be modified inside docker compose**



<br/>

### **Environment Variables**
<br/>

Connection string must be set up in Environment

    export DATABASE="mysql+pymysql://root:passwordroot@localhost/db"

***If you dont't want setting each time you can create file with .env inside app folder***

    touch app/.env


***Inside .env file add***

    DATABASE="mysql+pymysql://root:passwordroot@localhost/db"


<br/>


### **Requirments**
<br/>

    pip3 install -r requirments.txt


<br/>

### **Database Migrations using Alembic**
<br/>

***Creating blank migration for downgrade if needed***

    alembic revision -m "initial"

**if migrations created correctly then update head and apply migrations**

    alembic upgrade +1


**Next autogenerate models to alembic migrations**

    alembic revision --autogenerate -m "Initial book"


Then if created correctly and inside folder `db-migration -> versions` file with title Inital book looks like

```Python

def upgrade():
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('authors', mysql.JSON(), nullable=False),
    sa.Column('published_date', sa.Integer(), nullable=False),
    sa.Column('categories', mysql.JSON(), nullable=False),
    sa.Column('average_rating', sa.Float(), nullable=False),
    sa.Column('ratings_count', sa.Integer(), nullable=False),
    sa.Column('thumbnail', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

```

**Second time update alembic**

    alembic upgrade +1


***Now tables should be created insidie database***


---





<br/>


<br/>

---
## __Starting Up API__
<br/>

**If all requirements installed correctly app should be start using**

    uvicorn --reload --host 0.0.0.0 --port 8001 app.main:app


---


<br/>

<br/>

---

## __Api Routes__

<br/>

<br/>



### **Books**


- ***URL***

    /books
- ***Method***
 
    `POST`

- ***URL PARAMS***
  
    None

- ***Data Parmas***
  
    JSON

    `{"q":"Hobbit"}`

- ***Success Response***

    - *Code:* 200 Ok
        
        Content: `{"books":"/books/"}`

- ***Error Response***
  
  - *Code:* 422 Unprocessable Entity
    
    Content: `{"detail":[{"loc":["body","q"],"msg":"field required","type":"value_error.missing"}]}`


- ***URL***

    /books
- ***Method***
 
    `GET`

- ***URL PARAMS***
  
    ***Optional***
    
    `authors=List[string]`

    `published_date=List[integer]`

    `sort=String default ASC`

    `id=String`


    **Example**

    - `/books?authors=J. R. R. Tolkien&published_date=2010&published_date=2018&authors=Amy Clark&sort=DESC`
    - `/books?idBook=5dv-7xurxXsC`
  


- ***Data Parmas***
  
    None

- ***Success Response***

    - *Code:* 200 Ok
        
        Content: `[BookSchema]`


 

---

<br/>

<br/>


