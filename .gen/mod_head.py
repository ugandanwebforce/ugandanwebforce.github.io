def run(options):
    return '''
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="/assets/css/hacker.css">

        <!-- Our own CSS -->
        <link rel="stylesheet" href="/assets/css/nav-menu.css">
        <link rel="stylesheet" href="/assets/css/task-entry.css">
        <link rel="stylesheet" href="/assets/css/ui-xtd.css">
        <title>{}</title>
    </head>
    '''.format(options['page_title'])
