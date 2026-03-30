مدل‌های انتزاعی (Abstract Model)
=================================

مدل‌های انتزاعی به عنوان کلاس پایه برای اشتراک منطق بین مدل‌های دیگر استفاده می‌شوند و جدول دیتابیس تولید نمی‌کنند.

مثال:

.. code-block:: python

   from odoo import models, fields

   class AbstractModelExample(models.AbstractModel):
       _name = 'model.name'

       field = fields.Char(string='Field Label')

از مدل‌های انتزاعی برای قرار دادن منطق مشترک (مانند متدها یا فیلترها) استفاده کنید.
