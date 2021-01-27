现在是英语，如果你需要中文 [请点击这里](https://github.com/azurestar-space/RollWiki/blob/master/README_zh-cn.md)
# RollWiki
A Simple Single Page Wiki Software.
## Environment
MySQL or SQLite3 (required)

### Setup Environment
1. Install MySQL Server on your computer (If you using MySQL)
2. Connect to your database and create a schema called rollwiki (If you using MySQL)
3. Create a new file called `settings.json` (if you are using MySQL, just see `settings.mysql.default.json`, if you are using SQLite3, just see `settings.sqlite3.default.json`)
4. run `python manage.py migrate` (your python version must be python3)
5. 
```shell
pip install django
pip install mysqlclient # If you are using MySQL, install it
```

## Supported Languages

English (en)

Chinese (zh)
