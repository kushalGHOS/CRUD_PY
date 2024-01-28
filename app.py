import cx_Oracle
import streamlit as st
con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
cursor = con.cursor()
def main():
    st.title("crud operations")
    x=st.selectbox("select an operation",("Create","Read","Update","Delete"))
    if x=="Create":
       id=st.text_input("enter your id")
       name=st.text_input("enter your name")
       mail=st.text_input("enter your mail")
       if st.button("submit"):
        query = "INSERT INTO STUDENT VALUES (:1, :2, :3)"
        values = (id, name, mail)
        cursor.execute(query, values)
        con.commit()
        st.success("Record inserted")
    elif x=="Read" :
       result=cursor.execute("select * from STUDENT")
       st.write("the records are")
       for row in result:
            st.write(row)

    elif x=="Update":
       id1=st.text_input("enter  id u want to update")
       name2=st.text_input("enter your name")
       mail3=st.text_input("enter your mail")
       if st.button("submit"):
        query2 = "UPDATE STUDENT SET name=:1, mail=:2 WHERE id=:3"
        val = (name2, mail3, id1)
        cursor.execute(query2, val)
        con.commit()
        st.success("Record updated")
    
    
    
    elif x=="Delete":
       i=st.text_input("enter id u want to delete")
       if st.button("submit"):
            query3="delete from Student where id=:1"
            val2=(i)
            cursor.execute(query3,val2)
            con.commit()
            st.success("deleted")



            







if __name__=="__main__":
    main()