from flask import Flask, flash, redirect
from flask import render_template
from flask_wtf import FlaskForm, Form
from flask import request, jsonify
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField,SelectField,BooleanField, SubmitField, TextAreaField,validators, FileField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

import os
import connect


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


csrf = CSRFProtect()
uploads_dir = os.path.join(app.instance_path, 'images')


app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

global sdtcucbo

csrf.init_app(app)
class LoginForm(Form):
    username = StringField('Số điện thoại', validators=[DataRequired()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Đăng nhập')
class DangKi(Form): 
    remember_me = BooleanField('Nhớ mật khẩu')
    Hoten = StringField('Họ tên', validators=[DataRequired()])
    diachi = StringField('Địa chỉ', validators=[DataRequired()])
    sdt = StringField('Số điện thoại', validators=[DataRequired()])
    matkhau = PasswordField('Mật khẩu mới', [validators.DataRequired(),validators.EqualTo('confirm', message='Mật khẩu phải trùng khớp')])
    confirm = PasswordField('Lặp lại mật khẩu')
    submit = SubmitField('Đăng kí')
class Themsanpham(FlaskForm):
    tensanpham = StringField ('Tên sản phẩm', validators=[DataRequired()])
    gia = StringField ('Giá',validators=[DataRequired()])
    luachon=SelectField('Lứa chọn',choices=['Điện thoại','Laptop','Máy tính bảng','PC','Thiết bị khác'])
    chitiet = TextAreaField ('Mô tả chi tiết')
   
    picture = FileField('Update Profile Picture',filters=tuple())
    submit = SubmitField ('Thêm vào kho hàng')
@app.route ("/")
@app.route ("/base")
def loadbase():
    return render_template('base.html' )

@app.route ("/trangchu")
def index():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('trangchu.html', the_title ='Trang chủ')


@app.route ('/dienthoai')

def dienthoai():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
   
    return render_template('banhsinhnhat.html', the_title ='Bánh sinh nhật',images =connect.get_dienthoai())
@app.route ('/laptop')
def laptop():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('chocolate.html', the_title ='Chocolate', images= connect.get_maytinh())
@app.route ('/tab')
def tab():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('banhtrungthu.html', the_title ='Bánh Trung Thu', images= connect.get_tab())
@app.route ('/pc')
def pc():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('another.html', the_title ='Bánh khác', images= connect.get_pc())
@app.route ('/another')
def another():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('another.html', the_title ='Bánh khác', images= connect.get_another())

@app.route ('/dangki', methods=["GET", "POST"])
def dangki():
    form = DangKi()
    if form.validate_on_submit():
        if connect.Dangki_user(form.sdt.data, form.Hoten.data, form.diachi.data, form.matkhau.data)== True:
            return redirect('/dangnhap')
        else:
            flash('Số điện thoại này đã có, vui lòng đăng kí bằng số khác')

    return render_template('dangki.html', title='Đăng kí', form=form)


@app.route('/dangnhap',methods=["GET", "POST"])
def dangnhap():
    form = LoginForm()
    if form.validate_on_submit():
        check= connect.Check_DangNhap(form.username.data, form.password.data)
        if check==True:
            
            connect.themsdtcucbo(form.username.data)   
           
            return redirect('/trangchu')
        else:
            flash('Đăng nhập sai tên hoặc mật khẩu')
            return redirect('/dangnhap')
    return render_template('dangnhap.html', title='Sign In', form=form)
@app.route('/giohang', methods =['GET','HEAD'])
def giohang():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    if request.method=='GET':
        Id = request.values.get('btn')
        connect.themvaogiohang(x,Id) 
        loaisp=connect.getloaisp(Id)
        if loaisp==1:
            return redirect('/banhsinhnhat')
        if loaisp==2:
            return redirect('/chocolate')
        if loaisp==3:
            return redirect('/banhtrungthu')
        if loaisp==4:
            return redirect('/another')


@app.route('/cart')
def cart():

    return render_template('giohang.html', title='Giỏ hàng')

@app.route ('/thanhtoan',methods=['GET','POST'])

def thanhtoan():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    if request.method=='GET':
        check= connect.dathang(x , request.values.get('btn'), request.values.get('soluong'))
        if check==False:
            return redirect('/cart')
        else:
        
            return redirect('/cart')



@app.route ('/xoakhoidsmua',methods=['GET','POST'])
def xoakhoidsmua():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    if request.method=='GET':

        connect.xoakhoidsmua(x,request.values.get('X'))
        
    return redirect('/cart')

@app.route ('/xacnhan',methods=['GET','POST'])
def xacnhan():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    if request.method=='GET':
        connect.xacnhan(request.values.get('bt'))
    return render_template('xacnhanthanhcong.html',images=connect.dsxacnhanthanhcong(request.values.get('bt')))

@app.route('/quaylaimuasam', methods=['GET','POST'])
def quaylaimuasam():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    if request.method=='GET':
        return redirect('/')
@app.route('/themsanpham',methods =['get','post'])
def themsanpham():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    form = Themsanpham()
    tensp= form.tensanpham.data
    gia =request.values.get('gia')
    mieuta=form.chitiet.data
    loaisp=form.luachon.data
    hinhanh =form.picture.data 

    
    soluong= request.values.get('number')
    print (request.values.get('number'))
        
    if form.is_submitted():
        
        connect.themvaokhohang(tensp,gia,mieuta,hinhanh,loaisp,x,soluong)
        return redirect('/khohang')
 

    return render_template('themsanpham.html',form=form, list=connect.dstrongkhohang(x))
  

@app.route('/reset')
def reset():
    connect.resetsdtcucbo() 
    return redirect('/trangchu')

@app.route('/khohang')
def khohang():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('khohang.html',list=connect.dstrongkhohang(x))

@app.route('/lienhe')
def lienhe():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('lienhe.html')

@app.route('/lichsu')
def lichsu():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    return render_template('lichsu.html', images=connect.lichsumua(x))

@app.route('/dangban')
def dangban():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    connect.dangban(x,request.values.get('btn'))
    return render_template('khohang.html',list=connect.dstrongkhohang(x))
@app.route('/xoahangtrongkho')
def xoahangtrongkho():
    x=connect.getsdtcucbo()
    flash(connect.getten(x))
    connect.xoakhoikhohang(x,request.values.get('btn1'))
    return render_template('khohang.html',list=connect.dstrongkhohang(x))
if __name__ =="__main__":
   
    app.run(debug=True)
    