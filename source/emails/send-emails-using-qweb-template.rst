ارسال ایمیل با قالب QWeb
=========================

ایمیل یکی از قدرتمندترین و مقرون‌به‌صرفه‌ترین ابزارهای بازاریابی است. توانایی ارسال فوری پیام به هر نقطه‌ای از جهان، آن را از سایر کانال‌ها متمایز می‌کند. اما ساختن یک ایمیل خوب برای هر بار ارسال، کاری زمان‌بر است. **قالب‌های ایمیل (Email Templates)** این مشکل را حل می‌کنند — یک بار ساخته می‌شوند و بارها استفاده می‌شوند.

در اودو، قالب‌های ایمیل با استفاده از XML و زبان قالب‌سازی **QWeb** تعریف می‌شوند و به مدل ``mail.template`` وابسته هستند.

ساخت قالب ایمیل با XML
------------------------

در زیر یک مثال کامل از یک قالب ایمیل خوش‌آمدگویی برای کارمندان جدید آمده است:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <odoo>
       <data noupdate="1">
           <record id="mail_template_employee_welcome" model="mail.template">
               <field name="name">HR: Employee Welcome Email</field>
               <field name="model_id" ref="hr.model_hr_employee"/>
               <field name="subject">Welcome to the Company, <t t-out="object.name"/></field>
               <field name="email_from">{{ user.email_formatted }}</field>
               <field name="email_to">{{ object.work_email or '' }}</field>
               <field name="auto_delete" eval="False"/>
               <field name="body_html" type="html">
                   <div>
                       Dear <t t-out="object.name or 'Employee'"/>,
                       <br/><br/>
                       We are excited to welcome you to our company!
                       We look forward to working with you.
                       <br/><br/>
                       Please feel free to reach out if you have any questions.
                       <br/><br/>
                       Best regards,
                       <br/>
                       <t t-esc="user.name"/>
                       <br/>
                       Human Resources Team
                   </div>
               </field>
           </record>
       </data>
   </odoo>

توضیح فیلدهای قالب
--------------------

- **id:** شناسه یکتای رکورد. در مسیر **Settings > Technical > Email > Templates** قابل مشاهده است.
- **model** (در ``<record>``)‌: مدل مرتبط با رکورد قالب — همیشه ``mail.template`` است.
- **name:** نام نمایشی قالب برای شناسایی آن.
- **model_id:** مدلی که این قالب به آن تعلق دارد (مثلاً ``hr.employee``).
- **subject:** عنوان ایمیل. می‌توان از متغیرهای پویا استفاده کرد.
- **email_from:** آدرس ایمیل فرستنده.
- **email_to:** آدرس ایمیل گیرنده.
- **body_html:** محتوای HTML ایمیل که با QWeb می‌توان داده‌های پویا را درون آن نمایش داد.

مشاهده قالب‌های ایمیل
-----------------------

پس از ساخت قالب، آن را در مسیر **Settings > Technical > Email > Templates** مشاهده خواهید کرد. از آنجا می‌توانید قالب را پیش‌نمایش گرفته یا ویرایش کنید.

ارسال ایمیل با استفاده از کد Python
--------------------------------------

اگر بخواهید یک قالب ایمیل را از یک تابع Python سفارشی فراخوانی کنید، می‌توانید از روش زیر استفاده کنید:

.. code-block:: python

   def send_custom_email(self):
       """Send email using predefined template"""
       template = self.env.ref('module_name.mail_template_employee_welcome')
       template.send_mail(self.id, force_send=True)

در این مثال:

- ``self.env.ref(...)`` قالب را با استفاده از XML ID آن پیدا می‌کند.
- ``send_mail(self.id)`` ایمیل را با داده‌های رکورد جاری می‌فرستد.
- ``force_send=True`` باعث می‌شود ایمیل فوراً ارسال شود (نه از طریق صف ارسال).

.. note::

   با ترکیب قالب‌های ایمیل و توابع Python، می‌توانید جریان‌های ارتباطی خودکار، حرفه‌ای و یکپارچه بسازید. این روش در پیاده‌سازی گردش‌کار (workflow) های سفارشی بسیار رایج است.
