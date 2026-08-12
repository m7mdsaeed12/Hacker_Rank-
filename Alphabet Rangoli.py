def print_rangoli(size):
    import string
    # جلب الحروف الأبجدية الصغيرة
    design = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        # تحديد الحروف المستخدمة في السطر الحالي وعكسها لتبدأ من الحرف الأكبر وتتناقص
        s = "-".join(design[i:size])
        # دمج النصف الأيمن والأيسر للحروف وتوسيطها في السطر بالشرطات (-)
        row = (s[::-1] + s[1:]).center(4 * size - 3, "-")
        lines.append(row)
        
    # دمج الشطر العلوي (المعكوس) مع الشطر السفلي لإنشاء الشكل الكامل
    print('\n'.join(lines[:0:-1] + lines))