# FastApi books api

---
## __Configuration__
<br/>

### ***Docker***
<br/>

*Setting up mysql database*

    docker compose up -d
<br/>

Default **connecting** string to database: `mysql+pymysql://root:passwordroot@localhost/db`

<br/>

### **Environment Variables**
<br/>

Connection string must be set up in Environment

    export DATABASE="mysql+pymysql://root:passwordroot@localhost/db"

***If you dont't want setting each time you can create file with .env inside app folder***

    touch app/.env


***Inside .env file add***

    DATABASE="mysql+pymysql://root:passwordroot@localhost/db"


---