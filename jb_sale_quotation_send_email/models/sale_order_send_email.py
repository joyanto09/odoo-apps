# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT


class SendSaleOrderQuotationEmail(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # for rec in self:
        res = super(SendSaleOrderQuotationEmail, self).action_confirm()
        self.send_email()
        return res


    def send_email(self):

        print("Successfully Done", self.name)
        template_id = self.env.ref('jb_sale_quotation_send_email.sale_order_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)