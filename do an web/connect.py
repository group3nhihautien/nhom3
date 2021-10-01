import pymysql.cursors  

def connectt():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='123456',                             
                                db='c2c',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,
                                autocommit=True)
    return connection
# Kết nối vào database.

def get_dienthoai():
    try:
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "SELECT * FROM sanpham inner join dangban on sanpham.idsanpham=dangban.idsanpham  inner join nguoidung on dangban.sdt=nguoidung.sdt  where loaisp ='Điện thoại' "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
            for index in cursor:
                lst.append((index['idsanpham'],index['hinhanh'], index['tensp'], index['gia'], index['mieuta'], index['hoten']))
            return lst
    finally:
        connectt().close()

def get_maytinh():
    try:
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "SELECT * FROM sanpham inner join dangban on sanpham.idsanpham=dangban.idsanpham  inner join nguoidung on dangban.sdt=nguoidung.sdt  where loaisp ='Laptop' "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
            for index in cursor:
                lst.append((index['idsanpham'],index['hinhanh'], index['tensp'], index['gia'], index['mieuta'], index['hoten']))
            return lst
    finally:
        connectt().close()


def getten(SDT):
    try:
        with connectt().cursor() as cursor:
       
            sql = "SELECT hoten FROM nguoidung where sdt =%s "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql,SDT)
            for index in cursor:
                return index['hoten']
                 
            
    finally:
    # Đóng kết nối (Close connection).       
        connectt().close()

def get_tab():
    try:
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "SELECT * FROM sanpham inner join dangban on sanpham.idsanpham=dangban.idsanpham  inner join nguoidung on dangban.sdt=nguoidung.sdt  where loaisp ='Máy tính bảng' "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
            for index in cursor:
                lst.append((index['idsanpham'],index['hinhanh'], index['tensp'], index['gia'], index['mieuta'], index['hoten']))
            return lst
    finally:
        connectt().close()


def get_pc():
    try:
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "SELECT * FROM sanpham inner join dangban on sanpham.idsanpham=dangban.idsanpham  inner join nguoidung on dangban.sdt=nguoidung.sdt  where loaisp ='PC' "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
            for index in cursor:
                lst.append((index['idsanpham'],index['hinhanh'], index['tensp'], index['gia'], index['mieuta'], index['hoten']))
            return lst
    finally:
        connectt().close()


def get_another():
    try:
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "SELECT * FROM sanpham inner join dangban on sanpham.idsanpham=dangban.idsanpham  inner join nguoidung on dangban.sdt=nguoidung.sdt  where loaisp ='Thiết bị khác' "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
            for index in cursor:
                lst.append((index['idsanpham'],index['hinhanh'], index['tensp'], index['gia'], index['mieuta'], index['hoten']))
            return lst
    finally:
        connectt().close()



def Dangki_user(sdt,hoten,diachi,mk):
    try:
        with connectt().cursor() as cursor:
       
            sql = "insert into nguoidung(sdt,hoten,diachi) values (%s,%s,%s)"
            sql2 = "insert into taikhoan(sdt,matkhau) values (%s,%s)"
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql,(sdt,hoten,diachi))
            cursor.execute(sql2,(sdt,mk))
            connectt().commit
            return True
    except:

        return False    
        
def getloaisp(ID):
    try:
        with connectt().cursor() as cursor:
       
            sql = "SELECT loaisp FROM sanpham where idsanpham =%s "
            
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql,ID)
            for index in cursor:
                return index['loaisp']
                 
            
    finally:
    # Đóng kết nối (Close connection).       
        connectt().close()


def Check_DangNhap(sdt,mk):
    try:
        with connectt().cursor() as cursor:
       
            sql = "select matkhau from taikhoan where sdt=%s"
            cursor.execute(sql,(sdt))
            for index in cursor:
                if index['matkhau'] == mk:
                    return True
                else:
                    return False
    finally:
          
        connectt().close()
def themvaogiohang(sdt,idSp):
    try:
        with connectt().cursor() as cursor:
            sql = "insert into giohang(ID_KH, Id_sanpham) values (%s,%s)"
            cursor.execute(sql,(sdt,idSp))
            return connectt().commit
            
    finally:
        connectt().close()
        return False


def chongiohang(sdt):
    try:   
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "select * from sanpham inner join giohang on sanpham.ID= giohang.Id_sanpham inner join khachhang on khachhang.Sdt=giohang.ID_KH where giohang.ID_KH =%s"

            cursor.execute(sql,sdt)
            for index in cursor:
                lst.append((index['ID'],index['hinhanh'], index['TenSp'], index['GiaTien'], index['ChiTietSp']))
            return lst
    finally:
               
        connectt().close()

def dathang(Sdt, IdSP,Soluong):
    try:
        with connectt().cursor() as cursor:
            sql = "insert into dathang2(Sdt,ID_SanPham,Ngay,soluong,xacnhan) values (%s,%s,now(),%s,0)"
            cursor.execute(sql,(Sdt,IdSP,Soluong))
            return connectt().commit
    finally:
    # Đóng kết nối (Close connection).       
        connectt().close()
        return False

def xoakhoikhohang(sdt, sanpham):
    try:
        with connectt().cursor() as cursor:
            sql = "delete from khohang where idsanpham=%s and sdt= %s"
            sql2= "delete from sanpham where idsanpham=%s"
            cursor.execute(sql,(sanpham,sdt))
            cursor.execute(sql2, sanpham)
            connectt().commit
    finally:
    # Đóng kết nối (Close connection).       
        connectt().close()

