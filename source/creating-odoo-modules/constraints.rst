محدودیت‌ها (Constraints)
==========================

برای حفظ یکپارچگی داده‌ها Odoo از دو نوع محدودیت پشتیبانی می‌کند: محدودیت‌های SQL و محدودیت‌های پایتون.

SQL Constraints:

.. code-block:: python

   _sql_constraints = [
       (
           'constraint_name',
           "CHECK( (state IN ('sale', 'done') AND date_order IS NOT NULL) OR state NOT IN ('sale', 'done') )",
           'Confirmed sales orders must have a confirmation date.'
       )
   ]

Python Constraints (با دکوراتور `@api.constrains`):

.. code-block:: python

   from odoo import models, fields, api, _
   from odoo.exceptions import ValidationError

   class YourModel(models.Model):
       _name = 'your.model'

       product_id = fields.Many2one('product.product')

       @api.constrains('product_id')
       def check_product_is_not_kit(self):
           if some_condition:
               raise ValidationError(_("A product with a kit-type bill of materials cannot have a reordering rule."))

محدودیت‌ها باید به گونه‌ای نوشته شوند که پیام خطا برای کاربر معنا داشته باشد.
