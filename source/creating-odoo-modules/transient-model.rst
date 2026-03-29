مدل‌های موقت (Transient Model)
================================

TransientModelها برای داده‌های موقت و ویزاردها مناسب‌اند. رکوردهای این مدل‌ها پس از مدتی پاک می‌شوند و مدیریت دسترسی برای آن‌ها ساده‌تر است.

مثال:

.. code-block:: python

   from odoo import models, fields

   class ReportWizard(models.TransientModel):
       _name = 'report.wizard'
       _description = 'Report Wizard'

       date_from = fields.Date(string='Start Date')
       date_to = fields.Date(string='End Date')

استفادهٔ معمول: گرفتن ورودی از کاربر در ویزارد، اجرای یک پردازش و نمایش نتیجه یا تولید گزارش.
