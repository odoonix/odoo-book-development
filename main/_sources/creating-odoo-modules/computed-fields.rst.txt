فیلدهای محاسبه‌شده (Computed fields)
=====================================

فیلدهای محاسبه‌شده مقدارشان از روی فیلدهای دیگر محاسبه می‌شود و با آرگومان `compute` تعریف می‌شوند. برای مشخص کردن وابستگی‌ها از `@api.depends()` استفاده کنید.

مثال ساده:

.. code-block:: python

   from odoo import models, fields, api

   class YourModel(models.Model):
       _name = 'your.model'

       amount = fields.Float(string='Amount')
       total = fields.Float(string='Total', compute='_compute_total')

       @api.depends('amount')
       def _compute_total(self):
           for rec in self:
               rec.total = rec.amount * 2

اگر می‌خواهید مقدار محاسبه‌شده ذخیره شود از `store=True` استفاده کنید. برای پذیرفتن مقدار از UI و برگرداندن آن به فیلدهای منبع از `inverse` استفاده می‌شود.

.. code-block:: python

   total = fields.Float(string='Total', compute='_compute_total', inverse='_inverse_total', store=True)
