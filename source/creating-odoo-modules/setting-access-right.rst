تعریف دسترسی‌ها (Access Rights)
=================================

برای کنترل اینکه کدام کاربران می‌توانند رکوردها را ایجاد، خواند، ویرایش یا حذف کنند، باید گروه‌های کاربری و فایل `ir.model.access.csv` را تنظیم کنید. بدون دسترسی مناسب، منوها و نماها برای کاربران مخفی خواهد شد.

مراحل کلی:

1. پوشه `security/` بسازید و فایل `groups.xml` (در صورت نیاز) را تعریف کنید.
2. فایل `security/ir.model.access.csv` را اضافه کنید.
3. فایل‌های امنیتی را در `__manifest__.py` تحت کلید `data` اضافه کنید.

نمونهٔ `ir.model.access.csv`:

::

   id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
   access_visa_application_user,access.visa.application.user,model_visa_application,base.group_user,1,1,1,1

نمونهٔ گروه:

.. code-block:: xml

   <record id="new_user_group" model="res.groups">
       <field name="name">user</field>
       <field name="users" eval="[(4, ref('base.group_user'))]"/>
   </record>

همیشه بعد از تغییر فایل‌های امنیتی ماژول را ارتقا دهید تا تغییرات اعمال شود.
