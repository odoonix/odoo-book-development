ویژگی‌های فیلدها (Field Attributes)
====================================

فیلدها در تعریف مدل با پارامترهای کلیدواژه‌ای مشخص می‌شوند که رفتار و ظاهر آن‌ها را کنترل می‌کنند.

نمونهٔ پراستفاده:

- `string`: برچسب فیلد
- `required`: اجباری بودن فیلد
- `help`: متن راهنما
- `index`: افزودن ایندکس دیتابیس
- `default`: مقدار پیش‌فرض
- `readonly`: فقط خواندنی
- `translate`: فعال کردن ترجمه برای فیلد
- `groups`: محدود کردن دسترسی به گروه‌ها
- `store`: برای فیلدهای محاسبه‌شده که باید ذخیره شوند

مثال:

.. code-block:: python

   name = fields.Char(string="Name", required=True, help="Enter the full name")
   total = fields.Float(compute="_compute_total", store=True)

نکته: از `index=True` فقط برای فیلدهایی که در فیلترها/جستجوها زیاد استفاده می‌شوند استفاده کنید.
