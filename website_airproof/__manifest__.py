{
   'name': 'Airproof Theme',
   'description': '...',
   'category': 'Website/Theme',
   'version': '17.0.1.0',
   'author': '...',
   'license': 'LGPL-3',
   'depends': ['website'],
   'data': [
      'data/presets.xml',
      'views/header.xml'
   ],
   'assets': {
   'web._assets_primary_variables': [
      'website_airproof/static/src/scss/primary_variables.scss',
   ],
      'web.assets_frontend': [
      'website_airproof/static/src/scss/font.scss',
   ],
    'web._assets_frontend_helpers': [
      ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
   ],
    'web.assets_frontend': [
      'website_airproof/static/src/scss/theme.scss',
   ],
      'web.assets_frontend': [
      'website_airproof/static/src/js/theme.js',
   ],
   },
   'installable' : True,
   'application' : True,   
}
