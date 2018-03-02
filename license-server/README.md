license.db

```
# @ bash
sqlite3 license.db

# @ sqlite shell
create table license(cn text primary key, pass text, threshold smallint, counter smallint);
insert into license values('client', 'CN: client', 10, 0);
.quit
```

Test

```
bash test.sh
```