def dsSPduocchon(sdt):
    try:   
        lst = []
        with connectt().cursor() as cursor:
       
            sql = "select hinhanh,sanpham.TenSp, GiaTien, soluong, soluong*GiaTien as thanhtien, Ngay, dathang2.ID from sanpham inner join dathang2 on sanpham.ID=dathang2.ID_SanPham inner join khachhang on dathang2.Sdt = khachhang.Sdt where khachhang.Sdt=%s and xacnhan !=1 "

            cursor.execute(sql,sdt)
            for index in cursor:
                lst.append((index['hinhanh'], index['TenSp'], index['GiaTien'], index['soluong'], index['thanhtien'],index['Ngay'],index['ID']))
            return lst
    finally:
               
        connectt().close()

def xacnhan(id_dathang):
    try:   
        with connectt().cursor() as cursor:
            sql = "update dathang2 set xacnhan=True, ngayxacnhan=now()  where ID=%s"
            cursor.execute(sql,id_dathang)
            connectt().commit
    finally:    
        connectt().close()

def xoakhoidsmua(sdt,idd):
    try:   
        with connectt().cursor() as cursor:
            sql = "delete from dathang2 where ID=%s"
            cursor.execute(sql,idd)
            connectt().commit
    finally:    
        connectt().close()

def themsdtcucbo(x):
    try:   
        with connectt().cursor() as cursor:
            sql = "update quydinh set SdtCucBo=%s where IdQuyDinh='SdtCucBo'"
            cursor.execute(sql,x)
            connectt().commit
    finally:    
        connectt().close()

def getsdtcucbo():
    try:   
        with connectt().cursor() as cursor:
            sql = "select sdtcucbo from QuyDinh where IdQuyDinh='SdtCucBo'"
            cursor.execute(sql)
            for index in cursor:
                return index['sdtcucbo']
    finally:    
        connectt().close()
def dstrongkhohang(sdt):
    try:   
        lst=[]
        with connectt().cursor() as cursor:
            sql = "SELECT * FROM sanpham inner join khohang on sanpham.idsanpham=khohang.idsanpham inner join nguoidung on khohang.sdt=nguoidung.sdt  where nguoidung.sdt=%s  order by sanpham.idsanpham desc "
            cursor.execute(sql,sdt)
            for index in cursor:
                lst.append((index['hinhanh'], index['tensp'], index['gia'], index['soluong'],index['mieuta'], index['idsanpham'], index['ngaytao']))
            return lst
    finally:    
        connectt().close()

def dsxacnhanthanhcong(x):
    try:   
        lst=[]
        with connectt().cursor() as cursor:
            sql = "select hinhanh,sanpham.TenSp,sanpham.GiaTien,soluong,GiaTien*soluong as thanhtien, ngayxacnhan from dathang2 inner join sanpham on sanpham.ID= dathang2.ID_SanPham where xacnhan=1 and dathang2.ID=%s"
            cursor.execute(sql,x)
            for index in cursor:
                lst.append((index['hinhanh'], index['TenSp'], index['GiaTien'], index['soluong'], index['thanhtien'],index['ngayxacnhan']))
            return lst
    finally:    
        connectt().close()

def resetsdtcucbo():
    try:   
        with connectt().cursor() as cursor:
            sql = "update quydinh set SdtCucBo=' ' where IdQuyDinh='SdtCucBo'"
            cursor.execute(sql)
            connectt().commit
    finally:    
        connectt().close()

def xacnhanthanhtoan(ID):
    try:   
       
        with connectt().cursor() as cursor:
            sql = "select dathanhtoan from dathang2 where ID=%s"
            cursor.execute(sql,ID)
            for index in cursor:
                if index['dathanhtoan']==1:
                    return True
                else:
                    return False
           
    finally:    
        connectt().close()

def lichsumua(ID):
    try:   
        lst=[]
        with connectt().cursor() as cursor:
            sql = "select hinhanh,sanpham.TenSp,sanpham.GiaTien,soluong,GiaTien*soluong as thanhtien, ngayxacnhan, ghichu from dathang2 inner join sanpham on sanpham.ID= dathang2.ID_SanPham  inner join khachhang on khachhang.Sdt=dathang2.Sdt where xacnhan=1 and khachhang.Sdt = %s order by ngayxacnhan desc"
            cursor.execute(sql,ID)
            for index in cursor:
                lst.append((index['hinhanh'], index['TenSp'], index['GiaTien'], index['soluong'], index['thanhtien'],index['ngayxacnhan'],index['ghichu']))
            return lst
    finally:    
        connectt().close()

def themvaokhohang(tensp, gia, mieuta, hinhanh, loaisp, sdt,soluong):
    try:
        with connectt().cursor() as cursor:
            sql = " insert into sanpham (tensp, gia, mieuta,luotmua, hinhanh,loaisp,soluong,ngaytao) values (%s,%s,%s,0,%s,%s,%s,now())"
            sql2 =" insert into khohang (sdt, idsanpham) values (%s,(select last_insert_id()))"
            cursor.execute(sql,(tensp, gia, mieuta, hinhanh, loaisp,soluong))
            cursor.execute(sql2,sdt)
            
            return connectt().commit
    finally:    
        Exception 

def dangban(sdt, sanpham):
    try:
        with connectt().cursor() as cursor:
            sql = " insert into dangban (sdt,idsanpham, ngaydang) values (%s,%s,now())"
            cursor.execute(sql,(sdt,sanpham))
            return connectt().commit
    finally:    
        Exception 
def kiemtramaloaisp(tenloai):
    try:   
        with connectt().cursor() as cursor:
            sql = "select maloai from loaisp where tenloai like {}".format(tenloai)
            cursor.execute(sql)
            for index in cursor:
                return index['maloai']
    finally:    
        Exception 

     


