from django.shortcuts import render
from .models import NumberofData
import sqlite3
def UserPosted(request):
    con=sqlite3.connect('db.sqlite3')
    cursor=con.cursor()
    cursor.execute('Select id From auth_user')
    user_blog_id = cursor.fetchall()
    len_users_id = len(user_blog_id)
    ls_usr = []
    for i in range(len_users_id):
        ls_usr.append(user_blog_id[i][0])
    
    cursor.execute('Select users From data_numberofdata')
    blog_id = cursor.fetchall()
    len_blog_id = len(blog_id)
    ls_data = []
    for i in range(len_blog_id):
        ls_data.append(blog_id[i][0])
    

    for i in ls_usr:
        data=NumberofData()
        cursor.execute("Select username From auth_user where id=(?)",(i,))
        user=cursor.fetchall()
        user_data=user[0][0]
        cursor.execute("Select count(title) From blog_post where author_id=(?)",(i,))
        datas=cursor.fetchall()
        data_index=datas[0][0]
        cursor.execute("Select count(object_id) From django_admin_log where object_id=(?)",(i,))
        log=cursor.fetchall()
        log_data=log[0][0]
        if user_data in ls_data:
            cursor.execute("Select posted From data_numberofdata where users=(?)",(user_data,))
            c_posted=cursor.fetchall()
            control_posted=int(c_posted[0][0])
            cursor.execute("Select login From data_numberofdata where users=(?)",(user_data,))
            c_login=cursor.fetchall()
            control_login=int(c_login[0][0])
            if(data_index==control_posted and log_data==control_login):
                continue
            elif(data_index != control_posted or log_data!=control_login):
                cursor.execute("Update data_numberofdata set posted = (?) where users=(?)",(control_posted,user_data,))
                cursor.execute("Update data_numberofdata set login= (?) where users=(?)",(control_posted,user_data,))
                
        else:   
            data.users=user_data
            data.posted=data_index        
            data.login=log_data
            data.save()

    argv=NumberofData.objects.all()
    return render(request,"data/data_table.html",{'data':argv})


          

        
       
    
    

     

 
