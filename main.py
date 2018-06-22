# coding:utf8

def main():


# 权限
privilege_list = [
    "SELECT",
]

table_list = get_table_list()

user_info = {
    "username": "",
    "password": "",
    "host": "%",
    "db": "ifc",
    "privilege": ",".join(privilege_list),
    "table_list": table_list,

}

# 创建用户语句
create_user = "CREATE USER '{username}'@'{host}' IDENTIFIED BY '{password}';".format(**user_info)
print(create_user)

grant_sql = "GRANT {privilege} ON {db}.{table} TO '{username}'@'{host}';"

# 授权
for table in user_info['table_list']:
    grant = grant_sql.format(table=table, **user_info)
    print(grant)
