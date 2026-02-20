# -*- coding: utf-8 -*-
from odoo import http

class MtrModule(http.Controller):
    @http.route('/mtr_module/mtr_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/mtr_module/mtr_module/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('mtr_module.listing', {
            'root': '/mtr_module/mtr_module',
            'objects': http.request.env['mtr_module.mtr_module'].search([]),
        })

    @http.route('/mtr_module/mtr_module/objects/<model("mtr_module.mtr_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('mtr_module.object', {
            'object': obj
        })
