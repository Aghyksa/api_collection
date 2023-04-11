{
	'name': 'API Collection',
	'summary': 'API Collection',
	'description': '''
					purchase dealer,
					purchase dealer management,
					Purchase Dealer Management
					   ''',

	'category': 'website',
	'version': '12.0.1',
	'price':  269,
	"currency": "EUR",
	'author': 'Lyon',
	'license':  'Other proprietary',
	'live_test_url':  '',
	'depends': [
						# 'website_purchase',
						'website',
						'purchase',
						'account',
						'cro',
						'base',
						'base_setup',
						'portal',
						'hr_attendance',
					  ],

	'data': [],
	'demo': [],
	'qweb': ['static/src/xml/*.xml'],
	'images': ['static/description/Banner_v12.gif'],
	'application': True,
	'sequence': 7,
	'pre_init_hook': '',
}
