# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv

class product_brand(osv.osv):
    _name = 'product.brand'
    _description = "Product brands"
    _columns = {
        'name': fields.char('Brand Name', size=32, required=True, translate=True),
        'description': fields.text('Description',translate=True),
        'partner_id' : fields.many2one('res.partner','partner', help='Select a partner for this brand if it exist'),
        'logo': fields.binary('Logo File')
    }
product_brand()    

class product_template(osv.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    _columns = {
        'product_brand_id' : fields.many2one('product.brand','Brand', help='Select a brand for this product'),
    }
product_template
