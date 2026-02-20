{
    "name": "MTR Inventory Integration",
    "summary": "MTR and inventory data management with join reporting",
    "description": "Stores MTR extraction data and Business Central inventory in Odoo 13.",
    "author": "EOXS",
    "category": "Inventory",
    "version": "13.0.1.0.0",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
    ],
    "application": True,
    "installable": True,
}
