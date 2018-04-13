# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.connector.components.mapper import mapping
from odoo.addons.component.core import Component


class SaleOrderStateMapper(Component):
    _name = 'prestashop.sale.order.state.import.mapper'
    _inherit = 'prestashop.import.mapper'
    _apply_on = 'prestashop.sale.order.state'

    _model_name = 'prestashop.sale.order.state'

    direct = [
        ('name', 'name'),
    ]

    @mapping
    def backend_id(self, record):
        return {'backend_id': self.backend_record.id}

    @mapping
    def company_id(self, record):
        return {'company_id': self.backend_record.company_id.id}


class SaleOrderStateImporter(Component):
    _name = 'prestashop.sale.order.state.importer'
    _inherit = 'translatable.record.importer'
    _apply_on = 'prestashop.sale.order.state'

    """ Import one translatable record """
    _model_name = [
        'prestashop.sale.order.state',
    ]

    _translatable_fields = {
        'prestashop.sale.order.state': [
            'name',
        ],
    }


class SaleOrderStateBatchImporter(Component):
    _name = 'prestashop.sale.order.state.direct.batch.importer'
    _inherit = 'prestashop.direct.batch.importer'
    _apply_on = 'prestashop.sale.order.state'

    _model_name = 'prestashop.sale.order.state'
