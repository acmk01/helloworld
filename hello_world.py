# -*- coding: utf-8 -*-

from openerp.osv import fields
from openerp.osv.orm import Model

class helloworld_test(Model):
    _name = 'helloworld.test'
    _columns = {
        # name type is char as I see it more appropriate
        # even though the task description says 'text'
        'name': fields.char('Name', size=20, required=True),
        'value': fields.integer('Value', required=True),

    }
    _sql_constraints = [('value_gte_20', 'CHECK (value >= 20)', 'Value must be >= 20 !')]

    _defaults = { 'name': lambda self,cr,uid,c=None: self.pool.get('ir.sequence').get(cr, uid, 'helloworld') }

    def cron_create(self, cr, uid, context=None):
        self.create(cr, uid, {'value': 21})
        return True

class helloworld_test2(Model):
    _name = 'helloworld.test2'
    _columns = {
        'name': fields.text('Name', required=True),
        'helloworld_test_id': fields.many2one('helloworld.test', 'Helloworld Test'),
    }


