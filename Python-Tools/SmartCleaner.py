"""
TOOL: SMART FILE ORGANIZER
BUILDER: AHMED HAMDI
PURPOSE: تنظيم ملفات العمل المبعثرة تلقائياً في مجلدات منسقة
"""

import os
import shutil

def organize_folder(target_path):
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Spreadsheets': ['.xlsx', '.csv'],
        'Archives': ['.zip', '.rar']
    }

    for file in os.listdir(target_path):
        file_path = os.path.join(target_path, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, exts in extensions.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    dest_folder = os.path.join(target_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break
            
            if not moved:
                other_folder = os.path.join(target_path, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

    print("تم تنظيم المجلد بنجاح.")

if __name__ == "__main__":
    # ضع مسار المجلد الذي تريد تنظيمه هنا
    organize_folder("./Downloads")
