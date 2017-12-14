import zipfile

def setProxy(config, taskData):
    rawProxy = config['proxies'][0]
    taskData['proxy'] = rawProxy
    config['proxies'].remove(rawProxy)
    proxy = {'host': rawProxy.split(':')[0],
             'port': rawProxy.split(':')[1],
             'username': rawProxy.split(':')[2],
             'password': rawProxy.split(':')[3]}
    return proxy

def createProxyPlugin(proxy):
    manifestJson =  """
    {
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
    "proxy",
    "tabs",
    "unlimitedStorage",
    "storage",
    "<all_urls>",
    "webRequest",
    "webRequestBlocking"
    ],
    "background": {
    "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
    }
    """
    backgroundJs = """
    var config = {
    mode: "fixed_servers",
    rules: {
    singleProxy: {
    scheme: "http",
    host: """ + '"' + proxy['host'] + '"' + """,
    port: parseInt(""" + proxy['port'] + """)
    },
    bypassList: ["foobar.com"]
    }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
    return {
    authCredentials: {
    username: """ + '"' + proxy['username'] + '"' + """,
    password: """ + '"' + proxy['password'] + '"' + """
    }
    };
    }

    chrome.webRequest.onAuthRequired.addListener(
    callbackFn,
    {urls: ["<all_urls>"]},
    ['blocking']
    );
    """
    proxyPlugin = 'proxyPlugin.zip'
    with zipfile.ZipFile(proxyPlugin, 'w') as zp:
        zp.writestr("manifest.json", manifestJson)
        zp.writestr("background.js", backgroundJs)
    return proxyPlugin

def proxyHandling(config, taskData):
    if config['proxies'][0] != 'localhost':
        proxy = setProxy(config, taskData)
        proxyPlugin = createProxyPlugin(proxy)
        return proxyPlugin
    taskData['proxy'] = 'localhost'
