from ConnectServer import xmlrpc
import odoorpc


# Method for models
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

# Insert data
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "Jorge Sevilla",
    'email': "solopunks803@gmail.com",
    'telephone': "48991502621",
    'cep': "88040420"
}])

# Update data
ud= models.execute_kw('res.partner', 'write', [[id], {
    '902': "RG"
}])

# Search clients
sc = models.execute_kw(
    'res.partner', 'search_read',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
id

# List ten first clients
lf = models.execute_kw(
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]], 0, 10])

# Top products sales
#sales = models.execute_kw(['product.product'].search([('lst_price', 'condition', )]))


