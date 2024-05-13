import psycopg2
import speech_recognition as sr
from psycopg2 import Error

# تابع للبحث في قاعدة البيانات بالصوت
def voice_search_database():
    try:
        # الاتصال بقاعدة البيانات
        connection = psycopg2.connect(user="postgres",
                                      password="MohamedRizk123",
                                      host="localhost",
                                      port="5432",
                                      database="masark")

        cursor = connection.cursor()

        # استخدام الميكروفون كمصدر صوت
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        print("قل اسم المكان:")

        # تشغيل تقنية إلغاء الضوضاء
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)

            # الاستماع للصوت
            audio = recognizer.listen(source)

        

        # تحويل الصوت إلى نص
        query = recognizer.recognize_google(audio, language="ar-EG").lower()
        

        # استعلام SQL للبحث
        sql_query = "SELECT \"Name\" FROM station WHERE \"Name\" ILIKE %s UNION ALL SELECT \"Name\" FROM road WHERE \"Name\" ILIKE %s UNION ALL SELECT \"name\" FROM masark_famousplace WHERE \"name\" ILIKE %s"
        cursor.execute(sql_query, ('%' + query + '%', '%' + query + '%', '%' + query + '%'))


        # الحصول على النتائج
        results = cursor.fetchall()

        return results  # إرجاع النتائج

    except (Exception, Error) as error:
        print("خطأ أثناء الاتصال بقاعدة البيانات:", error)
        return None  # في حالة الخطأ، يمكنك إرجاع قيمة خاصة بالخطأ أو None

    finally:
        # إغلاق الاتصال بقاعدة البيانات
        if connection:
            cursor.close()
            connection.close()
            

# يمكنك استدعاء الدالة وتخزين النتائج في متغير
results = voice_search_database()

if results:
    for row in results:
        print(row)
else:
    print(" لا توجد نتائج حاول مره اخري.")
