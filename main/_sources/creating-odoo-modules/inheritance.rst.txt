وراثت در Odoo (Inheritance)
================================

وراثت مکانیزمی است که اجازه می‌دهد رفتار و ساختار مدل‌ها و نماها را توسعه یا تغییر دهیم بدون تغییر کد اصلی.

انواع اصلی:

- Classical Inheritance: ایجاد یک مدل جدید که از مدل والد ارث می‌برد و جدول جدیدی می‌سازد.
- Prototype (extension) Inheritance: با `_inherit` مدل موجود را توسعه می‌دهیم؛ جدول جدید ساخته نمی‌شود.
- Delegation Inheritance (`_inherits`): ترکیب دو مدل با ایجاد رابطه‌ی one2many/Many2one و بازنشر فیلدها.
- View Inheritance: ارث‌بری از نماها با استفاده از `inherit_id` و XPath برای درج یا ویرایش گره‌ها.

مثال Classical:

.. code-block:: python

   class ParentModel(models.Model):
       _name = 'parent.model'
       name = fields.Char(string='Name')

   class ChildModel(models.Model):
       _name = 'child.model'
       _inherit = 'parent.model'
       date = fields.Date(string='Date')

مثال View Inheritance (XPATH):

.. code-block:: xml

   <record id="product.view.form.inherit.custom" model="ir.ui.view">
       <field name="name">product.view.form.inherit.custom.module</field>
       <field name="inherit_id" ref="product.view_form"/>
       <field name="arch" type="xml">
           <xpath expr="//field[@name='name']" position="after">
               <field name="custom_field"/>
           </xpath>
       </field>
   </record>
