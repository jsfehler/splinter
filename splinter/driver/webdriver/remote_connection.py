import urllib3


retry = urllib3.util.Retry(total=5, redirect=3, backoff_factor=0.1)


def patch_get_connection_manager(self):
    """This replaces a method in Selenium's RemoteConnection class.

    A retry mechanism is added to try and recover from network issues.

    The patch is applied in splinter/driver/webdriver/__init__.py.
    """
    pool_manager_init_args = {"timeout": self.get_timeout(), "retries": retry}

    if self._ca_certs:
        pool_manager_init_args["cert_reqs"] = "CERT_REQUIRED"
        pool_manager_init_args["ca_certs"] = self._ca_certs

    if self._proxy_url:
        if self._proxy_url.lower().startswith("sock"):
            from urllib3.contrib.socks import SOCKSProxyManager

            return SOCKSProxyManager(self._proxy_url, **pool_manager_init_args)

        elif self._identify_http_proxy_auth():
            self._proxy_url, self._basic_proxy_auth = self._separate_http_proxy_auth()
            pool_manager_init_args["proxy_headers"] = urllib3.make_headers(proxy_basic_auth=self._basic_proxy_auth)

        return urllib3.ProxyManager(self._proxy_url, **pool_manager_init_args)

    return urllib3.PoolManager(**pool_manager_init_args)
