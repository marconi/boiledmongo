<!doctype html>
<!--[if lt IE 7 ]> <html class="no-js ie6" lang="en"> <![endif]-->
<!--[if IE 7 ]>    <html class="no-js ie7" lang="en"> <![endif]-->
<!--[if IE 8 ]>    <html class="no-js ie8" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title><%block name="title"></%block></title>
    <meta name="description" content="">
    <meta name="author" content="">

    <META HTTP-EQUIV="CACHE-CONTROL" CONTENT="${h.get_settings(request, 'meta_cache_control', 'PUBLIC')}">
    <META HTTP-EQUIV="EXPIRES" CONTENT="${h.get_settings(request, 'meta_expires', '1d')}">

    <link rel="shortcut icon" href="${h.assets_url(request, '/favicon.ico')}">

    <link rel="stylesheet" href="${h.assets_url(request, '/css/style.css')}" type="text/css" />
    <script src="${h.assets_url(request, '/js/libs/modernizr-1.7.min.js')}"></script>

</head>

<body class="<%block name="body_classes"></%block>">

    <div id="container">
        <header>
            <h1 class="title"><a href="${url('home')}">PlayMongo</a></h1>
        </header>
        <div id="main" role="main">
            <%block name="content"></%block>
        </div>
        <footer>
        </footer>
    </div> <!-- eo #container -->


    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.js"></script>
    <script>window.jQuery || document.write('<script src="${h.assets_url(request, "/js/libs/jquery-1.5.1.min.js")}">\x3C/script>')</script>

    <!-- scripts concatenated and minified via ant build script-->
    <script src="${h.assets_url(request, '/js/plugins.js')}"></script>
    <script src="${h.assets_url(request, '/js/script.js')}"></script>
    <!-- end scripts-->


    <!--[if lt IE 7 ]>
        <script src="${h.assets_url(request, '/js/libs/dd_belatedpng.js')}"></script>
        <script>DD_belatedPNG.fix("img, .png_bg");</script>
    <![endif]-->

</body>
</html>