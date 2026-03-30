فیلدهای مالی (Monetary)
================================

فیلدهای `Monetary` برای ذخیره مقادیر مالی همراه با ارز مربوطه استفاده می‌شوند. این فیلد معمولاً با فیلد `currency_id` مرتبط است.

نمونه:

.. code-block:: python

   from odoo import fields, models

   class FeeInherit(models.Model):
       _inherit = "school.student"

       company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
       currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
       tuition_amount = fields.Monetary(string='Tuition Amount', currency_field='currency_id')


می‌توانید به جای `Monetary` از `Float` استفاده کنید و در نما از ویجت `monetary` بهره ببرید:

.. code-block:: xml

   <field name="tuition_amount" widget="monetary"/>
