فیلدهای مرتبط و مرجع (Related & Reference Fields)
=================================================

Related fields: برای نمایش مقدار فیلدی از یک مدل مرتبط (معمولاً از طریق Many2one) از `related` استفاده می‌کنیم.

.. code-block:: python

   partner_id = fields.Many2one('res.partner', string='Partner')
   partner_name = fields.Char(related='partner_id.name', string='Partner Name')

به‌طور پیش‌فرض relatedها خواندنی و ذخیره‌نشده هستند؛ برای ذخیره از `store=True` استفاده کنید.

Reference fields: فیلدی است که می‌تواند یک رکورد از چند مدل متفاوت را ارجاع دهد. از `fields.Reference` با پارامتر `selection` استفاده می‌شود.

.. code-block:: python

   reference = fields.Reference(selection=[('sale.order','Sale Order'), ('purchase.order','Purchase Order')], string='Document Reference')

یا با یک متد دینامیک:

.. code-block:: python

   reference = fields.Reference(selection='get_model_list', string='Linked Document')

   @api.model
   def get_model_list(self):
       models = self.env['ir.model'].search([])
       return [(model.model, model.name) for model in models]
