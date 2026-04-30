"""
BUILDER: AHMED HAMDI
ROLE: AUTOMATION & SOFTWARE DEVELOPER
VERSION: 2.1 (SIMPLIFIED DEMO)
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# -----------------------------------------------------------
# الإعدادات - CONFIGURATION
# -----------------------------------------------------------
BOT_TOKEN = "ضع_هنا_توكن_البوت"  # التوكن الخاص بـ BotFather
# -----------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    الدالة المسؤولة عن الرد على أمر /start
    """
    
    # نص الرسالة التعريفية
    welcome_text = (
        "اهلا وسهلا بك\n\n"
        "انا احمد حمدي، مطور برمجيات وأتمتة اعمال.\n"
        "اقدم حلول ذكية لتوفير الوقت وزيادة الانتاجية عبر البرمجيات المخصصة.\n\n"
        "تنبيه: هذا البوت هو مجرد نموذج تجريبي (Demo) لعرض القدرات التقنية.\n"
        "يتم تصميم وبناء البوتات والخدمات البرمجية بشكل مخصص بالكامل حسب متطلبات كل مشروع."
    )

    # أزرار الخدمات
    keyboard = [
        [InlineKeyboardButton("خدمات اتمتة الاعمال", callback_data='service_1')],
        [InlineKeyboardButton("برمجة البوتات المخصصة", callback_data='service_2')],
        [InlineKeyboardButton("تطوير حلول الويب", callback_data='service_3')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=reply_markup
    )

def main():
    """
    تشغيل البوت
    """
    if BOT_TOKEN == "ضع_هنا_توكن_البوت":
        print("خطأ: يرجى وضع KeyBot (TOKEN) الصحيح داخل ملف الكود.")
        return

    # إنشاء التطبيق
    application = Application.builder().token(BOT_TOKEN).build()

    # إضافة معالج أمر البداية
    application.add_handler(CommandHandler("start", start))

    print("البوت قيد التشغيل الآن...")
    application.run_polling()

if __name__ == "__main__":
    main()
