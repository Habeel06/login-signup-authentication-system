from flask import Flask, render_template, request, redirect, url_for,flash
import os
import bcrypt

app = Flask(__name__)
app.secret_key="auth_key_temp" 

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login",methods=['GET','POST'])

def login():

    if request.method == 'POST':
        usr_name = request.form['usr']
        usr_password=request.form['pass']
        
        try:
           
        
            usr_01=usr_name
            passwd_01=usr_password

            auth_string=(usr_01+passwd_01)

            with open(f"{usr_01}.txt",'rb') as file: # for those who are wondering why as rb its because we need it as a binary format for bcrypt,fr
                a=file.read()
                

                if  bcrypt.checkpw(auth_string.encode('utf-8'),a):
                    
                    print("")
                    print("Logged In!")
                    
                    
                    with open(f"{usr_01}_name.txt",'r') as file:
                        msg1=file.read()
                        print(f"Hello,{msg1}!!")
                        
                        

                    with open(f"{usr_01}_token.txt",'r') as file:
                        msg2=file.read()
                        print(f"Your token is : ,{msg2}")
                        flash(f"Hello {msg1},Your Secret Message is : {msg2}")

                else: 
                    
                    flash("WRONG USERNAME OR PASSWORD,PLEASE TRY AGAIN!")
                    return redirect("/login")


        except FileNotFoundError:
           flash("WRONG USERNAME OR PASSWORD,PLEASE TRY AGAIN!")
           return redirect("/login")
       
    return render_template("login.html")



@app.route('/signup',methods=['GET','POST'])

def signup():
    if request.method == 'POST':

        usr_02= request.form['usr']
        passwd_02=request.form['pass']
        name_02=request.form['name']
        token_02=request.form['token']

        usr_verify=(f"{usr_02}.txt")
        if os.path.exists(usr_verify):
            print("")
            print("Username already taken,choose a different username!")
            flash("Username already taken,choose a different username!")
        else:
            deez=(usr_02+passwd_02)
            hashed=bcrypt.hashpw(deez.encode('utf-8'),bcrypt.gensalt())
           

            with open(f"{usr_02}.txt",'wb') as file:
                file.write(hashed)

       

            with open(f"{usr_02}_name.txt",'w') as file:
                file.write(f"{name_02}")

            with open(f"{usr_02}_token.txt",'w') as file:
                file.write(f"{token_02}")
            print("")
            print("Thank You for Signing Up!!")
            print("")
            flash( "Thank You for Signing Up!!" )
            return redirect('/login')
            
       
        
        
        
    return render_template('signup.html')
        


if __name__ == '__main__':
    app.run()

